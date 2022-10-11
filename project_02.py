import random
randNumber = random.randint(1,50)
# print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input('Enter Your guess: '))
    guesses += 1
    if(userGuess == randNumber):

        print("You nailed it... Congratulations")
    else:
        if(userGuess>randNumber):
            print('You missed, please Try smaller number')
        else:
            print("You missed, please Try larger number")

print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
    
if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))