# Input validation is done using pyinputplus which provides a ton of features
# nputStr() Is like the built-in input() function but has the general PyInputPlus features. You can also pass a custom validation
# function to it
# inputNum() Ensures the user enters a number and returns an int or
# float, depending on if the number has a decimal point in it
# inputChoice() Ensures the user enters one of the provided choices
# inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options
# inputDatetime() Ensures the user enters a date and time
# inputYesNo() Ensures the user enters a “yes” or “no” response
# inputBool() Is similar to inputYesNo(), but takes a “True” or “False”
# response and returns a Boolean value
# inputEmail() Ensures the user enters a valid email address
# inputFilepath() Ensures the user enters a valid file path and filename,
# and can optionally check that a file with that name exists
# inputPassword() Is like the built-in input(), but displays * characters as
# the user types so that passwords, or other sensitive information, aren’t
# displayed on the screen

import pyinputplus as pyip

response = pyip.inputInt(prompt="Enter a number: ")

response2 = pyip.inputNum("Enter Number: ", greaterThan=4)
response3 = pyip.inputNum("Enter Number: ", lessThan=4)
response4 = pyip.inputNum("Enter Number: ", min=4)

print('By default, Blank Input Is not allowed Unless the blank=True is allowed.')

response5 = pyip.inputNum('Enter Something: ', blank=True)

print('-------------------------------')
print('Allow RegEx')
print('-------------------------------')

response6 = pyip.inputNum("Enter Number: ", allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])  #The expected input is a number but
#allowRegexes creates an exception so that the roman number listed can be entered and accepted.
print(response6)
response7 = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero']) # This also allows for roman numbers in small caps
print(response7)

response8 = pyip.inputNum("Enter a number: ",blockRegexes=[r'[02468]$'])
print(response8)

print('-------------------------------')
print('Passing Custom Functions')
print('-------------------------------')

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to ten, not %s.') %(sum(numbersList))
        return int(numbers)


response9 = pyip.inputCustom(addsUpToTen)
print(response9)




