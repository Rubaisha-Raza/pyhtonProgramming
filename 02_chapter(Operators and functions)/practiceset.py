# 1.program to add two numbers

# from audioop import avg


a = 21
b = 13
print("the addition of two numbers is : ",a,"+" ,b,"=", a+b)


# #2. program to find a reminder when number is divided by 2

num = 5
print("the remainder of the",num,"when divided by 2 is =",num%2)

# user input and type casting
num1 = int(input("Enter any number: "))
print("the remainder of the",num1,"when divided by 2 is =",num1%2)
print("the type of the " ,num1,"is ",type(num1))


# 3. use comparision oeprators to show that a is greater then b
print("the value of a (",a,")is greater then b (",b,")",(a<b))

# # 4.find the average of two numers given by the user

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
avg = (x+y)/2
print("the average of the numbers",x,"and",y, "is:" ,avg)

# #5.program to find the square of a number 
sq = int(input("enter the number you want to calculate the square of:"))  
print("the square of the number is :",(sq*sq))