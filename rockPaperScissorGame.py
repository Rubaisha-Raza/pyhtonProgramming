import random
def game(comp,you):
 if comp == you:
  return None
 elif comp == 'r':
  if you == 's':
   return False
  elif you == 'p':
   return True 
 elif comp == 'p':
  if you == 'r':
   return False
  elif you == 's':
   return True 
 elif comp == 's':
  if you == 'p':
   return False
  elif you == 'r':
   return True 
  
  print("COMPUTER'S TURN: SNAKE(s) WATER(w) GUN(g)? ")
randNo = random.randint(1,3)
if randNo == 1:
   Comp = 'r'
elif randNo == 2:
  comp = 'p'
elif randNo == 3:
  comp ='s'
you=input(("PLAYER'S TURN: ROCK(r) PAPER(p) SCISSOR(s)? "))
a = game(comp,you)
print(f"COMPUTER CHOSE: {comp}")

print(f"PLAYER CHOSE: {you}")

if a == None:
 print("the game is a tie :-/ ") 
elif a:
 print("WOW! YOU WIN!!!!! :-D ") 
else:
 print("ALAS! YOU LOSE :-( ")