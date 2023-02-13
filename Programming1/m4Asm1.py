# 1
def turn_clockwise(compass):
    if compass == "N":
        return "E"
    elif compass == "E":
        return "S"
    elif compass == "S":
        return "W"
    elif compass == "W":
        return "N"
    else:
        return "None"


# 2
def day_name(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    else:
        return "None"


# 3
def day_num(day):
    if day == "Sunday":
        return 0
    elif day == "Monday":
        return 1
    elif day == "Tuesday":
        return 2
    elif day == "Wednesday":
        return 3
    elif day == "Thursday":
        return 4
    elif day == "Friday":
        return 5
    elif day == "Saturday":
        return 6
    else:
        return "None"


# 4
def day_add(day, add):
    if day_num(day) == "None":
        return "None"
    else:
        return (day_name((day_num(day) + add) % 7))


# 5
## It works because with the operation %, it always return a positive answer

# 6
def days_in_month(month):
    if month == "January" or month == "March" or month == "May" or month == "July" \
            or month == "August" or month == "October" or month == "December":
        return 31
    elif month == "April" or month == "June" or month == "September" or month == "November":
        return 30
    elif month == "February":
        return 28
    else:
        return "None"


# 7,8
def to_secs(hour, minute, second):
    return int(hour * 60 * 60 + minute * 60 + second)


# 9
def hour_in(sec):
    return int(sec / 3600)


def minutes_in(sec):
    return int((sec / 60) % 60)


def seconds_in(sec):
    return int(sec % 60)



