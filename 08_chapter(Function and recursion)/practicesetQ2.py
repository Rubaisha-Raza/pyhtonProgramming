#WRITE A PROGRAM TO CONVERT CELSIUS TO FSHRENHEIT:
#pre define
def conv(temp):
    return (temp * (9/5)) + 32.

temp1 = conv(100)
print("the temprature in fehrenheit is: " ,temp1)

#user define

def conv(temp):
    return (temp * (9/5)) + 32.
c = float(input("ENTER THE TEMPRATURE IN CELSIUS: "))
temp1 = conv((c))
print(temp1)