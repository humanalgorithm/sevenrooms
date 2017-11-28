import datetime as dt
from logger import Logger
from reservation import Reservation
from time_calc import TimeCalculuation
from table import TableList

log = Logger().log


class ReservationService():
    def __init__(self):
        self._unfilled_reservations = []

    def add_unfilled_reservation(self, reservation):
        self._unfilled_reservations.append(reservation)

    def get_unfilled_reservations(self):
        return self._unfilled_reservations

    def add_reservation_block(self, start_time, party_sizes):
        party_sizes_sorted = sorted(party_sizes, key=lambda k: k, reverse=True)
        for party_size in party_sizes_sorted:
            self.add_reservation(party_size, start_time)

    def add_reservation(self, party_size, start_time):
        reservation = ReservationBuilder().get_reservation(party_size, start_time)
        eligible_tables = self._get_size_appropriate_tables(party_size)
        table_priority_list = self._get_tables_sorted_by_closest_to_max_size(eligible_tables, party_size)

        for table_priority_obj in table_priority_list:
            table = table_priority_obj['table']
            can_be_booked = TimeCalculuation().get_reservation_time_can_be_added(table.get_reservations(), reservation)
            if can_be_booked:
                self._add_reservation_to_table(reservation, table)
                log("reservation_added", {"table_name": table.name, "reservation": reservation})
                return
        log("reservation_blocked", reservation)
        self.add_unfilled_reservation(reservation)

    def _add_reservation_to_table(self, reservation, table):
        table.add_reservation(reservation)
        existing_reservations = table.get_reservations()
        table.set_free_times(TimeCalculuation().compute_free_blocks(existing_reservations))

    def _get_size_appropriate_tables(self, party_size):
        table_list = TableList().get_tables()
        return filter(lambda x: x.seat_min <= party_size and x.seat_max >= party_size, table_list)

    def _get_tables_sorted_by_closest_to_max_size(self, eligible_tables, party_size):
        # table that is the best fit will be the one where the max capacity is closest to our party size
        # we then sort on number of existing reservations to prioritize tables that have the least utilization
        table_list = [{"table": table, "seat_diff": table.seat_max - party_size,
                       "existing_reservations": len(table.get_reservations())} for table in eligible_tables]
        seat_diff_ascending = sorted(table_list, key=lambda k: (k['seat_diff'], k['existing_reservations']))
        return seat_diff_ascending


class ReservationBuilder():
    def __init__(self):
        self._time_addition_blocks = {
            "1": {"hours": 0, "minutes": 45},
            "2_to_3": {"hours": 1, "minutes": 30},
            "4_to_6": {"hours": 2, "minutes": 0},
            "7_to_10": {"hours": 2, "minutes": 30}
        }

    def get_reservation(self, party_size, start_time):
        time_addition = {}
        if party_size == 1:
            time_addition = self._time_addition_blocks['1']
        elif party_size >= 2 and party_size <= 3:
            time_addition = self._time_addition_blocks['2_to_3']
        elif party_size >= 4 and party_size <= 6:
            time_addition = self._time_addition_blocks['4_to_6']
        elif party_size >= 7 and party_size <= 10:
            time_addition = self._time_addition_blocks['7_to_10']

        time_delta = dt.timedelta(hours=time_addition['hours'], minutes=time_addition['minutes'])
        end_time = (dt.datetime.combine(dt.date(1, 1, 1), start_time) + time_delta).time()
        return Reservation(start=start_time, end=end_time, party_size=party_size)
