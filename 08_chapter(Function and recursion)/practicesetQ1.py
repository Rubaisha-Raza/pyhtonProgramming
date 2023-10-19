# WRITE A PROGRAM USING FUNCTION TO FIND THE GREATEST OF THREE NUMBERS:
#user define
def maximum(num1,num2,num3):
    return max(num1,num2,num3)
a = int(input("ENTER 1ST NUMBER: "))
b = int(input("ENTER 2nd NUMBER: "))
c = int(input("ENTER 3rd NUMBER: "))
max1 = maximum(a,b,c)
print(max1)

#pre define()
def maximum(num1,num2,num3):
    return max(num1,num2,num3)
max1 = maximum(8,5,3)
print(max1)

#another method
def maximum(num1,num2,num3):
   if (num1>num2):
    if (num1>num3):
       return(num1)
    elif (num2>num1):
       if(num2>num3):
          return(num2)
    else:
       return(num3)
max1 = maximum(8,5,3)
print(max1)
# OR
def maximum(num1,num2,num3):
   if (num1>num2):
    if (num1>num3):
       return(num1)
    else:
        return(num3)
   else:
     if(num2>num1):
       if(num2>num3):
          return(num2)
     else:
        return(num3)
max1 = maximum(18,5,3)
print(max1)