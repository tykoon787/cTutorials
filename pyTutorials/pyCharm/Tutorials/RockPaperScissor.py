import random, sys, keyboard

print('Welcome to the Rock, Paper, Scissor Game')
while True:
    print('Enter Your Name to Play: ', end='')
    try:
        name = input()
        if not name:
            raise ValueError('Error: Your Name is Required to Continue')
        else:
            print('Welcome ' + name)
            print('')
            break
    except ValueError as e:
        print(e)


# Variables
Wins = 0
Losses = 0
Ties = 0
Tries = 3

while Tries != 0:

    # Computer Moves
    r = random.randint(0, 2)
    computer_select = ''  # default computer selection
    print('')
    # print("Random Value is " + str(r))

    if r == 0:
        computer_select = 'Rock'
    elif r == 1:
        computer_select = 'Paper'
    elif r == 2:
        computer_select = 'Scissors'

    # User's Move + Computer Logic
    print('Enter Your Move: (r)ock, (p)aper, (s)cissor or (q)uit: ', end='')
    userInput = input()
    userSelection = ''
    if userInput == 'r':
        userSelection = 'Rock'
        print('ROCK Versus ...')
        print(computer_select)
        if userSelection == 'Rock' and computer_select == 'Rock':
            print("Its a Tie")
            Ties = Ties + 1
            Tries = Tries - 1
        elif userSelection == 'Rock' and computer_select == 'Paper':
            print("Computer Wins. Its Your Loss")
            Losses = Losses + 1
            Tries = Tries - 1
        elif userSelection == 'Rock' and computer_select == 'Scissors':
            print("You Win.")
            Wins = Wins + 1
            Tries = Tries - 1
    elif userInput == 'p':
        userSelection = 'Paper'
        print('PAPER')
        print('Versus ...')
        print(computer_select)
        if userSelection == 'Paper' and computer_select == 'Rock':
            print("You Win")
            Wins = Wins + 1
            Tries = Tries - 1
        elif userSelection == 'Paper' and computer_select == 'Paper':
            print("Its a Tie")
            Ties = Ties + 1
            Tries = Tries - 1
        elif userSelection == 'Paper' and computer_select == 'Scissors':
            print("You Loose.")
            Losses = Losses + 1
            Tries = Tries - 1
    elif userInput == 's':
        userSelection = 'Scissor'
        print('SCISSOR Versus')
        print(computer_select)
        if userSelection == 'Scissor' and computer_select == 'Rock':
            print("You Loose")
            Losses = Losses + 1
            Tries = Tries - 1
        elif userSelection == 'Scissor' and computer_select == 'Paper':
            print("You Win")
            Wins = Wins + 1
            Tries = Tries - 1
        elif userSelection == 'Scissor' and computer_select == 'Scissors':
            print("It's a Tie")
            Ties = Ties + 1
            Tries = Tries - 1
    elif userInput == 'q':
        print('Wins: ' + str(Wins))
        print('Losses: ' + str(Losses))
        print('Ties: ' + str(Ties))
        sys.exit()
print('---- ScoreBoard -----')
print(name)
print('---------------------')
print('Wins: ' + str(Wins))
print('Losses: ' + str(Losses))
print('Ties: ' + str(Ties))
