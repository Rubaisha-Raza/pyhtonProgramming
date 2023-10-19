#WRITE A PYTHON FUNCTION TO PRINT MULTIPLICATION TABLE OF A GIVEN NUMBER...
def table(num):
 for i in range(1,11,+1):
  if i == 11:
   return 1
  print (num, " x " ,i, " = ",(num*i))



n = int(input("ENTER THE NUMBER TO PRINT THE TABLE: "))
table(n)