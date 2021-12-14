import random
i = 1
while 1 > 0:
    computerchoice1 = ["rock", "paper", "scissors"]
    computerchoice = random.choice(computerchoice1)
    userchoice = input("Enter a selection: rock, paper, scissors: \n")
    if userchoice not in computerchoice1:
        print('invalid selection - try again')
        break
    print("computer: " + computerchoice)
    if computerchoice == 'rock' and userchoice == 'rock':
        print("draw")
    if computerchoice == 'rock' and userchoice == 'paper':
        print("you win")
    if computerchoice == 'rock' and userchoice == 'scissors':
        print("you loose")
    if computerchoice == 'scissors' and userchoice == 'scissors':
        print("draw")
    if computerchoice == 'scissors' and userchoice == 'rock':
        print("you win")
    if computerchoice == 'scissors' and userchoice == 'paper':
        print("you loose")
    if computerchoice == 'paper' and userchoice == 'paper':
        print("draw")
    if computerchoice == 'paper' and userchoice == 'scissors':
        print("you win")       
    if computerchoice == 'paper' and userchoice == 'rock':
        print("you loose")

