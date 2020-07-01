# python|simple GUI calculator using Tkinter
from tkinter import *

window = Tk()
window.title("BASIC CALCULATOR")

entry = Entry(window, bg="#e0e0d1", width=100, borderwidth=3)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_adding():
    first_number_entered = entry.get()
    global first_number
    global math
    math = "Addition"
    first_number = int(first_number_entered)
    entry.delete(0, END)


def button_subtract():
    first_number_entered = entry.get()
    global first_number
    global math
    math = "Subtraction"
    first_number = int(first_number_entered)
    entry.delete(0, END)


def button_multiply():
    first_number_entered = entry.get()
    global first_number
    global math
    math = "Multiplication"
    first_number = int(first_number_entered)
    entry.delete(0, END)


def button_divide():
    first_number_entered = entry.get()
    global first_number
    global math
    math = "Division"
    first_number = int(first_number_entered)
    entry.delete(0, END)


def button_clicked(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_cleared():
    entry.delete(0, END)


def button_results():
    second_number_entered = entry.get()
    entry.delete(0, END)
    if math == "Addition":
        entry.insert(0, first_number + int(second_number_entered))
    if math == "Multiplication":
        entry.insert(0, first_number * int(second_number_entered))
    if math == "Division":
        entry.insert(0, first_number / int(second_number_entered))
    if math == "Subtraction":
        entry.insert(0, first_number - int(second_number_entered))


# Define Buttons
button_1 = Button(window, text="1", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(1))
button_2 = Button(window, text="2", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(2))
button_3 = Button(window, text="3", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(3))
button_4 = Button(window, text="4", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(4))
button_5 = Button(window, text="5", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(5))
button_6 = Button(window, text="6", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(6))
button_7 = Button(window, text="7", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(7))
button_8 = Button(window, text="8", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(8))
button_9 = Button(window, text="9", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(9))
button_0 = Button(window, text="0", bg="#e0e0d1", padx=80, pady=30, command=lambda: button_clicked(0))
button_add = Button(window, text="+", bg="#b7b795", padx=80, pady=30, command=button_adding)
button_equal = Button(window, text="=", bg="#a2a276", padx=125, pady=30, command=button_results)
button_clear = Button(window, text="CLEAR", bg="#b7b795",  padx=65, pady=30, command=button_cleared)
button_subtract = Button(window, text="-", bg="#b7b795", padx=80, pady=30, command=button_subtract)
button_multiply = Button(window, text="x", bg="#b7b795", padx=80, pady=30, command=button_multiply)
button_divide = Button(window, text="/", bg="#b7b795", padx=80, pady=30, command=button_divide)

# putting the buttons on the window
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row=5, column=2)

button_add.grid(row=4, column=0)
button_equal.grid(row=6, column=1)

button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)

window.mainloop()
