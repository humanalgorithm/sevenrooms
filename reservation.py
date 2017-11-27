from random import shuffle
from time_calc import TimeCalculuation
from table import TableList

class ReservationService():
    def add_reservation(self, party_size, time_block):
        eligible_tables = self._get_size_appropriate_tables(party_size)
        table_list_priority = self._get_tables_sorted_by_closest_to_max_size(eligible_tables, party_size)

        for table_priority_obj in table_list_priority:
            table = table_priority_obj['table']
            can_add_time_block = TimeCalculuation().get_time_block_can_be_added(table.get_reservations(), time_block)

            if can_add_time_block:
                self._add_reservation_to_table(time_block, table)
                print "table time block was added {} {}".format(table.name, time_block)
                print " "
                return

        print "couldnt find a suitable reservation for {}".format(time_block, table_list_priority)
        print " "

    def _add_reservation_to_table(self, time_block, table):
        table.add_reservation(time_block)
        existing_reservations = table.get_reservations()
        table.set_free_times(TimeCalculuation().get_free_time_blocks_after_adding_schedule_block(existing_reservations))

    def compute_table_to_add_reservation(self):
        pass

    def _get_size_appropriate_tables(self, party_size):
        table_list = TableList().get_tables()
        eligible_tables = []
        for key in table_list:
            table = table_list[key]
            if party_size >= table.seat_min and party_size <= table.seat_max:
                print "appending party size {} seat min {} seat max {}".format(party_size, table.seat_min, table.seat_max)
                eligible_tables.append(table)

        return eligible_tables

    def _get_tables_sorted_by_closest_to_max_size(self, eligible_tables, party_size):
        #table that is the best fit will be the one where the max capacity is closest to our party size
        table_list = []
        for table in eligible_tables:
            seat_diff = table.seat_max - party_size
            table_list.append({"table": table, "seat_diff": seat_diff})

        shuffle(table_list)
        seat_diff_ascending = sorted(table_list, key=lambda k: k['seat_diff'])
        print "seat ascending is ", seat_diff_ascending
        print " "
        return seat_diff_ascending