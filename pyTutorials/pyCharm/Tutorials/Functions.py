import random

def getAnswer(AnsNumber):
    if AnsNumber > 5:
        return 'Number is Greater than Five'
    elif AnsNumber < 5:
        return 'Number is less than Five'

r = random.randint(1,9)
fortune = getAnswer(r)
print(r)
print(fortune)

print(getAnswer(random.randint(1,9)))
