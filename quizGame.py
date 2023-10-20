print("Welcome to the quiz: ")
playing = input("Do you want to play [yes/no]? ")

if playing.lower() != "yes":
    quit()

print("Okay! LET's PLAY :-) ")
score = 0
count = 0
answer = input(" what is 12*36  " )
if answer == "432":
    print("CORRECT!")
    score +=1
   
else:
    print("INCORRECT ")
count+=1
answer = input(" what is 8*6  " )
if answer == "48":
    print("CORRECT!")
    score +=1
   
else:
    print("INCORRECT ")
count+=1
answer = input(" what is 9*36  " )
if answer == "324":
    print("CORRECT!")
    score +=1
    
else:
    print("INCORRECT ")
count+=1
answer = input(" what is 11*11  " )
if answer == "121":
    print("CORRECT!")
    score +=1
    
else:
    print("INCORRECT ")
count+=1
answer = input(" What is the sum of 130+125+191?  " )
if answer == "446":
    print("CORRECT!")
    score +=1
    
else:
    print("INCORRECT ")
count+=1
answer = input(" If we minus 712 from 1500, how much do we get?  " )
if answer == "788":
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT ")
count+=1
    
answer = input(" 50 times of 8 is equal to?  " )
if answer == "400":
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT ")
count+=1

answer = input(" 110 divided by 10 is?  " )
if answer == "11":
    print("CORRECT!")
    score +=1 
else:
    print("INCORRECT ")
count+=1

answer = input(" 20+(90÷2) is equal to?  " )
if answer == "65":
    print("CORRECT!")
    score +=1  
else:
    print("INCORRECT ")
count+=1

answer = input("  Find the missing terms in multiple of 3: 3, 6, 9, __, 15?  " )
if answer == "12":
    print("CORRECT!")
    score +=1  
else:
    print("INCORRECT ")
count+=1

print("the number of questions IS : ",count)
print("YOUR SCORE IS : ",score)

