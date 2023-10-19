#Q1 TO MAKE A DICTIONARY AND MAKE USER LOOK INTO IT BY INPUT  METHOD
dict = {
    "thicket":"wood",
    "house": "place of residence",
    "room": "free space",
    "furniture": "large movable equipment"
}
key = input("Enter the key value ")
print("THE VALUE CORRESPONDING TO THE KEY IS \n" ,dict.get(key))

#Q2 INPUT 8 NUMBERS FROM THE USER AND DISPLAY ALL UNIQUE NUMBERS
s = set()
s.add(input("ENTER THE NUMBER "))
s.add(input("ENTER THE NUMBER "))
s.add(input("ENTER THE NUMBER "))
s.add(input("ENTER THE NUMBER "))
s.add(input("ENTER THE NUMBER "))
s.add(input("ENTER THE NUMBER "))
s.add(input("ENTER THE NUMBER "))
s.add(input("ENTER THE NUMBER "))
print(s)