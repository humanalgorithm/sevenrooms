from time_calc import TimeCalculuation, TimeUtility

class Table():
    def __init__(self, name, seat_min, seat_max):
        self.name = name
        self.seat_min = seat_min
        self.seat_max = seat_max
        self.reservations = []
        self.free_times = TimeCalculuation().get_free_time_blocks_after_adding_schedule_block(self.reservations)

    def __repr__(self):
        return "Name: {} Seat Range: {}-{} Reservations: {} Free Times: {}".format(
            self.name, self.seat_min, self.seat_max, self.reservations, self.free_times)

    def set_free_times(self, free_times):
        self.free_times = free_times

    def get_free_times(self):
        return self.free_times

    def get_reservations(self):
        return self.reservations

    def add_reservation(self, reservation):
        self.reservations.append(reservation)
        self.reservations = TimeUtility().sort_times(self.reservations)


class TableList:
    class __TableList:
        def __init__(self, table_setup):
            self.table_setup = table_setup
            self.tables = {}
            self.init_tables()

        def init_tables(self):
            for key, value in self.table_setup.iteritems():
                seat_min = min(value)
                seat_max = max(value)
                table = Table(name=key, seat_min=seat_min, seat_max=seat_max)
                self.tables[key] = table
    instance = None
    def __init__(self, table_setup=None):
        if not TableList.instance:
            TableList.instance = TableList.__TableList(table_setup)

    def get_tables(self):
        return getattr(self.instance, "tables")
