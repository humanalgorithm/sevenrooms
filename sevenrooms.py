import datetime as dt


class TimeCalculuation():
    def run(self):
        time_5_pm = dt.time(17, 0, 0)
        time_9_pm = dt.time(21, 0 ,0)

        time_6_pm = dt.time(18, 0, 0)
        time_7_pm = dt.time(19, 0, 0)

        time_730_pm = dt.time(19, 30, 0)
        time_745_pm =  dt.time(19, 45, 0)

        print "time 5 pm: ", time_5_pm
        print "time 9 pm: ", time_9_pm

        bookings = [{"start": time_6_pm, "end": time_7_pm },
                    {"start": time_730_pm, "end": time_745_pm}]

        free_blocks = []

        earliest_free_time = time_5_pm
        end_of_night = time_9_pm
        for i in range(0, len(bookings)):
            booking = bookings[i]
            free_time_block = {"start": earliest_free_time, "end": booking['start']}
            free_blocks.append(free_time_block)
            earliest_free_time = booking['end']

            if i == len(bookings)-1:
               free_time_block = {"start": earliest_free_time, "end": end_of_night}
               free_blocks.append(free_time_block)

        print free_blocks

class Table():
    def __init__(self, name, seat_range, booked_times=None, free_times = None):
        self.name = name
        self.seat_range = seat_range
        self.booked_times = []
        self.free_times = []

    def __repr__(self):
        return "Name: {} Seat Range: {} ".format(self.name, self.seat_range)


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


# run_program = RunProgram()
# run_program.run()
TimeCalculuation().run()
