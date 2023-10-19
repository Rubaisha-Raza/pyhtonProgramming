#Q2 WRITE A PROGRAM TO FIND WEATHER A STUDENT IS FAIL OR PASS IF IT REQUIRES 40% TOTAL 
# #AND ATLEAST 33% TO PASS IN EACH SUBJECT
sub1 = int(input("ENTER THE MARKS OF SUBECT 1: "))
sub2 = int(input("ENTER THE MARKS OF SUBECT 2: "))
sub3 = int(input("ENTER THE MARKS OF SUBECT 3: "))

per1 = (sub1/75)*100
print(per1,"%")

per2 = (sub2/75)*100
print(per2,"%")

per3 = (sub3/75)*100
print(per3,"%")

totalper = ((sub1+sub2+sub3)/225)*100
print("TOTAL PERCENTAGE ", totalper)
if(per1 < 33 or per2 < 33 or per3 < 33):
   print("you are Fail in subject due to obtained percentage is less than 33% percentage ")
elif (totalper >= 40): 
   print("Congratulations YOU PASSED YOUR EXAM") 
else:
   print("ALAS! YOU ARE FAILED YOUR TOTAL PERCENTAGE IS LESS THAN 40")