# imports
import random
import time
#game vars
snake = ["ð", 100]
money = ["ð°", 50]
skull = ["ð", 3]
lemon = ["ð", 1]
cherry = ["ð", 20]
eball = ["ð±", 8]
seven = ["7ï¸â£", 77]
digits = [snake, money, skull, lemon, cherry, eball, seven]
cash = 50
#intro
print("Let's play Slotð!")
print("You're starting with $50, each spin costs $1")
print("Good Luck!")
print()
#functions
def odds(digits):
    choices = []
    for _ in range(random.randrange(3, 7)):
        choice = random.choice(digits)
        if choice not in choices: choices.append(choice)
    return choices
def spinner(digits):
        temp = random.choice(digits)[0]
        print(f'\b{temp}', end= "")
        time.sleep(0.5)
def pline(a,b,c):
    print('[ ', end = "")
        #spinner(digits)
    print(f"{a[0]} | ", end = "")
    #spinner(digits)
    print(f"{b[0]} | ", end = "")
    #spinner(digits)
    print(f"{c[0]} ]")
def spin(digits):
    line = []
    for x in range(3):
        slot = random.choice(digits)
        line.append(slot)
    return line
#gameplay
pcash = cash
while True:
    user = input("Press <enter> to spin, \'c\' to cashout:  ")
    if user == "c":
        if pcash == cash:
            print()
            print(f"You broke even, winnings = ${pcash -  cash}")
        if pcash > cash:
            print()
            print(f"You came out ahead, winnings = ${pcash -cash}")
        if pcash < cash:
            print()
            print("You cashed out without winning more")
            print("than your starting amount")
            print(f"You now owe the casino: ${cash-pcash}")
        break
    if user == "":
        pcash -= 1
        a,b,c = spin(odds(digits))
        print()
        pline(a,b,c)
        if a[1] == b[1] and b[1] == c[1]:
            print("\n    Winner!")
            pcash += a[1]
            print(f"You won ${a[1]}!, cash balance = {pcash}\n")
        else:
            print(f"\nLoser, cash balance = {pcash}\n")
        if pcash == 0:
            print("You ran out of money!")
            break
