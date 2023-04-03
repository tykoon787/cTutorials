allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham-sandwiches': 4, 'apples': 2},
             'Carol': {'cups': 3, 'apple-pies': 5}
             }


def totalBrought(guests, items):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(items, 0)
        return numBrought


print('Total Number of Things brought by Alice Bob and Carol')
print('Apples: ' + str(totalBrought(allGuests, 'apples')))
print('Pretzels: ' + str(totalBrought(allGuests, 'pretzels')))
print('Ham-Sandwiches: ' + str(totalBrought(allGuests, 'ham-sandwiches')))
print('Cups: ' + str(totalBrought(allGuests, 'cups')))
print('Apple-Pies: ' + str(totalBrought(allGuests, 'apple-pies')))
