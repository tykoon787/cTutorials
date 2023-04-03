while True:
    print('Who are you?')
    name = input()
    if name != 'Jessica':
        continue # The continue keyword makes restart the loop
    print('Hello Jessica, Please Enter the password: ')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')