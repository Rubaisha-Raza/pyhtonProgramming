import random 
low = 1
high = 100
guesses = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"GUESS THE NUMBER BETWEEN {low} - {high}: "))
    guesses +=1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct")
        break
print(f"THIS ROUND TOOK YOU {guesses} GUESSES")