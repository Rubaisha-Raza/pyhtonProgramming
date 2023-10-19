#   WRITE A PROGRAM TO PRINT A TABLE OF A GIVEN NUMBER USING FOR LOOP
#01. given number
for i in range (1,11):
    j = i*2
    print("2 X ",i, " = " ,j)

#02. user input
i = int(input("ENTER NUMBER YOU WANT THE TABLE OF ")) 
for j in range (1,11):
   # print(i," X ",j, " = " ,(i*j))
  #  print (f"{i}X{j}={i*j}") #f string
    print(str(i)+"x"+str(j)+"="+str(i*j))
    