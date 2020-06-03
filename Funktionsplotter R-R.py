import Tkinter as T
import matplotlib.pyplot as plt
import math
import numpy as np

pi = math.pi
e = math.e

def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)

def asin(x):
    return math.asin(x)
def acos(x):
    return math.acos(x)
def atan(x):
    return math.atan(x)

def factorial(x):
    return math.factorial(x)

def log(x, base):
    return math.log(x, base)




def execute():

    if resolution.get() == "":
        res = 100
    else:
        res = float(resolution.get())

    if border_x_left.get() == "":
        b_left = -10
    else:
        b_left = float(border_x_left.get())

    if border_x_right.get() == "":
        b_right = 10
    else:
        b_right = float(border_x_right.get())

    X = np.arange(b_left, b_right, 1.0/res)
    Y = map(equation, X)

    plt.scatter(X,Y, s = 0.1)
    plt.show()



def equation(x):
    if limit.get() == "":
        lim = 10**24


        if eval(function.get()) > lim:
            return 0
        elif eval(function.get()) < -lim:
            return 0
        else:
            return eval(function.get())

    else:
        if eval(function.get()) > float(limit.get()):
            return 0
        elif eval(function.get()) < -float(limit.get()):
            return 0
        else:
            return eval(function.get())


def clear():
    plt.close()

menu = T.Tk()
menu.title("Funktionsplotter R->R")

introduction = T.Label(menu, text = "Hinweise: 1. Wird das eingestellte Limit erreicht, werden die Werte auf der X-Achse geplottet.\n2. Die Funktion muss in Python-Schreibweise geschrieben sein damit das Programm vernuenftig funktioniert.\n3. Die Standartwerte betragen: resolution = 100, border_left = -10, border_right = 10, limit = 10^24")
introduction.pack()

L_function = T.Label(menu, text = "f(x) =")
function = T.Entry(menu)
L_function.pack()
function.pack()

L_resolution = T.Label(menu, text = "Schritte pro X (Aufloesung)")
resolution = T.Entry(menu)
L_resolution.pack()
resolution.pack()

L_border_x_left = T.Label(menu, text = "von x =")
border_x_left = T.Entry(menu)
L_border_x_left.pack()
border_x_left.pack()

L_border_x_right = T.Label(menu, text = "bis x =")
border_x_right = T.Entry(menu)
L_border_x_right.pack()
border_x_right.pack()

L_limit = T.Label(menu, text = "Grenze von Y:")
limit = T.Entry(menu)
L_limit.pack()
limit.pack()

clear = T.Button(menu, text = "clear", command = clear)
clear.pack()

plot = T.Button(menu, text = "plot", command = execute)
plot.pack()


menu.mainloop()