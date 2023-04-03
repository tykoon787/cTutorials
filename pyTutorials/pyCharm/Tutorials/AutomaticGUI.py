import pyautogui

print('-------------------------------')
print('Getting The Size of a Screen')
print('-------------------------------')

wh = pyautogui.size()
print(wh)

print('-------------------------------')
print('Moving the Mouse')
print('-------------------------------')

for i in range(10):
    print(f'Move Number: {i}')
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

print('-------------------------------')
print('Getting Mouse Position')
print('-------------------------------')

while True:
    print(pyautogui.position())  # Get the position
    print(pyautogui.position().x)  # To get the x attribute i.e., the position on the x asis
    print(pyautogui.position()[0])


print('-----------------------------')
print('Clicking with Mouse')
print('-------------------------------')

import pyautogui as pyg
pyg.click(100, 100, button='right')  # Click using the right button
# pyg.click(100, 100, button='left')

print('-------------------------------')
print('Dragging the Mouse')
print('-------------------------------')

import pyautogui, time
time.sleep(5)

pyautogui.click() # Click to make the window Active
distance = 20
change = 20

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)  # Move right.
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)  # Move down.
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up.