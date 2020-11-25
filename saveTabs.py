# saveTabs.py 
# This script will save Google Chrome's tabs website to open later

import pyautogui, pyperclip, json
from time import sleep

SLEEP_TIME = 0.5

# This function assumes you're already in Goolge Chrome
def readTabURL():
    pyautogui.click(1308, 55)
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    link = pyperclip.paste()
    print(link)
    pyautogui.click(1908, 301)  # Click somewhere else
    return link

data = {}
data['pastTabs'] = []
pyautogui.hotkey('win', '5')
sleep(SLEEP_TIME)

firstURL = readTabURL()
data['pastTabs'].append(firstURL)

pyautogui.hotkey('ctrl', 'tab')
nextTabURL = readTabURL()

while nextTabURL != firstURL:
    data['pastTabs'].append(nextTabURL)
    sleep(SLEEP_TIME)
    
    pyautogui.hotkey('ctrl', 'tab')
    nextTabURL = readTabURL()


with open('pastTabs.json', 'w') as outfile:
    json.dump(data, outfile)