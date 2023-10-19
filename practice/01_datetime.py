# program to find curent date and time 
import datetime
now = datetime.datetime.now()
print("Current date time are: ")
print(now.strftime("%d-%m-%y  %H:%M"))

# Program to find Current date:

current_date = datetime.date.today()
print("current date is", current_date.strftime("%d-%m-%Y"))

#Program to fine current Time:

current_time = datetime.datetime.now().time()
print("Current time is: " ,current_time.strftime("%H:%M"))

#Program to convert time from 24hrs to 12hrs

current_time = datetime.datetime.now().time()
print("Current time is: " ,current_time.strftime("%I:%M %p"))