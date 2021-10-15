from tkinter import *
from tkinter.ttk import Combobox
import turtle as tt

MODE = "write"


# Functions
def draw(x, y):
    drawer.ondrag(None)
    drawer.setheading(drawer.towards(x, y))
    if MODE == "write":
        drawer.pencolor(color.get())
    elif MODE == "erase":
        drawer.pencolor("white")
    drawer.width(thickness.get() + 2)
    drawer.goto(x, y)
    drawer.ondrag(draw)


def change_mode():
    global MODE
    if MODE == "write":
        MODE = "erase"
        erase_b.configure(bg="black", fg="white")
    elif MODE == "erase":
        MODE = "write"
        erase_b.configure(bg="#0edee6", fg="black")


# Create GUI
window = Tk()
window.title("Drawing App")
window.config(padx=25, pady=50)
window.iconbitmap("favicon.ico")

color = StringVar()
color_cbox = Combobox(window, width=10, textvariable=color)
color_cbox["values"] = ("Red",
                        "Green",
                        "Blue",
                        "Yellow",
                        "Orange",
                        "Pink",
                        "Black")
color_cbox.grid(column=0, row=0, padx=(0, 25))
color_cbox.current(0)

thickness = IntVar()
thickness_cbox = Combobox(window, width=5, textvariable=thickness)
thickness_cbox["values"] = (1, 2, 3, 4, 5)
thickness_cbox.grid(column=1, row=0)
thickness_cbox.current(0)

erase_b = Button(window, text="Erase", bg="#0edee6", command=change_mode)
erase_b.grid(column=2, row=0, padx=25)

clear_b = Button(window, text="Clear", bg="#09ff00", command=lambda: drawer.clear())
clear_b.grid(column=3, row=0)

canvas = Canvas(window, width=600, height=600)
canvas.grid(column=0, row=1, columnspan=4, pady=(25, 0))

penup_b = Button(window, text="Pen Up", bg="#ffbc03", width=10, command=lambda: drawer.penup())
penup_b.grid(column=0, row=2, pady=(25, 0))

pendown_b = Button(window, text="Pen Down", bg="#ffbc03", width=10, command=lambda: drawer.pendown())
pendown_b.grid(column=3, row=2, pady=(25, 0))

# Create Turtle
drawer = tt.RawTurtle(canvas)
drawer.shape("circle")
drawer.speed(-1)
drawer.ondrag(draw)

window.mainloop()
