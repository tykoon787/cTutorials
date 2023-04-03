import random

tries = 4
secretNumber = random.randint(1,20)
print('The Secret Number is: ' + str(secretNumber))

print('You have ' + str(tries) + ' left')

for i in range(tries):
    print('Guess a number: ', end='')
    userNumber_str = input()
    userNumber_int = int(userNumber_str)
    if userNumber_int == secretNumber:
        print('Good Job. You guessed the Secret Number')
        break
    elif userNumber_int < 16 and userNumber_int != secretNumber:
        print('Your Guess is Too Low')
        continue
    elif userNumber_int > 16 and userNumber_int != secretNumber:
        print('Your Guess is Too High')
        continue

