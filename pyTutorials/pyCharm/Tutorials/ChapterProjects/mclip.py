#! python 3
# ! mclip.py - A mutli-clipboard program

TEXT = {'agree': '''Yes I agree With you Completely. That sounds fine with me. ''',
        'busy': '''Sorry. We can do that right now because we are a little busy''',
        'upsell': '''Would you consider making this a monthly donation?'''}

import sys, pyperclip
if len (sys.argv) < 2:
    print('Usage: Python mclip.py [keyphrase]')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard')
else:
    print(f'{keyphrase} not associated with any text')