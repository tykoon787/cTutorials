# Reading and Writing Codes

from pathlib import Path

print(Path('spam', 'bacon', 'eggs'))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\NotOduor', filename))

print('-------------------------------')
print('Joining Paths')
print('-------------------------------')
homeFolder = Path('C:/Users/NotOduor')
subFolder = Path('Spam')
print(homeFolder / subFolder)  # Joined Paths using the '\' operator

print('-------------------------------')
print('Current Working Direcrory')
print('-------------------------------')

import os

currentWorkingDirectory = Path.cwd()  # To ge the Current Working Directory
print(f'{currentWorkingDirectory}')
# To change the current working directory, we use os.chdir() os.chdir('C:/Users/Oduor')  # You can uncomment this to
# demonstrate the changing of directory but be sure to return it to its initial cwd
print(Path.cwd())

print('-------------------------------')
print('Absolute vs Relative Paths')
print('-------------------------------')
# the .\ and ..\ are the operands for relative paths
# C:\User\NotOduor is the way to write an absolute path

print('-------------------------------')
print('Creating New Folders')
print('-------------------------------')
import os

# os.makedirs('C:/NotUsers/NotOduor/NotSpam')  # This can make a directory and a subdirectory at the same time

# Path(r'C:/NotUsers/NotOduor/NotBacon').mkdir()  # This can only make one directory at a time

print('---------------------------------------------')
print('Getting an Absolute Path From a Relative Path')
print('---------------------------------------------')
# We use the is_absolute()

print(Path.cwd().is_absolute()) # This will bring true because Path.cwd() is an absolute Path

print(Path('my/relative/path').is_absolute()) # This will bring False because this is a relative path

converted = Path.cwd() / Path('my/relative/path')  # This will convert a relative path to an absolute Path
print(f'{converted}')
print(f'{converted.is_absolute()}')

print('-------------------------------')
print('Getting File Size')
print('-------------------------------')
filesize = os.path.getsize('C:/Users/Oduor')

print(f'{filesize} bytes')

print('-------------------------------')
print('Listing Directories')
print('-------------------------------')
directoryListing = os.listdir('C:/Users/Oduor')
print(f'{directoryListing}')

print('-------------------------------')
print('Using GLOB')
print('-------------------------------')
p = Path('C:/Users/Oduor/Downloads')
print(p.glob('*'))
print(list(p.glob('*')))

print(list(p.glob('*.docx')))

print('-------------------------------')
print('Reading and Writing a File')
print('-------------------------------')

path2 = Path('spam.txt')
path2.write_text("Hello Dear Reader")

print(path2.read_text())

print('----------------------------------------------------')
print('Reading and writing a File using the open() Function')
print('----------------------------------------------------')

helloFile = open(Path.home() / 'hello.txt')
print(helloFile.read())

print('--------------------')
print("Writing to the File")  # If the file is non existent, the 'w' will create it
print('--------------------')
baconFile = open('bacon.txt', 'w')
baconFile.write("This is a new bacon File \n")
baconFile.close()

print('------------------------------------------')
print("Appending (or Adding) a string to the File")
print('------------------------------------------')
baconFile = open('bacon.txt', 'a')
baconFile.write("This only inserts more Text into the Bacon File")
baconFile.close()

print("Reading The file ")
baconFile = open('bacon.txt')
print(baconFile.read())
baconFile.close()


print('-------------------------------')
print('Reading Multiple Lines ')
print('-------------------------------')

manyLines = open(Path.home() /'anotherHello.txt')
print(manyLines.readlines())


print('---------------------------------------------------')
print('Saving Variables (Like Settings) Using a Shelf File')
print('---------------------------------------------------')

import shelve
shelfFile = shelve.open('mySettings')
cats = ['Zookie', 'Jessica', 'Ashley', 'Tamara']
shelfFile['cats'] = cats
shelfFile.close()

# Just like dictionaries, shelf values have keys() and values() methods that
# will return list-like values of the keys and values in the shelf. Since these
# methods return list-like values instead of true lists, you should pass them
# to the list() function to get them in list form

# Opening the Settings File
shelfFile = shelve.open('mySettings')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

print('-------------------------------')
print('Saving Variables with pprint.pformat()')
print('-------------------------------')

import pprint

dogs = [{'name':'Doggie', 'desc': 'chubby'}, {'name':'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(dogs))

fileObject = open('myDogs.py', 'w')
fileObject.write('dogs =' + pprint.pformat(dogs) + '\n')
fileObject.close()