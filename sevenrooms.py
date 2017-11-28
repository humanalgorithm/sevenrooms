import pprint
import datetime as dt
from table import TableList
from reservation_service import ReservationService

time_5_pm = dt.time(17, 0, 0)
time_6_pm = dt.time(18, 0, 0)
time_630_pm = dt.time(18, 30, 0)
time_700_pm = dt.time(19, 00, 0)
time_730_pm = dt.time(19, 30, 0)
time_800_pm = dt.time(20, 00, 0)


class TableReservationSimulation():
    table_setup = []

    def run(self):
        raise NotImplementedError


class TableReservationSimulation1(TableReservationSimulation):
    table_setup = [{"name": "A", "min": 1, "max": 2}, {"name": "B", "min": 1, "max": 2},
                   {"name": "C", "min": 1, "max": 2}, {"name": "D", "min": 2, "max": 4},
                   {"name": "E", "min": 2, "max": 4}, {"name": "F", "min": 2, "max": 4},
                   {"name": "G", "min": 1, "max": 4}, {"name": "H", "min": 6, "max": 8},
                   {"name": "I", "min": 4, "max": 10}]

    def run(self):
        table_list = TableList(self.table_setup).get_tables()
        reservation_service = ReservationService()
        # 5pm
        party_sizes = [1, 1, 2, 4, 4]
        reservation_service.add_reservation_block(start_time=time_5_pm, party_sizes=party_sizes)
        # 6pm
        party_sizes = [1, 1, 2, 2]
        reservation_service.add_reservation_block(start_time=time_6_pm, party_sizes=party_sizes)
        # 630 pm
        party_sizes = [4, 6, 7]
        reservation_service.add_reservation_block(start_time=time_630_pm, party_sizes=party_sizes)

        party_sizes = [2, 2, 2, 4, 4, 4, 8]
        reservation_service.add_reservation_block(start_time=time_700_pm, party_sizes=party_sizes)

        party_sizes = [1, 2, 5]
        reservation_service.add_reservation_block(start_time=time_730_pm, party_sizes=party_sizes)

        party_sizes = [2, 4, 5]
        reservation_service.add_reservation_block(start_time=time_800_pm, party_sizes=party_sizes)

        return reservation_service


class RunProgram():
    def run_program(self):
        table_reservation_sim = TableReservationSimulation1()
        reservation_service = table_reservation_sim.run()
        table_list = TableList().get_tables()
        self.display_reservations(table_list)
        self.display_unbooked_reservations(reservation_service)

    def display_reservations(self, table_list):
        for table in table_list:
            print " "
            print "Table name: {}".format(table.name)
            print "Table seating: {}-{}".format(table.seat_min, table.seat_max)
            print "-"*64
            print "Reservations:"
            pprint.pprint(table.get_reservations(), indent=2)
            print ""
            print "Free Times: "
            pprint.pprint(table.get_free_times(), width=20)


    def display_unbooked_reservations(self, reservation_service):
        print ""
        print "*" * 64
        print "The following reservations were not able to be booked:"
        unfilled = reservation_service.get_unfilled_reservations()
        pprint.pprint(unfilled, indent=2)


run_program = RunProgram()
run_program.run_program()
