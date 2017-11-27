import datetime as dt
from time_calc import  TimeBlock
from table import TableList
from reservation import ReservationService

time_5_pm = dt.time(17, 0, 0)

time_530_pm = dt.time(17, 30, 0)
time_9_pm = dt.time(21, 0 ,0)

time_6_pm = dt.time(18, 0, 0)
time_7_pm = dt.time(19, 0, 0)

time_730_pm = dt.time(19, 30, 0)
time_745_pm = dt.time(19, 45, 0)



class RunProgram():
    table_setup = {"A": range(1, 2+1), "B": range(1, 2+1), "C": range(1, 2+1),
                   "D": range(2, 4+1), "E": range(2, 4+1), "F": range(2, 4+1),
                   "G": range(1, 4+1), "H": range(6, 8+1), "I": range(4, 10+1)}

    def run(self):
        table_list = TableList(self.table_setup).get_tables()

        print "adding reservations...."
        time_block1 = TimeBlock(time_6_pm, time_7_pm)
        time_block2 = TimeBlock(time_730_pm, time_745_pm)
        time_block3 = TimeBlock(time_5_pm, time_530_pm)

        ReservationService().add_reservation(8, time_block1)
        ReservationService().add_reservation(1, time_block2)
        ReservationService().add_reservation(1, time_block3)

        import pprint
        print " "
        pprint.pprint(table_list, indent=4)


run_program = RunProgram()
run_program.run()
#TimeCalculuation().run()

