# copy and deepcopy is used to copy a mutable list
import copy

Numbers = [1, 2, 3, 4, 5, 6, 7]

copiedNumbers = copy.copy(Numbers)

copiedNumbers.append(88)
copiedNumbers[1] = 42
print(copiedNumbers)
print(Numbers)  # The first list remains the same
