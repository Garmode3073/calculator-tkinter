from tkinter import *

# create and edit tkinter window
screen = Tk()
screen.title("Calculator")
screen.geometry("500x700")
screen.resizable(0, 0)
screen.config(bg='DarkOrchid4')

# upper panal
center_panel = Canvas(screen, bg='MediumOrchid',
                      height=70, width=476)
center_panel.place(x=10, y=10)

center_panel2 = Canvas(screen, bg='MediumOrchid',
                       height=470, width=476)
center_panel2.place(x=10, y=100)


# labels and buttons
display = Label(center_panel, text='0', bg='MediumOrchid', fg='white', justify=RIGHT, anchor="e",
                font=('Roboto', 30), relief=GROOVE, height=1, width=20)
display.place(x=9, y=5)

allclear = Button(center_panel2, text='AC', font=('Roboto', 20, 'bold'),
                  bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: allclear())
allclear.place(x=30, y=30)

plus = Button(center_panel2, text='+', font=('Roboto', 20, 'bold'),
              bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('+'))
plus.place(x=120, y=30)

minus = Button(center_panel2, text='-', font=('Roboto', 20, 'bold'),
               bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('-'))
minus.place(x=210, y=30)

multiply = Button(center_panel2, text='*', font=('Roboto', 20, 'bold'),
                  bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('*'))
multiply.place(x=300, y=30)

divide = Button(center_panel2, text='/', font=('Roboto', 20, 'bold'),
                bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('/'))
divide.place(x=390, y=30)

# numbers

one = Button(center_panel2, text='1', font=('Roboto', 30, 'bold'),
             bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('1'))
one.place(x=30, y=120)

two = Button(center_panel2, text='2', font=('Roboto', 30, 'bold'),
             bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('2'))
two.place(x=140, y=120)

three = Button(center_panel2, text='3', font=('Roboto', 30, 'bold'),
               bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('3'))
three.place(x=250, y=120)

four = Button(center_panel2, text='4', font=('Roboto', 30, 'bold'),
              bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('4'))
four.place(x=360, y=120)

five = Button(center_panel2, text='5', font=('Roboto', 30, 'bold'),
              bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('5'))
five.place(x=30, y=240)

six = Button(center_panel2, text='6', font=('Roboto', 30, 'bold'),
             bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('6'))
six.place(x=140, y=240)

seven = Button(center_panel2, text='7', font=('Roboto', 30, 'bold'),
               bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('7'))
seven.place(x=250, y=240)

eight = Button(center_panel2, text='8', font=('Roboto', 30, 'bold'),
               bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('8'))
eight.place(x=360, y=240)

nine = Button(center_panel2, text='9', font=('Roboto', 30, 'bold'),
              bg='DarkOrchid4', fg='White', width=3, height=1, command=lambda: addchar('9'))
nine.place(x=30, y=360)

zero = Button(center_panel2, text='0', font=('Roboto', 30, 'bold'),
              bg='DarkOrchid4', fg='white', width=3, height=1, command=lambda: addchar('0'))
zero.place(x=140, y=360)

# backspace
backspace = Button(center_panel2, text='Backspace', font=('Roboto', 15, 'bold'),
                   bg='DarkOrchid4', fg='White', height=3, width=17, command=lambda: backspace())
backspace.place(x=250, y=360)

# calculate
calculate = Button(screen, text='Calculate', font=('Roboto', 30, 'bold'),
                   bg='MediumOrchid', fg='White', height=1, width=20, command=lambda: calculate())
calculate.place(x=15, y=590)

# functions


def allclear():
    global display
    display["text"] = "0"


def addchar(char):
    global display
    if(display["text"] == "0" or display["text"] == "SYNTAX   ERROR"):
        display["text"] = ""
    if(len(display["text"]) < 16):
        display["text"] += char


def backspace():
    global display
    if(len(display["text"]) == 1 or display["text"] == "SYNTAX   ERROR"):
        display["text"] = "0"
        return

    display["text"] = display["text"][0:len(display["text"])-1]


def calculate():
    global display
    inp = display["text"]
    try:
        display["text"] = str(eval(inp))

    except:
        display["text"] = "SYNTAX   ERROR"


# activate
screen.mainloop()
