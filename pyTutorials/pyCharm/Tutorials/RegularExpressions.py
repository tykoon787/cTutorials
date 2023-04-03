# Finding a Phone Number for example
import pyperclip


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print(isPhoneNumber("445-332-1234"))

# Finding a phone number in a large string

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my number.'

for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print(f'Phone number found: {chunk}')
print('Done')

# Finding Patterns Using Regular Expressions
print('''Finding Patters Using Regular Expressions (Also called regex
''')
import re

phoneNumberRegEx = re.compile(r'\d{3}-\d{3}-\d{4}')  # Short for r'\d\d\d-\d\d\d-\d\d\d\d'
mo = phoneNumberRegEx.search("My phone number is 123-455-8599")
print(f'Phone Number Found: {mo.group()}')

# Grouping with parenthesis
parenthesis_phoneNumberRegEx = re.compile(r'(\d{3})-(\d{3}-\d{4})')  # Notice the use of Parenthesis to create groups
parenthesis_mo = parenthesis_phoneNumberRegEx.search("My phone number is 123-455-8599")
print(f'Group 1: {parenthesis_mo.group(1)}')  # Will print the area code or the first group
print(f'Group 2: {parenthesis_mo.group(2)}')  # Will print the second group
print(f'Group 0: {parenthesis_mo.group(0)}')  # Will print everything

print(f'Printing all groups: {parenthesis_mo.groups()}')  # You will notice that the result is returned in the form
# of a tuple
#  you can use the multiple-assignment trick to assign each value to a separate variable
areaCode, mainNumber = parenthesis_mo.groups()
print(areaCode)
print(mainNumber)

print('----------------------------------------')
print('Matching Multiple Groups Using the PIPE')
print('----------------------------------------')

heroRegEx = re.compile(r'Batman|Tina Fay')  # Notice that there is no spacing between '|' and the words
mo1 = heroRegEx.search('Batman')
print(mo1.group())

mo2 = heroRegEx.search('Tina Fay and Batman')
print(f'{mo2.group()}')

print('----------------------------------------')
print('Optional Matching with question')
print('----------------------------------------')
# Used to find a match regardless of whether a bit of the text is present or not

batRegEx = re.compile(r'Bat(wo)?man')
mo3 = batRegEx.search("The Adventures of Batman")
print(f'{mo3.group()}')

mo4 = batRegEx.search("The adventures of Batwoman")
print(f'{mo4.group()}')

# The (wo)? part of the regular expression means that the pattern wo is
# an optional group

phoneAreaRegEx = re.compile(r'((\d{3}-)?\d{3}-\d{4})')
mo5 = phoneAreaRegEx.search("My Phone Number is 254-768-1415")
print(f'{mo5.group()}')

mo6 = phoneAreaRegEx.search("My Other Phone Number is 768-1415")
print(f'{mo6.group()}')

print('----------------------------------------')
print('Matching Zero or More with the Star')
print('----------------------------------------')

batRegEx2 = re.compile(r'Bat(wo)*man')
mo7 = batRegEx2.search('The Adventures of Batman')
print(f'{mo7.group()}')

mo8 = batRegEx2.search("The Adventures of Batwoman")
print(f'{mo8.group()}')

mo9 = batRegEx2.search("The Adventures of Batwowoman")
print(f'{mo9.group()}')

# For 'Batman', the (wo)* part of the regex matches zero instances of wo
# in the string; for 'Batwoman', the (wo)* matches one instance of wo; and for
# 'Batwowowowoman', (wo)* matches four instances of wo

print('----------------------------------------')
print('Matching One or More with the Plus(+)')
print('----------------------------------------')

batRegEx3 = re.compile(r'Bat(wo)+man')
mo10 = batRegEx3.search("The Adventures of Batwoman")
print(f'{mo10.group()}')

mo11 = batRegEx3.search("The Adventures of Batwowowoman")
print(f'{mo11.group()}')

mo12 = batRegEx3.search("The Adventures of Batman")
print(mo12 == None)

print('----------------------------------------')
print('Using Find All')
print('----------------------------------------')

phoneNumberRegEx2 = re.compile(r'\d{3}-\d{3}-\d{3}-\d{3}')  # With No Groups
print(phoneNumberRegEx2.findall("Cell: 254-768-141-511 Work: 254-711-234-567"))

phoneNumberRegEx3 = re.compile(r'(\d{3})-(\d{3})-(\d{3})-(\d{3})')  # With No Groups
print(phoneNumberRegEx3.findall("Cell: 254-768-141-511 Work: 254-711-234-567"))

print('----------------------------------------')
print('Caret and Dollar Sign Characters')
print('----------------------------------------')

# The ^ symbol is used at the start of a regex to indicate that a match must occur at the beginning of the searched text.
# The $ symbol is used at the end of a regex to indicate that a match must occur at the end of the searched text.

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search("Hello World"))

print(beginsWithHello.search("He Said Hello") == None)

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your Number is 42'))

print(endsWithNumber.search("42 Doesnt End") == None)

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('12345667'))

print('----------------------------------------')
print('Wild Card Character')
print('----------------------------------------')

# The result is cat, hat, sat, lat and mat

atRegEx = re.compile(r'.at')
print(atRegEx.findall('The Cat in the hat sat on the flat mat'))

print('----------------------------------------')
print('Matching Everything with Dot-Star .*')
print('----------------------------------------')

nameRegEx = re.compile(r'First Name: (.*) Last Name: (.*)')
mo13 = nameRegEx.search('First Name: Larry Last Name: Evans')
print(f'{mo13.group(1)}')
print(f'{mo13.group(2)}')

print('----------------------------------------')
print('CASE SeNsItIvE Matching')
print('----------------------------------------')

regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.I)  # re.I or re.IGNORECASE ignores the case
print(robocop.search('RoboCop is part of Man, part Machine, all cop').group())

print(robocop.search('ROBOCOP is part of Man, part Machine, all cop').group())

print('----------------------------------------')
print('Substituting String with the sub()')
print('----------------------------------------')

namesRegEx = re.compile(r'Agent \w+')
print(namesRegEx.sub('CENSORED', 'Agent Alice gave the Secret documents to Agent Bob'))

agentNamesRegEx = re.compile(r'Agent (\w)\w*')
result = agentNamesRegEx.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double Agent')
print(f'{result}')

print('----------------------------------------')
print('Managing Complex RegEXes')
print('----------------------------------------')

phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 \d{3} # first 3 digits
 (\s|-|\.) # separator
 \d{4} # last 4 digit
 (\s*(ext|x|ext.)\s*\d{2,5})? # extension
 )''', re.VERBOSE)

text = str(pyperclip.past())
phoneRegex.findall(text)


