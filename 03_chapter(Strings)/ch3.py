# string
 # 1 String indexing concatenation 

name = "rubaisha"
greetings = "Hello"
c = name + " " +greetings
print("The output is " ,c)

print(c[8])

#2 string slicing 
#print(c[0:8]) #includes lower limit(0) but will end just before the upper limit(7)

#3 negetive index
print(c[-16:-1])

#4 skipping characters in a string
print(c[0::2])

#5 string functions
#a FIND
poem = '''TWINKLE TWINKLE litle STARS
HOW I WONDER WHAT YOU ARE
UP ABOVE THE WORLD SO HIGH
LIKE A DIAMOND IN THE SKY'''

poem = poem.find("litle")
print(poem)

#b REPLACE
poem = '''TWINKLE TWINKLE litle STARS
HOW I WONDER WHAT YOU ARE
UP ABOVE THE WORLD SO HIGH
LIKE A DIAMOND IN THE SKY'''
newpoem = poem.replace("litle" ,"LITTLE")
print(newpoem)

#c LENGTH
print(len(poem))
#d ENDSWITH
print(poem.endswith("SKY"))
#e CAPITALIZED
print(poem.capitalize())
#f WORD COUNT
print(newpoem.count("L"))