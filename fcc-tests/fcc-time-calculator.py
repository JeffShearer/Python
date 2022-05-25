def add_time(start, duration):
    start_hours = int()
    start_mins = int()
    am_pm = str()
    add_hours = int()
    add_mins = int()
    new_mins = int()
    new_hours = int()
    new_am_pm = str()
    add_days = int()
    day_statement = "days later"
    # slice start time & duration arguments
    if len(start) == 8:
        start_hours = int(start[0:2])
        start_mins = int(start[3:5])
        am_pm =  str(start[6:8])
    else:
        start_hours = int(start[0:1])
        start_mins = int(start[2:4])
        am_pm =  str(start[5:7])


    if len(duration) == 5:
        add_hours = int(duration[0:2])
        add_mins = int(duration[4:5])
    else: 
        add_hours = int(duration[0:1])
        add_mins = int(duration[2:4])

    # Convert start hours to 24hr format

    if start_hours == 12 and am_pm == "AM":
        start_hours = 0
    elif start_hours == 12 and am_pm == "PM":
        start_hours = start_hours
    elif am_pm == "PM":
        start_hours += 12


    # Add duration to start times
    new_mins = start_mins + add_mins
    if new_mins >= 60:
        new_mins -= 60
        new_hours += 1
    #fix notation on minutes to ensure it always has two digits
    if new_mins < 10:
        new_mins = "0" + str(new_mins)


    new_hours = start_hours + new_hours + add_hours

    if new_hours >= 24:
        # note - have to convert to int to get rid of decimals - round() may round up, so can't use here.
        add_days += int((new_hours/24))
        new_hours = new_hours - (add_days*24)

    if new_hours > 12:
        new_am_pm = "PM"
        new_hours -= 12

    else:
        new_am_pm = "AM"

    
    #convert add_days & day statement if the next day
    if add_days == 1:
        add_days = str("next")
        day_statement = "day"

    
    new_time = (str(new_hours) + ":" + str(new_mins) + " " + str(new_am_pm) + " (" + str(add_days) + " " + day_statement + ")" )


    return new_time


print(add_time("11:00 AM", "3:00"))

