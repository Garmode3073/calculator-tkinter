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


# activate
screen.mainloop()
