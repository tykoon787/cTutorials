print('''User Input Can be validated using the isX() Method''')

while True:
    print('Enter Your Age: ', end='')
    age = input()
    if age.isdecimal():
        break
    print('Please Enter a number for your Age')

while True:
    print('Please Enter a new password: ', end='')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')