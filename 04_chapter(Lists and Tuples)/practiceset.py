#Q1  WRITE A PROGRAM TO STORE SEVEN FRUITS NAME IN A LIST ENTERED BY USER
f1=input("ENTER 1 FRUIT NAME ")
f2=input("ENTER 2 FRUIT NAME ")
f3=input("ENTER 3 FRUIT NAME ")
f4=input("ENTER 4 FRUIT NAME ")
f5=input("ENTER 5 FRUIT NAME ")
f6=input("ENTER 6 FRUIT NAME ")
f7=input("ENTER 7 FRUIT NAME ")

fruitlist=[f1,f2,f3,f4,f5,f6,f7]
print(fruitlist)


#Q2  WRITE A PROGRAM TO ENTER MARKS OF 6 STUDENTS AND DISPLAY THEM IN SORTED MANNER
s1 = int(input("enter the marks of student 1 ")) #  type casting elements because marks cannot be in string type
s2 = int(input("enter the marks of student 2 "))
s3 = int(input("enter the marks of student 3 "))
s4 = int(input("enter the marks of student 4 "))
s5 = int(input("enter the marks of student 5 "))
s6 = int(input("enter the marks of student 6 "))


studentlist=[s1,s2,s3,s4,s5,s6]
print(studentlist)
studentlist.sort()
print(studentlist)

#Q3  CHECK A TUPLE CANNOT BE CHANGED IN PYTHON

a=(1,2,3,4,5)
print(a[0])

a[0] = 6
print(a)

#Q4 WRITE A PROGRAM TO SUM A LIST WITH 4 NUMBERS 
    #using index numbers 
b = [1,2,3,4]
print("SUM OF THE LIST USING OPERATOR '+' AND 'INDEX NUMBERS' IS ",b[0]+b[1]+b[2]+b[3])
  #using method(SUM)
print("SUM OF THE LIST USING THE SUM METHOD IS ",sum(b))

#Q5  WRITE THE PROGRAM TO COUNT THE NUMBER OF ZEROES IN FOLLOWING TUPLE
tuple = (7,0,8,0,0,9) 

print(tuple.count(0))
