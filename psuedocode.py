'''
starter project
in the main:
    update
    organize
    print

function that updates schedule
    for each upcoming ship:
        get the available bays for the ship
        update the schedule by appending

Note* This if I attempt level 4:
    The function that update schedule
    for each upcoming ship:
        call the function that gets the available bays for the ship
    gets all the available paths
    gets all the times between and empty for all the paths
    choose the best one


inside the function that gets :
    use for loop to check size of each bay
        adds bays to a list
    checks if the time is available using the list by comparing the maximum 
    to mininum to all the things already on the schedule
        adds to another list
    returns the first bay (the others would be for if I attempt level 4)
        
organizing schedule inside:
    for loop every bay:
        add the min (to find need for loop) to a new list
        remove it from the current schedule
        repeat until current is empty
        then assign the new list to the current

bonus inside:
    for loop the bays then the schedules
    convert the time to human time then print it out

other function needed:
    turning the time into a decimal:
        getting the index of ':' then creating a new string to the index, period, and after
        turn into float and return iter
    turning time back into central time:
        do the same except : , and adding 0 at the end because when float it deletes it,
        and keeping it a string


            
'''

