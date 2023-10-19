# def func()    FUNCTION DEFINATION
    #print()
# func()    FUNCTION CALL


#EXAMPLE
def percent(marks):  #defining a function
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100 #WHAT A FUNCTION RETURNS(OUTPUT OF FUNCTION)
#USING FUNCTION
marks1 = [100,78,34,55] #PASSING PARAMETERS
percent1 = percent(marks1) #FUNCTION WITH ARGUMENTS
print(percent1)

#FUNCTION CAN BE CALL ANY NUMBER OF TIME IN A PROGRAM:
marks2 = [89,89,89,89]
percent2 = percent(marks2)
print(percent2)

#FUNCTION WILL PASS THE DEFAULT VALUE IF NO ARGUMENT IS PASSED TO IT:
def greet(name = "stranger"):
    return("good day," +name)
greet1 = greet("rubaisha")
print(greet1)
n = input("enter any name: ")
greet2 = greet()
print(greet2)


