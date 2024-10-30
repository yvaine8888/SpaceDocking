import dockingBays as db

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    updating_schedule()
    print()
    print_docking_bays()
    
    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below
def updating_schedule():
    for ship in db.incoming_ships:
        bay = available(ship) -1
        detail = (ship['arrival_time'], ship['departure_time'], ship['ship_name'])
        db.docking_bays[bay]['schedule'].append(detail)

def available(ship):
    filtered_size = []
    for bay in db.docking_bays:
        if bay['size'] == ship['size']:
            filtered_size.append(bay)

    filtered_time = []
    new_arrival = get_hour(ship['arrival_time'])
    new_depart = get_hour(ship['departure_time'])

    for bay in filtered_size:
        can = True
        for schedule in bay['schedule']:
            current_arrival = get_hour(schedule[0])
            current_depart = get_hour(schedule[1])
            if new_arrival < current_depart and current_arrival < new_depart:
                can = False
        if can:
            filtered_time.append(bay['bay_id'])
    return filtered_time[0]


def get_hour(s):
    index = 0
    for num in range(len(s)):
        if s[num] == ':':
            index = num
    s = s[:index]
    s = int(s)
    return s

    


if __name__ == "__main__":
    main()
