from pynput.mouse import Button, Controller

mouse=Controller()
def mice():
    mouse.position = (40,60)
    mouse.position = (20,50)
    mouse.position = (90,100)
    mouse.press(Button.right)
    mouse.release(Button.right)
