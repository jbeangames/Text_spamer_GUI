import tkinter as tk
from PIL import ImageTk, Image
import pyautogui
import time
import threading

root = tk.Tk()

root.minsize(150, 150)

message = ''

repeats = 0

delay = 0


# adds bg image
img = ImageTk.PhotoImage(Image.open("unnamed.png"))
panel = tk.Label(root, image = img).grid(column = 1)

# initalise buttons
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=3, column=1)
tk.Label(root, text="Message (pastes if left blank)").grid(row=0)
tk.Label(root, text="Repeat Number of times").grid(row=1)
tk.Label(root, text="delay (in ms)").grid(row=3)

#callBack func starts spammer based on data in text inputs
def CallBack():
    #retreve inputs
    global repeats
    global delay
    global message
    repeats = int(e2.get())
    message = e1.get()
    delay = int(e3.get())


    #checks if message is blank to display properly
    if message == '':
        message2 = 'ctrl v'
    else:
        message2 = message

    #makes lables telling input data and instructions
    l1 = tk.Label(root, text= "auto typeing " + message2 + ' ' + str(repeats) + ' times every ' + str(delay) + ' miliseconds.').grid(column= 1)

    l2 = tk.Label(root, text= "You have five seconds to refocus the text input area of your messaging app").grid(column = 1)

    root.update()

    threading.Timer(5, spam())

def spam():
    time.sleep(5)
    global repeats
    print(repeats)
    for i in range(0, repeats):  # Message sending loop
        if message != "":
            pyautogui.typewrite(message)
            pyautogui.press("enter")
        else:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("enter")

        time.sleep(int(delay) / 1000)

    #makes done label
    lDone = tk.Label(root, text= 'done').grid(row =4)

B = tk.Button(root, text ="start", command = CallBack).grid(column=1)

# title adder
root.title('The spammer')

# loop starter
root.mainloop()
