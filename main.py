import dockingBays as db
# Note: I used W3Schools to figure out append, end in print statement, and remove.

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    updating_schedule()
    organize_schedule()
    print_schedule()

# Function to update the schedule to accomodate the incoming ships
def updating_schedule():
    for ship in db.incoming_ships:
        bay = available(ship) - 1 
        detail = (ship['arrival_time'], ship['departure_time'], ship['ship_name'])
        db.docking_bays[bay]['schedule'].append(detail)

# Function to check the bays available for the ships based on size and time and return it.
## Note: I did it small to small, medium to medium, and large to large.
def available(ship):
    filtered_size = []
    for bay in db.docking_bays:
        if bay['size'] == ship['size']:
            filtered_size.append(bay)

    filtered_time = []
    new_arrival = get_time(ship['arrival_time'])
    new_depart = get_time(ship['departure_time'])

    for bay in filtered_size:
        can = True
        for schedule in bay['schedule']:
            current_arrival = get_time(schedule[0])
            current_depart = get_time(schedule[1])
            if new_arrival < current_depart and current_arrival < new_depart:
                can = False
        if can:
            filtered_time.append(bay['bay_id'])
    return filtered_time[0]

# Function to turn time into decimal and return it. Ex. 12:30 = 12.3
def get_time(s):
    index = 0
    for num in range(len(s)):
        if s[num] == ':':
            index = num

    s = s[:index] + '.' + s[index+1:]
    s = float(s)
    return s


# Function to turn decimal into time and return it. Ex. 12.3 = 12:30
def turn_back_time(s, old):
    index = 0
    s = str(s)
    for num in range(len(s)):
        if s[num] == '.':
            index = num

    s = s[:index] + ':' + s[index+1:]
    if old[4] == '0':
        s = s + '0'
    return s

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

if __name__ == "__main__":
    main()
