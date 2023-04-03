#! python3
# MapIt - A Simple Script that opens google maps to show location of a place when passed as an argument
import webbrowser, sys

import pyperclip

if len (sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')
