#Q1 write a program to find the greatest of four numbers entered by user

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

# if(num1 > num2 and num1 > num3 and num1 > num4):
#  print(num1, "is greater")
# elif(num2 > num1 and num2 > num3 and num2 > num4):
#  print(num2, "is greater")
# elif(num3 > num1 and num3 > num2 and num3 > num4):
#  print(num3,"is greater")
# else:
#  print(num4, "is greater")

 #METHOD 2
if num1>num2:
  f1=num1
else:
  f1 = num2
if num3>num4:
    f2 = num3
else:
 f2 = num4

if(f1 > f2):
   print(f1, "is greatest")
else:
    print(f2, "is greatest")

