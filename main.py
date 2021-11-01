from tkinter import *
from tkinter import colorchooser
from tkinter.ttk import Combobox
import turtle as tt

MODE = "write"
PENMODE = "DOWN"
COLOR = "Black"


# Functions
def reset():
    drawer.pendown()
    penmode_l.configure(text="PENMODE: DOWN")	
    drawer.goto(0, 0)
    drawer.clear()


def choose_color():
    global COLOR
    color_code = colorchooser.askcolor(title="Choose Pen Color")
    if color_code[1]:
        COLOR = color_code[1]


def draw(x, y):
    drawer.ondrag(None)
    drawer.setheading(drawer.towards(x, y))
    if MODE == "write":
        drawer.pencolor(COLOR)
    elif MODE == "erase":
        drawer.pencolor("white")
    drawer.width(thickness_spbox.get())
    drawer.goto(x, y)
    drawer.ondrag(draw)



def change_write_mode():
    global MODE
    if MODE == "write":
        MODE = "erase"
        drawer.pendown()
        erase_b.configure(bg="black", fg="white")
    elif MODE == "erase":
        MODE = "write"
        drawer.pendown()
        erase_b.configure(bg="#0edee6", fg="black")


def change_penmode(self):
    global PENMODE
    if PENMODE == "DOWN":
        drawer.penup()
        penmode_l.configure(text="PENMODE: UP")
        PENMODE = "UP"
    elif PENMODE == "UP":
        drawer.pendown()
        penmode_l.configure(text="PENMODE: DOWN")
        PENMODE = "DOWN"    


# Create GUI
window = Tk()
window.title("Drawing App")
window.geometry("+0+0")
window.config(padx=25, pady=50)
window.iconbitmap("favicon.ico")

window.bind("<p>", func=change_penmode)

img = PhotoImage(file="color-wheel.png")
color = Button(window, image=img, command=choose_color)
color.grid(column=0, row=0)

thickness_spbox = Spinbox(from_=1, to=25, width=5)
thickness_spbox.grid(column=1, row=0)

erase_b = Button(window, text="Erase", bg="#0edee6", command=change_write_mode)
erase_b.grid(column=2, row=0, padx=25)

clear_b = Button(window, text="Clear", bg="#09ff00", command=reset)
clear_b.grid(column=3, row=0)

canvas = Canvas(window, width=600, height=600)
canvas.grid(column=0, row=1, columnspan=4, pady=(25, 25))

penmode_l = Label(window, text="PENMODE: DOWN", font=("Times New Roman", 20, "bold"), fg="brown")
penmode_l.grid(column=0, row=2, columnspan=4)

# Create Turtle
drawer = tt.RawTurtle(canvas)
drawer.shape("circle")
drawer.speed(-1)
drawer.ondrag(draw)

window.mainloop()
