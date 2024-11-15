import dockingBays as db
import itertools
from starterProject import *
from collections import OrderedDict
# Note: I used W3Schools to figure out append, end in print statement, and remove.
# I also figured out itertools, importing, and dictionaries from GeeksforGeeks.

# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    updating_schedule()
    organize_schedule()
    print_schedule()

# Function to update the schedule to accomodate the incoming ships
def updating_schedule():
    max_bays = 0
    available_bay = []
    for ship in db.incoming_ships:
        size = available_size(ship)
        if len(size) > max_bays:
            max_bays = len(size)
        available_bay.append(size)

    possibilities = []
    for num in range(max_bays):
        possibilities.append(num)
    paths = list(itertools.product(possibilities, repeat=len(db.incoming_ships)))

    first_schedule = []
    for bay in db.docking_bays:
        first_schedule.append(bay['schedule'])

    times_between = {}
    for path in paths:
        can_do = True
        for num, bay in enumerate(path):
            try:
                bay_index = available_bay[num][bay]
                ship = db.incoming_ships[num]
                if available_time(db.docking_bays[bay_index], ship):
                    detail = (ship['arrival_time'], ship['departure_time'], ship['ship_name'])
                    db.docking_bays[bay_index]['schedule'].append(detail)      
                else:
                    can_do = False   
            except IndexError:
                can_do = False
        if can_do:
            organize_schedule()
            times_between.update({find_time_excess(): path})
        for num, bay in enumerate(db.docking_bays):
            bay['schedule'] = first_schedule[num]

        times_between = OrderedDict(sorted(times_between.items()))
        print(times_between)
        """first_key = list(times_between.keys())[0]
        best_path = times_between[first_key]

        for num, bay in enumerate(best_path):
            bay_index = available_bay[num][bay]
            ship = db.incoming_ships[num]
            detail = (ship['arrival_time'], ship['departure_time'], ship['ship_name'])
            db.docking_bays[bay_index]['schedule'].append(detail)"""

        
def find_time_excess():
    count = 0
    for bay in db.docking_bays:
        for num, the_ship in enumerate(bay['schedule']):
            first = get_time(the_ship[1])
            try:
                second = get_time(bay['schedule'][num+1][0])
            except:
                break
            count = count + second - first
        if bay['schedule'] == []:
            count = count + 24

    return count

# Function to check the bays available for the ships based on size and return it.
## Note: I did it small to small, medium to medium, and large to large.
def available_size(ship):
    filtered_size = []
    for bay in db.docking_bays:
        if bay['size'] == ship['size']:
            filtered_size.append(bay['bay_id']-1)
    return filtered_size
    
# Function to print the new schedule in a human-readable format.
def print_schedule():
    print("\nSchedule")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']}: ", end = "")
        
        for ship in bay['schedule']:
            arrival = get_time(ship[0])
            depart = get_time(ship[1])
            arr_period = ''
            dep_period = ''
            
            if arrival < 12 or arrival == 24.00:
                arr_period = 'AM'
            else:
                arr_period = 'PM'

            if depart < 12 or depart == 24.00:
                dep_period = 'AM'
            else:
                dep_period = 'PM'

            if arrival >= 13:
                arrival = arrival - 12

            if depart >= 13:
                depart = depart - 12
            
            arrival = turn_back_time(arrival, ship[0])
            depart = turn_back_time(depart, ship[1])
            
            ending = ""
            if ship != bay['schedule'][len(bay['schedule'])-1]:
                ending = ", "

            print(f"{ship[2]} - {arrival} {arr_period} to {depart} {dep_period}", end = ending)
        print()

# Function to turn time into decimal and return it. Ex. 12:30 = 12.3
def get_time(s):
    index = 0
    s = str(s)
    for num, letter in enumerate(s):
        if letter == ':':
            index = num

    s = s[:index] + '.' + s[index+1:]
    s = float(s)
    return s


# Function to turn decimal into time and return it. Ex. 12.3 = 12:30
def turn_back_time(s, old):
    index = 0
    s = str(s)
    for num, letter in enumerate(s):
        if letter == '.':
            index = num

    s = s[:index] + ':' + s[index+1:]
    if old[4] == '0':
        s = s + '0'
    return s

# Function to check if it is able to add to schedule without overlapping.
def available_time(bay, ship):
    filtered_time = []
    new_arrival = get_time(ship['arrival_time'])
    new_depart = get_time(ship['departure_time'])

    can = True
    for schedule in bay['schedule']:
        current_arrival = get_time(schedule[0])
        current_depart = get_time(schedule[1])
        if (new_arrival < current_depart and new_arrival > current_arrival) or (new_depart > current_arrival and new_depart < current_depart):
            can = False
    return can

# Function to organize the schedule based on time
def organize_schedule():
    for bay in db.docking_bays:
        result = []

        for num in range(len(bay['schedule'])):
            added_ship = bay['schedule'][0]
            min = get_time(added_ship[0])
            
            for ship in bay['schedule']:
                if get_time(ship[0]) < min:
                    min = get_time(ship[0])
                    added_ship = ship

            result.append(added_ship)
            bay['schedule'].remove(added_ship)

        bay['schedule'] = result

if __name__ == "__main__":
    main()
