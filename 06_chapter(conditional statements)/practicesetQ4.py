#   WRITE A PROGRA TO FIND WEATHER THE USERNAME CONTAIN LESS THAN 1 CHARACTERS OR NOT
name = input("Enter your Name: \n")
print(len(name))
if(len(name) < 10):
 print("username contain less than 10 characters")
elif(len(name) > 10):
   print("Username contain more than 10 characters")
else:
  print("Username contain 10 characters")