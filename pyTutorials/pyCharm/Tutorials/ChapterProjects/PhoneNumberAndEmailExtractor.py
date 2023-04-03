#! python3
# phoneAndEmail.py - Finds Phone Numbers and Email Addresses on the ClipBoard

import re, pyperclip

phoneNumberRegEx = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)

emailAddRegEx = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# Finding Matches in the Clipboard

text = str(pyperclip.paste())

matches = []
for groups in phoneNumberRegEx.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailAddRegEx.findall(text):
    matches.append(groups[0])

# Copying The Matches Found to Clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard: ')
    print('\n'.join(matches))
else:
    print('No Phone Numbers or Email Addresses Found.')
