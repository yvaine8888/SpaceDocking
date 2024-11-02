'''
starter project
new function that updates schedule
    for each upcoming ship:
        calls the function that gets the available bays for the ship
        inside the function:
            use for loop to check size of each bay
                adds bays to a list
            then it checks if the time is available by using the list of bays (for loop)
            by comparing the maximum to mininum to all the things already on the schedule
                To do that, I need a for loop and something that returns the first two as int
                adds to another list
            returns the first bay (the others would be for if I attempt level 4)
        still inside the for loop of the first function, update the schedule by appending
        
call organizing schedule
inside:
    for loop every bay:
        add the min (to find need for loop) to a new list
        remove it from the current schedule
        repeat until current is empty
        then assign the new list to the current

call the bonus
inside the bonus
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

