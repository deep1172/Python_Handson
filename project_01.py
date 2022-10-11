# SNAKE WATER GUN GAME
import random
def gamewin(system, you):
    if system == you:
        return None
    elif system == 's':
            if you == 'w':
                return False
            elif you == 'g':
                return True
            elif system == 'w':
                if you == 'g':
                    return False
            elif you == 's':
                return True
            elif system == 'g':
                if you == 's':
                    return False
            elif you == 'w':
                return True

print("system's Turn: Snake(s) water(w) or Gun(g) ?")
randNo = random.randint(1, 3) 
if randNo == 1:
    system = 's'
elif randNo == 2:
    system = 'w'
elif randNo == 3:
    system = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)? ")
a = gamewin(system, you)

print(f"system chose {system}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")



