import datetime as dt
from time_calc import TimeCalculuation, TimeBlock
from table import TableList

class ReservationService():
    def add_reservation(self, party_size, start_time):
        time_block = ReservationPeriod().get_time_block(party_size, start_time)
        eligible_tables = self._get_size_appropriate_tables(party_size)
        table_priority_list = self._get_tables_sorted_by_closest_to_max_size(eligible_tables, party_size)

        for table_priority_obj in table_priority_list:
            table = table_priority_obj['table']
            can_add_time_block = TimeCalculuation().get_time_block_can_be_added(table.get_reservations(), time_block)
            if can_add_time_block:
                self._add_reservation_to_table(time_block, table)
                print "table time block was added {} {}".format(table.name, time_block)
                print " "
                return
        print "couldnt find a suitable reservation for time: {} party size: {}".format(time_block, party_size)
        print " "

    def _add_reservation_to_table(self, time_block, table):
        table.add_reservation(time_block)
        existing_reservations = table.get_reservations()
        table.set_free_times(TimeCalculuation().compute_free_blocks(existing_reservations))

    def _get_size_appropriate_tables(self, party_size):
        table_list = TableList().get_tables()
        return filter(lambda x: x.seat_min <= party_size and x.seat_max >= party_size, table_list)

    def _get_tables_sorted_by_closest_to_max_size(self, eligible_tables, party_size):
        #table that is the best fit will be the one where the max capacity is closest to our party size
        #we then sort on number of existing reservations to prioritize tables that have the least utilization
        table_list = [{"table": table, "seat_diff": table.seat_max - party_size,
                       "existing_reservations": len(table.get_reservations())} for table in eligible_tables]
        seat_diff_ascending = sorted(table_list, key=lambda k: (k['seat_diff'], k['existing_reservations']))
        print "seat ascending is ", seat_diff_ascending
        print " "
        return seat_diff_ascending

class ReservationPeriod():
    def __init__(self):
        self.time_addition_blocks = {
            "1": {"hours": 0, "minutes": 45},
            "2_to_3": {"hours": 1, "minutes": 30},
            "4_to_6": {"hours": 2, "minutes": 0},
            "7_to_10": {"hours": 2, "minutes": 30}
        }

    def get_time_block(self, party_size, start_time):
        time_addition = {}
        if party_size == 1:
            time_addition = self.time_addition_blocks['1']
        elif party_size >= 2 and party_size <= 3:
            time_addition = self.time_addition_blocks['2_to_3']
        elif party_size >= 4 and party_size <= 6:
            time_addition = self.time_addition_blocks['4_to_6']
        elif party_size >= 7 and party_size <= 10:
            time_addition = self.time_addition_blocks['7_to_10']

        time_delta = dt.timedelta(hours=time_addition['hours'], minutes=time_addition['minutes'])
        end_time = (dt.datetime.combine(dt.date(1,1,1),start_time) + time_delta).time()
        return TimeBlock(start=start_time, end=end_time)

