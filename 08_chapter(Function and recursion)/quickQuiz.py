# WRITE A PROGRAM TO GREET A USER WITH GOOD DAY USING FUNCTION

def greet(name): #FUNCTION DEFINATION
    return ("Good day "+name)


#METHOD 1 user define function
names1 = "Rubaisha"
greet1 = greet(names1)
print(greet1)



#method 2 user input
names = input("Enter user name: ")
greets = greet(names)
print(greets)

