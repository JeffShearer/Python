# note optional argument "day" has a default empty value to avoid breaking the function if it is not supplied
def add_time(start,duration,day=""):
    start_hours = ""
    start_mins = ""
    am_pm = str()
    add_hours = int()
    add_mins = int()
    new_mins = int()
    new_hours = int()
    new_am_pm = str()
    add_days = int()
    start_day = str()
    day_statement = ""
    day_name = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    new_day = str()
    
    # slice start & duration arguments into separate variables for calculations
    start_colon_pos = start.find(":")
    start_hours = start[0:start_colon_pos]
    start_mins = start[start_colon_pos+1:start_colon_pos+3]
    am_pm = start[start_colon_pos+4:start_colon_pos+6]
    start_hours = int(start_hours)
    start_mins = int(start_mins)

    dur_colon_pos = duration.find(":")
    add_hours = duration[0:dur_colon_pos]
    add_mins = duration[dur_colon_pos+1:dur_colon_pos+3]
    add_hours = int(add_hours)
    add_mins = int(add_mins)

    #Normalize day & look up code
    if day != "":
        start_day = day.capitalize()
        day_code = day_name.index(start_day)
        print(day_code)

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
        if day != "":
            day_code += add_days
            if day_code > 6:
                    day_code = day_code - (7*int(day_code/7))
            print(day_code)
        new_hours = new_hours - (add_days*24)

    #Converts back to 12 hour clock - note clauses for handling both 12oclock times properly.
    if new_hours == 12:
        new_am_pm = "PM"
    elif new_hours > 12:
        new_am_pm = "PM"
        new_hours -= 12
    elif new_hours == 0:
        new_am_pm = "AM"
        new_hours = 12
    else:
        new_am_pm = "AM"

    
    #convert add_days & day statement if the next day
    if add_days > 1:
        add_days = " (" + str(add_days)
        day_statement = " days later)"
    elif add_days == 1:
        add_days = str(" (next ")
        day_statement = "day)"
    else:
        add_days = ""
        day_statement = ""

    # Convert date code to new day of week
    if day !="":
        new_day = day_name[day_code]


    if day != "":
        new_time = (str(new_hours) + ":" + str(new_mins) + " " + str(new_am_pm) + ", " + str(new_day) + str(add_days) + str(day_statement)  )
    else:    
        new_time = (str(new_hours) + ":" + str(new_mins) + " " + str(new_am_pm) + str(add_days) + str(day_statement)  )


    return new_time


print(add_time("11:59 PM", "400:00","friday"))

