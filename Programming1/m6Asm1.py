import calendar
#####1
# a
cal = calendar.TextCalendar()
cal.pryear(2012)
print("-" * 100)

# b
cal = calendar.TextCalendar(firstweekday=3)
cal.pryear(2012)
print("-" * 100)

# c
cal = calendar.TextCalendar()
cal.prmonth(2012, 3)
print("-" * 100)

# d
d = calendar.LocaleTextCalendar(6, "KOREAN")
#d.pryear(2012)
print("-" * 100)

#e
##It expect an integer as argument. It returns boolean. It judge if the year given is a leap year.

#####2
#a
##44 functions

#b
##celi round number up to the nearest integer
##floor round number down to the nearest integer

#c
number = 4
number ** 0.5 ##This is how, power to 0.5

#d
## pi and e

#####3
#A deep copy constructs a new compound object and then,
#recursively, inserts copies into it of the objects found in the original.

#####4
#Refer to python files

#####5
#The name of namespace_test is not it but "___main___"
# in mymodule1 we can see the statement