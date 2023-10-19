#Q1 USER ENETERD NAME AFTER GREETING
 
print("Enter your name")
name = input()
print("Hello " +name)

#Q2(a) LETTER TEMPLATE
print("Enter your name")
name = input()
print("Enter date:" )
date = input()
print("\n Dear " +name+"\n you are selected ! \n"+date+"\n")

#Q2(b) LETTER TEMPLATE USING REPLACE FUNCTION
letter = '''Dear <|NAME|>
You are Selected!

<|DATE|>'''

name= input("Enter Your Name: ")
date = input("Enter Date: ")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print("\n ",letter)

#Q3 DETECT DOUBLE SPACES IN STRING
poem = '''TWINKLE  TWINKLE LITTLE  STARS
HOW I WONDER  WHAT YOU  ARE 
UP  ABOVE THE WORLD SO  HIGH

LIKE A  DIAMOND  IN THE  SKY'''

doublespaces = poem.find("  ")
print("the number of double spaces are",doublespaces)

#Q4 REPLCE DOUBLE SPACES IN STRING WITH SINGLE SPACE
  
singleSpace = poem.replace("  "," ")
print(singleSpace)
 
#Q5 FORMTTING OF LETTER USING ESCAPE SEQUENCES
leter = '''" Dear harry, This python course is nice. Thanks!"'''
formatted_leter = '''" Dear harry, \n \tThis python course is nice.\n Thanks!"'''
print(formatted_leter)