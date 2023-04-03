import random

secretNumber = random.randint(1,20)
#print('The secret number is ' + str(secretNumber))

print('Welcome to Guess A number. You Have 6 Chances to guess the correct number.')
for guesses in range(1,7):
    print('Take a guess: ', end='')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

    if guess == secretNumber:
        print('Good Job. You have guessed the correct number in ' + str(guesses) + 'guesses!')
    else:
        print('Sorry! The correct number was ' + str(secretNumber))
