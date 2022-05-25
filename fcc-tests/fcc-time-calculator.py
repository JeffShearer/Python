def add_time(start, duration):
    start_hours = ""
    start_mins = ""
    am_pm = str()
    add_hours = int()
    add_mins = int()
    new_mins = int()
    new_hours = int()
    new_am_pm = str()
    add_days = int()
    day_statement = ""
    
    # slice start & duration arguments into separate variables for calculations
    start_colon_pos = start.find(":")
    start_hours = start[0:start_colon_pos]
    start_mins = start[start_colon_pos+1:start_colon_pos+3]
    start_hours = int(start_hours)
    start_mins = int(start_mins)

    dur_colon_pos = duration.find(":")
    add_hours = duration[0:dur_colon_pos]
    add_mins = duration[dur_colon_pos+1:dur_colon_pos+3]
    add_hours = int(add_hours)
    add_mins = int(add_mins)

    # Convert start hours to 24hr format
    if start_hours == 12 and am_pm == "AM":
        start_hours = 0
    elif start_hours == 12 and am_pm == "PM":
        start_hours = start_hours
    elif am_pm == "PM":
        start_hours += 12


    # compute new time:
    # add minutes, incrementing hours if >= 60
    new_mins = start_mins + add_mins
    if new_mins >= 60:
        new_mins -= 60
        new_hours += 1
    #fix notation on minutes to ensure it always has two digits
    if new_mins < 10:
        new_mins = "0" + str(new_mins)

    # add hours, incrementing days if >= 24
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
    if add_days >1:
        add_days = " (" + str(add_days)
        day_statement = " days later)"
    elif add_days == 1:
        add_days = str(" (next ")
        day_statement = " day"
    else:
        add_days = ""
        day_statement = ""

    
    new_time = (str(new_hours) + ":" + str(new_mins) + " " + str(new_am_pm) + str(add_days) + str(day_statement)  )


    return new_time


print(add_time("8:16 PM", "466:02"))

