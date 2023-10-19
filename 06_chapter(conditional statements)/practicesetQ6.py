#  WRITE A PROGRAM TO CONVERT MARKS INTO GRADES
marks = int(input("ENTER YOUR MARKS: "))
if(marks >= 90  or marks == 100 ):
    print("YOUR GRADE IS 'Ex'")
elif(marks >= 80):
    print("YOUR GRADE IS 'A'")
elif(marks >= 70):
        print("YOUR GRADE IS 'B' ")
elif(marks >= 60):
         print("YOUR GRADE IS 'C' ")
elif(marks >= 50):
          print("YOUR GRADE IS 'D' ")
else:
       print("SORRY YOU FAILED YOUR GRADE IS 'F'")