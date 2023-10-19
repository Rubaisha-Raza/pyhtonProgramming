import random #generate random things
 
def game(comp,you):
 if comp == you:
  return None
 elif comp == 's':
  if you == 'w':
   return False
  elif you == 'g':
   return True 
 elif comp == 'w':
  if you == 'g':
   return False
  elif you == 's':
   return True 
 elif comp == 'g':
  if you == 's':
   return False
  elif you == 'w':
   return True 

  
print("COMPUTER'S TURN: SNAKE(s) WATER(w) GUN(g)? ")
randNo = random.randint(1,3)
if randNo == 1:
   Comp = 's'
elif randNo == 2:
  comp = 'w'
elif randNo == 3:
  comp ='g'
you=input(("PLAYER'S TURN: SNAKE(s) WATER(w) GUN(g)? "))
a = game(comp,you)
print(f"COMPUTER CHOSE: {comp}")

print(f"PLAYER CHOSE: {you}")

if a == None:
 print("the game is a tie :-/ ") 
elif a:
 print("WOW! YOU WIN!!!!! :-D ") 
else:
 print("ALAS! YOU LOSE :-( ")