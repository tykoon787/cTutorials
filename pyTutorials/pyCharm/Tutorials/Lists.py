catNames = []

while True:
    print('Enter the name of the CAT ' + str(len(catNames) + 1) + ' (or Enter Nothing to Stop : ', end='')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]

if len(catNames) > 5:
    print("You have so many cats")
else:
    print("That's a fair amount of Cats")

# Printing everything in a list using the for loop
print('The cat Names are: ')
for name in catNames:
    print(name)

# Printing everything in a list using the range(len(listName))
print('Using the Range(len(object)) Function')
for i in range(len(catNames)):
    print(catNames[i])

# Printing the Index and Value in a list using the enumerate Function
print('Using the Enumerate function to display all items')
for index, item in enumerate(catNames):
    print(str(index) + " is: " + item)



