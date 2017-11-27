import datetime as dt
from time_calc import  TimeBlock
from table import TableList
from reservation import ReservationService

time_5_pm = dt.time(17, 0, 0)

time_530_pm = dt.time(17, 30, 0)
time_9_pm = dt.time(21, 0 ,0)

time_6_pm = dt.time(18, 0, 0)
time_7_pm = dt.time(19, 0,++ 0)

time_730_pm = dt.time(19, 30, 0)
time_745_pm = dt.time(19, 45, 0)



class RunProgram():
    table_setup = [{"name": "A", "min": 1, "max": 2}, {"name": "B", "min": 1, "max": 2},
                   {"name": "C", "min": 1, "max": 2},  {"name": "D", "min": 2, "max": 4},
                   {"name": "E", "min": 2, "max": 4}, {"name": "F", "min": 2, "max": 4},
                   {"name": "G", "min": 1, "max": 4}, {"name": "H", "min": 6, "max": 8},
                   {"name": "I", "min": 4, "max": 10}]

    def run(self):
        table_list = TableList(self.table_setup).get_tables()

        print "adding reservations...."
        '''
        5 pm
        - 2 x Party of 1
        - 1 x Party of 2
        - 2 x Party of 4

        6pm
        - 2 x Party of 1
        - 2 x Party of 2

        6:30pm
        - 1 x Party of 4
        - 1 x Party of 6
        - 1 x Party of 7
        '''
        time_5_pm = dt.time(17, 0, 0)
        time_6_pm = dt.time(18, 0, 0)
        time_630_pm = dt.time(18, 30, 0)

        # 5pm
        ReservationService().add_reservation(1, time_5_pm)
        ReservationService().add_reservation(1, time_5_pm)
        ReservationService().add_reservation(2, time_5_pm)
        ReservationService().add_reservation(4, time_5_pm)
        ReservationService().add_reservation(4, time_5_pm)

        # 6pm
        ReservationService().add_reservation(1, time_6_pm)
        ReservationService().add_reservation(1, time_6_pm)
        ReservationService().add_reservation(2, time_6_pm)
        ReservationService().add_reservation(2, time_6_pm)

        ReservationService().add_reservation(4, time_630_pm)
        ReservationService().add_reservation(6, time_630_pm)
        ReservationService().add_reservation(7, time_630_pm)

        import pprint
        print " "
        pprint.pprint(table_list, indent=4)


run_program = RunProgram()
run_program.run()
#TimeCalculuation().run()

