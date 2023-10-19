num = int(input("Enter number"))
prime = True
for i in range(2,num):
    if(num%i == 0):
     prime = False
     break
if prime:
 print("number is prime")
else:
 print("number is not prime")