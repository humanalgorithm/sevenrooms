# Sevenrooms Seating Table Reservation Program
![ScreenShot](https://raw.githubusercontent.com/humanalgorithm/sevenrooms/master/sevenrooms-screenshot.png)

## What is it? 
This program computes reservation times for a set of seating tables based on the party size to occupy the table and reservation time requested. The program comes with a script to setup a simulation of tables and reservation requests. Once the program is run it will display all of the reservations(time block and party size) per table along with the remaning free time blocks on that table. 

## How does it work? 

### Reservation Service
Requests are made to the reservation service class with a time and a party size. The reservation service can either be called with one reservation at a time or with several reservations for the same start time. 

When making a single reservation request, the service finds the best table to put a reservation by doing the following 1) get list of eligble tables based on party size 2) sort those tables in ascending order of least number of reservations, such that tables with the least number of reservations are prioritized. 

When making a request to add several reservations to one time block, the reservation requests are sorted in descending order of party size to give priority to larger reservation requests first.  

### Time Calculation
The TimeCalculation class has two public methods get_reservation_time_can_be_added and compute_free_blocks. The former method takes a time block and then determines if given the current reservations that the new block can be added with a conflict. The compute_free_blocks loops through all of the existing reservation time blocks and denotes the time inbetween reservations. 

### Reservation and TimeBlock
The TimeBlock object stores a start and end time which is of type datetime.time. The TimeBlock object is what is used to denote the storage of a time range .The reservation class extends time block and adds additional instance variable party_size to mark the size when a reservation is made. 

## How to run?
Once repo is cloned
From the /sevenrooms folder
```
python sevenrooms.py
```
