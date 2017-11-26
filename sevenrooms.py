import datetime as dt

time_5_pm = dt.time(17, 0, 0)

time_530_pm = dt.time(17, 30, 0)
time_9_pm = dt.time(21, 0 ,0)

time_6_pm = dt.time(18, 0, 0)
time_7_pm = dt.time(19, 0, 0)

time_730_pm = dt.time(19, 30, 0)
time_745_pm = dt.time(19, 45, 0)

class TimeUtility():
    def sort_times(self, time_block_list):
        sorted_list = sorted(time_block_list, key=lambda k: k.get()['start'])
        return sorted_list

class TimeCalculuation():
    def __init__(self):
        self.availability_start = dt.time(17, 0, 0)
        self.availability_end = dt.time(21, 0, 0)
        self.start_key = "start"
        self.end_key = "end"

    def get_free_blocks(self, schedule_time_blocks):
        if not schedule_time_blocks:
            return self._return_all_free()
        schedule_time_blocks = TimeUtility().sort_times(schedule_time_blocks)
        earliest_free_time = self.availability_start
        return self._process_schedule_time_blocks(schedule_time_blocks, earliest_free_time)

    def _process_schedule_time_blocks(self, schedule_time_blocks, earliest_free_time):
        free_blocks = []
        for counter in range(0, len(schedule_time_blocks)):
            schedule_time_block = schedule_time_blocks[counter]
            if not schedule_time_block.get()[self.start_key] == earliest_free_time:
                free_time_block = TimeBlock(**{self.start_key: earliest_free_time, self.end_key: schedule_time_block.get()[self.start_key]})
                free_blocks.append(free_time_block)
            earliest_free_time = schedule_time_block.get()[self.end_key]

            if counter == len(schedule_time_blocks)-1:
                free_time_block = TimeBlock(**{self.start_key: earliest_free_time, self.end_key: self.availability_end})
                free_blocks.append(free_time_block)
        return free_blocks

    def _return_all_free(self):
        free_blocks = [TimeBlock(**{self.start_key: self.availability_start, self.end_key: self.availability_end})]
        return free_blocks


class ReservationService():
    def add_reservation(self, time_block, table):
        table.add_reservation(time_block)
        existing_reservations = table.get_reservations()
        table.set_free_times(TimeCalculuation().get_free_blocks(existing_reservations))

class TimeBlock():
    def __init__(self, start, end):
        self.time_block = {"start": start, "end": end}

    def __repr__(self):
        return "{}".format(self.time_block)

    def get(self):
        return self.time_block

class Table():
    def __init__(self, name, seat_range):
        self.name = name
        self.seat_range = seat_range
        self.reservations = []
        self.free_times = TimeCalculuation().get_free_blocks(self.reservations)

    def __repr__(self):
        return "Name: {} Seat Range: {} Reservations: {} Free Times: {}".format(self.name, self.seat_range, self.reservations, self.free_times)

    def get_reservations(self):
        return self.reservations

    def set_free_times(self, free_times):
        self.free_times = free_times

    def get_free_times(self):
        return self.free_times

    def add_reservation(self, reservation):
        self.reservations.append(reservation)
        self.reservations = TimeUtility().sort_times(self.reservations)


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

        print "table A"
        table_A = table_list['A']
        reservation1 = TimeBlock(time_6_pm, time_7_pm)
        reservation2 = TimeBlock(time_730_pm, time_745_pm)
        reservation3 = TimeBlock(time_5_pm, time_530_pm)


        ReservationService().add_reservation(reservation1, table_A)
        ReservationService().add_reservation(reservation2, table_A)
        ReservationService().add_reservation(reservation3, table_A)

        print "Table A Reservations are ..."

        print table_A.get_reservations()

        print "Table A free times are"
        print table_A.get_free_times()


run_program = RunProgram()
run_program.run()
#TimeCalculuation().run()

