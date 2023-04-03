print('---------------------------')
print('MultiThreading')
print('---------------------------')

import time, datetime

startTime = datetime.datetime(2022, 4, 14, 18,51,0)
while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Programm now Exiting')