import pyautogui
import pyperclip
import re
import time
Loader = ''
Question = ''
flag = 0
pattern = ''
def openEdge():
    global Loader
    pyautogui.hotkey('win','2')
    time.sleep(0.5)
    while "loaded" not in Loader:
        time.sleep(0.5)
        pyautogui.write("loaded")
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')
        time.sleep(0.5)
        Loader = pyperclip.paste()
    Loader = ''
    pyperclip.copy('plumppillows')
def openMessages():
    global Loader
    time.sleep(0.5)
    pyautogui.hotkey('alt','d')
    pyautogui.write('https://messages.google.com/web/conversations')
    time.sleep(0.5)
    pyautogui.press('enter')
    while "Conversations" not in Loader:
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')
        time.sleep(0.5)
        Loader = pyperclip.paste()
    Loader = ''
    pyperclip.copy('plumppillows')
def get_question():
    global Question
    time.sleep(2.5)
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    time.sleep(0.5)
    pattern = r"Conversations list(.*?)\n(.*?)\n(.*?)\n"
    alltext = pyperclip.paste()
    match = re.search(pattern, alltext, re.DOTALL)
    if match:
        Question = match.group(3)
        Question = Question.strip()
        Question = Question.strip('\n')
        if Question[-1] == '?':   
            chatGPT()
    pyperclip.copy('plumppillows')  
def chatGPT():
    global Question, flag, pattern
    flag = 1
    for i in range(0,3):
        pyautogui.press('tab')
    for i in range(0,3):
        pyautogui.press('up')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','t')
    time.sleep(0.5)
    pyautogui.hotkey('alt','d')
    pyautogui.write('www.chatgpt.com')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.write(Question + '-Answer in one paragraph only')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('tab')
    pattern = r"Today(.*?)Upgrade plan"
    pattern2 = r"ChatGPT(.*?)User(.*?)\?(.*?)ChatGPT(.*?)Message ChatGPT"
    while True:
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')
        alltext = pyperclip.paste()
        match = re.search(pattern, alltext, re.DOTALL)
        if "New chat" not in match.group(1):
            time.sleep(3)
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('ctrl','c')
            alltext = pyperclip.paste()
            break
    match = re.search(pattern2, alltext, re.DOTALL)
    pyperclip.copy(match.group(4).strip().strip('?'))
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','w')
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.press('enter')
openEdge()
openMessages()
while True:
    get_question()
    if flag == 1:
        openMessages()
        flag = 0