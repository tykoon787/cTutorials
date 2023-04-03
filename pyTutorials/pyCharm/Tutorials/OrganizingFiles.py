# Using the Shell Utilities Module (shutil)
# lets you copy, move, rename, and delete files in your Python programs.

print('-------------------------------')
print('Copying Files and Folders')
print('-------------------------------')

import shutil, os
from pathlib import Path

p = Path.home()
print(f'Home Path is: {p}')

# Creating the Folder To copy files into
try:
    Path(r'C:/Users/Oduor/some_folder').mkdir()
except FileExistsError:
    print('The File Already Exists')

shutil.copy(p / 'hello.txt', p / 'some_folder')
shutil.copy(p / 'bacon.txt', p / 'some_folder/bacon2.txt')
print('Copied Successfully')

print('-------------------------------')
print('Copying a Whole Folder')
print('-------------------------------')

try:
    shutil.copytree(p / 'some_folder', p / 'some_folder_backup')
    print('Folder Backup Created')
except FileExistsError:
    print('The File Was already Successfully Backed Up')

print('-------------------------------------')
print('Moving and Renaming Files and Folders')
print('-------------------------------------')

try:
    shutil.move(p / 'fileToBeMoved.txt', p / 'some_folder')
    print('Moved Successfully')
except FileNotFoundError:
    print('Cannot Find File To be Moved')

print('-------------------------------')
print('Permanently Deleting Files')
print('-------------------------------')

# Calling os.unlink(path) will delete the file at path.
# Calling os.rmdir(path) will delete the folder at path. This folder must be
# empty of any files or folders.
# Calling shutil.rmtree(path) will remove the folder at path, and all files
# and folders it contains will also be deleted.

import os
from pathlib import Path

for filename in Path.home().glob('*.txt'):
    print(f'{filename} will be Deleted')
    # os.unlink(filename)  # Commented This out because i did not want the files deleted
print('Deleted Files Successfully')

print('--------------------------------------')
print('Safe Delete with the Send2Trash Module')
print('--------------------------------------')

import send2trash

filename = 'OldBacon.txt'
newBaconFile = open(filename, 'a')  # Creates the file
newBaconFile.write('Bacon is Not a vegetatble')
newBaconFile.close()

send2trash.send2trash(filename)
print(f'{filename} Sent to Trash')

print('-------------------------------')
print('Compressing Files with the Zipfile Moddule')
print('-------------------------------')

import zipfile, os

from pathlib import Path

p = Path.home()
BaconZip = zipfile.ZipFile(p / 'bacon.zip')
filesInZip = BaconZip.namelist()  # Organizes the files in the zip folder in a list format
print(filesInZip)

for file in filesInZip:  # Loops through the list of files
    fileInfo = BaconZip.getinfo(file)
    fileSize = fileInfo.file_size
    fileCompressed = fileInfo.compress_size
    print(f'{file} is {fileSize} bytes')
    print(f'{file} when compressed is {fileCompressed} bytes')

BaconZip.close()

print('-------------------------------')
print('Extracting Zip Files')
print('-------------------------------')
import zipfile, os
from pathlib import Path

p = Path.home()
Destination_Folder = 'Bacon_folder'
baconZip = zipfile.ZipFile(p / 'Bacon.zip')
baconZip.extractall(f'C:\\Users\\Oduor\\{Destination_Folder}')
print(f'Extract Successful to {Destination_Folder}')
baconZip.close()

print('-------------------------------')
print('Creating and Adding Zip Files')
print('-------------------------------')
import zipfile
from pathlib import Path

newZip = zipfile.ZipFile('newZipFile.zip', 'w')  # Creating a newzipfile in writable mode
newZip.write('spam.txt', 'anotherspam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

workingDirectory = Path.cwd()
print(f'New Zip file created in {workingDirectory}')
# zipfile.ZIP_DEFLATED tells the computer what algorithm it should use to compress the files;
