# Checking for a Value using the in and not in operator in a list

myPets = ['Zoophie','Zara', 'CanCan', 'Doggie']

while True:
    print('Search for a Cat: ', end='')
    userInput = input()
    if userInput not in myPets:
        print("We don't have " + userInput)
        continue
    else:
        print(userInput + ' Is available')
        break

