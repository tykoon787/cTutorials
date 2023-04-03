from selenium.webdriver.common.by import By
from selenium import webdriver



print('-------------------------------')
print('Controlled Browser with Sellenium')
print('-------------------------------')



fireFoxBrowser = webdriver.Firefox()
print(type(fireFoxBrowser))
fireFoxBrowser.get('https://inventwithpython.com')

print('-------------------------------')
print('Fidning Elements')
print('-------------------------------')

# Please not that we have enclosed the code in try and except because if the element is not found it will crash.

try:
    elem = fireFoxBrowser.find_element(by=By.CLASS_NAME, value='cover-thumb')  # Finding an element by its class
    print(f'Found {elem.tag_name} with that class name')
except:
    print('Was not able to find an element with that name')

print('-------------------------------')
print('Mouse Clicks')
print('-------------------------------')

linkElem = fireFoxBrowser.find_element(by=By.LINK_TEXT, value='Read Online for Free')
print(type(linkElem))
linkElem.click()

print('-------------------------------')
print('Filling Out and Submiting Forms')
print('-------------------------------')

fireFoxBrowser.get('https://login.metafilter.com')
userElem = fireFoxBrowser.find_element(by=By.ID, value='user_name')
userElem.send_keys('Panda 21')

passElem = fireFoxBrowser.find_element(by=By.ID, value='user_pass')
passElem.send_keys('notPanda21')
passElem.submit()


print('-------------------------------')
print('Sending Special Keys')
print('-------------------------------')

from selenium.webdriver.common.keys import Keys

fireFoxBrowser.get('https://nostarch.com')
htmlElem = fireFoxBrowser.find_element(by=By.TAG_NAME, value='html')
htmlElem.send_keys(Keys.END)  # Scrolls to bottom
htmlElem.send_keys(Keys.HOME)  # Scrolls to TOP

print('-------------------------------')
print('Clicking Browser Buttons')
print('-------------------------------')

# browser.back() Clicks the Back button.
# browser.forward() Clicks the Forward button.
# browser.refresh() Clicks the Refresh/Reload button.
# browser.quit() Clicks the Close Window button.

print('-------------------------------')
print('Clicking Browser Buttons')
print('-------------------------------')

# browser.back() Clicks the Back button.
# browser.forward() Clicks the Forward button.
# browser.refresh() Clicks the Refresh/Reload button.
# browser.quit() Clicks the Close Window button.

print('-------------------------------')
print('Playing A Game')
print('-------------------------------')

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
fireFoxBrowser = webdriver.Firefox()
# chromeBrowser = webdriver.Chrome()

fireFoxBrowser.get('https://play2048.co/')


htmlElem = fireFoxBrowser.find_element(by=By.TAG_NAME, value='html')
print(type(htmlElem))
while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)


