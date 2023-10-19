#WRITE A PYTHON FUNCTION TO CONVERT INCHES INTO CENTIMETERS:
def conv(inches):
    return  inches*2.54 

length = float(input("Enter length in inches: "))
print("The converted length in centimeters is : ",conv(length))

