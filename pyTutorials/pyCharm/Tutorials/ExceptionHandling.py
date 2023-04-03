# Errors can be handled with try and except statements. The code that
# could potentially have an error is put in a try clause. The program execu-
# tion moves to the start of a following except clause if an error happens.
# You can put the previous divide-by-zero code in a try clause and have an
# except clause contain code to handle what happens when this error occurs

def divider(DivideBy):
    try:
        return 42 / DivideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument. Cannot divide a number by Zero')


print(divider(1))
print(divider(2))
print(divider(0))
# How to Catch an Empty Input from user and Output an Error
# I got this from https://stackoverflow.com/questions/19579997/how-to-catch-empty-user-input-using-a-try-and-except-in-python


# This is an example of how we can define our own error
while True:
    print('Enter Your Name to Continue: ', end='')
    try:
        name = input()
        if not name:
            raise ValueError('Error: Your Name is Required to Continue')
        else:
            print('Welcome ' + name)
            break
    except ValueError as e:
        print(e)
