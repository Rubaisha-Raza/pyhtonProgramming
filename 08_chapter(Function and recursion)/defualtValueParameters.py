#DEFAULT VALUE PARAMETER
def greet(name = 'Stranger'):
    return("Hello "+name)

names = input("enter User Name: ")
greet1 = greet(names)
print(greet1)
