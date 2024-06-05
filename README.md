# ChatGPT-for-Feature-Phones
This Project titled 'SMSavvy' helps Feature Phones interact with ChatGPT using their inbuilt SMS interface. A Desktop Automation Script built using PyAutoGUI on a standard PC running Windows 11, services the queries received through SMS by injecting them into the Web UI of ChatGPT, scraping the response and sending it back as an SMS.

## Tutorial
 - Watch the YouTube video for a step-by-step Tutorial on how to create this program: https://www.youtube.com/watch?v=LEb1HXX7ElE

## Prerequisites
 - Standard PC(Laptop/Desktop) with Windows 8/10/11.
 - A Minimum Internet speed of 4Mb/s.
 - Any Web Browser (preferably Microsoft Edge) placed as the second icon from the left in the Taskbar.
 - Google Messages installed on Phone (Android) and linked to Web Application on PC through QR Code.
 - Login to ChatGPT using Personal Account on Web Browser on PC.
 - Secondary SMS sending/receiving capable device for testing purposes.
 - IDE (preferably VSCode) installed with Python setup.
 - Additional Libraries/Modules - PyAutoGUI, Pyperclip, time, re ('pip install pyautogui','pip install pyperclip' in Windows Command Prompt)

## Caution
 - The Automation Script 'Script.py' is designed as per the Web UI of Google Messages and ChatGPT on 5th June, 2024.
 - It is important to note that changes would be needed to be made to the script if and when the UI of these websites change.
 - Changes would probably be required in the pattern matching using the re module and the number of 'tab's to be pressed.
   
## Steps for Usage
 - After all the steps in the Prerequisites are completed, download the 'Script.py' program into your local system.
 - Open it in your IDE (preferably VSCode) and run the Program.
 - If script is not running fine, manipulate the delays in time.sleep() calls throughout the program.

