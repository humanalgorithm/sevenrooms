import datetime as dt

time_5_pm = dt.time(17, 0, 0)

time_530_pm = dt.time(17, 30, 0)
time_9_pm = dt.time(21, 0 ,0)

time_6_pm = dt.time(18, 0, 0)
time_7_pm = dt.time(19, 0, 0)

time_730_pm = dt.time(19, 30, 0)
time_745_pm = dt.time(19, 45, 0)


class TimeCalculuation():
    def __init__(self):
        self.availability_start = dt.time(17, 0, 0)
        self.availability_end = dt.time(21, 0, 0)

    def sort_times(self, time_list):
        return sorted(time_list, key=lambda k: k['start'])

    def return_all_free(self):
        free_blocks = [{"start": self.availability_start, "end": self.availability_end}]
        return free_blocks

    def get_free_blocks(self, bookings):
        if not bookings:
            return self.return_all_free()

        bookings = self.sort_times(bookings)
        earliest_free_time = self.availability_start
        free_blocks = []
        for i in range(0, len(bookings)):
            booking = bookings[i]
            if booking['start'] != earliest_free_time:
                free_time_block = {"start": earliest_free_time, "end": booking['start']}
                free_blocks.append(free_time_block)
            earliest_free_time = booking['end']

            if i == len(bookings)-1:
               free_time_block = {"start": earliest_free_time, "end": self.availability_end}
               free_blocks.append(free_time_block)

        return free_blocks

class Table():
    def __init__(self, name, seat_range):
        self.name = name
        self.seat_range = seat_range
        self.bookings = []
        self.free_times = TimeCalculuation().get_free_blocks(self.bookings)

    def __repr__(self):
        return "Name: {} Seat Range: {} bookings: {} free_times: {}".format(self.name, self.seat_range, self.bookings, self.free_times)

    def add_booking(self, booking):
        self.bookings.append(booking)
        self.free_times = TimeCalculuation().get_free_blocks(self.bookings)

    def get_bookings(self):
        return self.bookings

    def get_free_times(self):
        return self.free_times

    def set_up_bookings(self):
        bookings = [{"start": time_6_pm, "end": time_7_pm},
                    {"start": time_730_pm, "end": time_745_pm},
                    {"start": time_5_pm, "end": time_530_pm}]

        for booking in bookings:
            self.add_booking(booking)

class TableList():
    def __init__(self, table_setup):
        self.table_setup = table_setup
        self.tables = {}

    def init_tables(self):
        for key, value in self.table_setup.iteritems():
            table = Table(name=key, seat_range=value)
            self.tables[key] = table

    def get_tables(self):
        if not self.tables:
            self.init_tables()
        return self.tables


class RunProgram():
    table_setup = {"A": range(1, 3), "B": range(1, 3), "C": range(1, 3),
                   "D": range(2, 5), "E": range(2, 5), "F": range(2, 5),
                   "G": range(1, 5), "H": range(6, 9), "I": range(6, 9),
                   "I": range(4, 11)}

    def run(self):
        table_list = TableList(self.table_setup).get_tables()
        print table_list

        print "table A...."
        print "----"
        table_A = table_list['A']
        table_A.set_up_bookings()
        print table_A


run_program = RunProgram()
run_program.run()
#TimeCalculuation().run()

