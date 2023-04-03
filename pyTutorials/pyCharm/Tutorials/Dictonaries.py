import pprint

birthdays = {'Jessicah': 'June 6th', 'Oduor': 'July 31st', 'Faith': 'April 2nd'}
print('To Exit Please Press Q')
while True:
    print("Search For anybody's Birthday by Entering their name: ", end='')
    name = input()
    if name == 'q' or name == 'Q':
        break

    if name in birthdays:
        print('The Birthday of ' + name + ' is ' + birthdays[name])
    else:
        print('Cannot Find ' + name + "'s Birthday")
        print('Would You like to enter their Birthday? : [Y/N] ', end='')
        userAnswer = input()
        if userAnswer == 'Y' or userAnswer == 'y':
            print("Enter " + name + "'s Birthday: ", end='')
            name = input()
            print('Birthday Database has been updated')
        elif userAnswer == 'N' or userAnswer == 'n':
            print('Would You Like to See the Database? [Y/N]: ', end='')
            quit_decision = input()
            if quit_decision == 'y' or quit_decision == 'Y':
                break
            else:
                continue

print('-------------------------')
print('Printing Values ')
print('-------------------------')
for v in birthdays.values():
    print(v)

print('-------------------------')
print('Printing Keys ')
print('-------------------------')
for k in birthdays.keys():
    print(k)
print('-------------------------')
print('Printing Items ')
print('-------------------------')
for l in birthdays.items():
    print(l)

print('-------------------------')
print('Using the get() method')
print('-------------------------')
# Takes two arguments: the key of the value to retrieve and a fallback value to return if
# that key does not exist.

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('apples', 0)) + ' apples and ' + str(picnicItems.get('cups', 0)) + ' cups')

# if the key is absent the default value will be 0 as under

print('I am also bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs')

print('-------------------------')
print('Using setdefault() method ')
print('-------------------------')
# Checks if there is a key and value pair in a dictionary and if not adds them automatically

picnicItems.setdefault('eggs', 4)
picnicItems.setdefault('blankets', 10)

print('I am also bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs')

print('-------------------------')
print('A short Counting Game to count the number of charactes appearing in a string')
print('-------------------------')

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

print('-------------------------')
print('Preety Print')
print('-------------------------')
pprint.pprint(count)