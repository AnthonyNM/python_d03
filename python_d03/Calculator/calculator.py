#!/usr/bin/env python3


# Copyright (c) 2020 Anthony Cazes

# This source code is licensed under the MIT license found in the
# License_calculator file in the root directory of this source tree.


from tkinter import *
import math

window = Tk()
window.title("Calculator")

calc_input = ""

def input_key(value):
    
    # Cette fonction permet de récupérer l'input et de l'afficher sur la calculette 

    global calc_input
    calc_input += value
    calc_input_text.set(calc_input)
    print(calc_input)

def equal():
   
    # Cette fonction permet une fois la key("=") de press, de call la bonne fonction qui va return un résultat que l'on va pouvoir afficher sur la calculatrice

    global calc_input

    if "+" in calc_input:
        result = add()
    
    elif "*" in calc_input:
        result = mult()

    elif "/" in calc_input:
        result = div()

    elif "tan" in calc_input:
        result = tan()

    elif "cos" in calc_input:
        result = cos()

    elif "sin" in calc_input:
        result = sin()

    elif "exp" in calc_input:
        result = exp()

    elif "-" in calc_input:
        result = sub()

    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set(result)
    print(result)

def exp():

    # Cette fonction permet de return l'exponentielle d'un nombre
    
    global calc_input
    exponentielle = calc_input.split("exp")
    result = math.exp(int(exponentielle[1]))
    return result

def cos():

    # Cette fonction permet de return le cosinus d'un nombre

    global calc_input
    cosinus = calc_input.split("cos")
    result = math.cos(int(cosinus[1]))
    return result

def sin():

    # Cette fonction permet de return le sinus d'un nombre

    global calc_input
    sinus = calc_input.split("sin")
    result = math.sin(int(sinus[1]))
    return result

def tan():

    # Cette fonction permet de return la tangente d'un nombre

    global calc_input
    tangente = calc_input.split("tan")
    result = math.tan(int(tangente[1]))
    return result

def add():

    # Cette fonction permet de faire une addition avec plusieurs nombres ( positifs ou négatifs ) et de return son résultat

    global calc_input
    result = 0
    additions = calc_input.split("+")
    for value in additions:
            result += int(value)
    return result

def sub():

    # Cette fonction permet de faire une soustraction avec plusieurs nombres ( positifs ou négatifs ) et de return son résultat

    global calc_input
    soustraction = calc_input.split("-")
    if soustraction[0] == "":
        soustraction.pop(0)
        result = 0
    else:
        result = int(soustraction[0]) * 2
    for index, value in enumerate(soustraction):
        if value == "":
            soustraction.pop(index)
            soustraction[index] = "-" + soustraction[index]
    for value in soustraction:
        result = result - int(value)
    return result

def mult():

    # Cette fonction permet de faire une multiplication avec plusieurs nombres ( positifs ou négatifs ) et de return son résultat

    global calc_input
    result = 1
    multiplication = calc_input.split("*")
    for value in multiplication:
        result = result * int(value)
    return result

def div():

    # Cette fonction permet de faire une division avec plusieurs nombres ( positifs ou négatifs ) et de return son résultat

    global calc_input
    division = calc_input.split("/")
    result = int(division[0]) * int(division[0])
    for value in division:
        result = result / int(value)
    return result

def clear():

    # Cette fonction permet d'enlever les values dans calc_input 

    global calc_input
    calc_input = ""
    calc_input_text.set(calc_input)


# ---------------------------------------------------------------------------Affichage Calculette-----------------------------------------------------------------------------------------------


Button(window, text="Fermer", command=window.quit).grid(row=0, column=4)
Button(window, text=" 0 ", padx = 40, pady = 20, command=lambda: input_key("0")).grid(row=6, column=0)
Button(window, text=" 1 ", padx = 40, pady = 20, command=lambda: input_key("1")).grid(row=5, column=0)
Button(window, text=" 2 ", padx = 40, pady = 20, command=lambda: input_key("2")).grid(row=5, column=1)
Button(window, text=" 3 ", padx = 40, pady = 20, command=lambda: input_key("3")).grid(row=5, column=2)
Button(window, text=" 4 ", padx = 40, pady = 20, command=lambda: input_key("4")).grid(row=4, column=0)
Button(window, text=" 5 ", padx = 40, pady = 20, command=lambda: input_key("5")).grid(row=4, column=1)
Button(window, text=" 6 ", padx = 40, pady = 20, command=lambda: input_key("6")).grid(row=4, column=2)
Button(window, text=" 7 ", padx = 40, pady = 20, command=lambda: input_key("7")).grid(row=3, column=0)
Button(window, text=" 8 ", padx = 40, pady = 20, command=lambda: input_key("8")).grid(row=3, column=1)
Button(window, text=" 9 ", padx = 40, pady = 20, command=lambda: input_key("9")).grid(row=3, column=2)
Button(window, text=" ÷ ", padx = 38, pady = 20, command=lambda: input_key("/")).grid(row=6, column=1)
Button(window, text=" × ", padx = 40, pady = 20, command=lambda: input_key("*")).grid(row=3, column=4)
Button(window, text=" + ", padx = 40, pady = 20, command=lambda: input_key("+")).grid(row=4, column=4)
Button(window, text=" - ", padx = 41, pady = 20, command=lambda: input_key("-")).grid(row=6, column=2)
Button(window, text=" tan ", padx = 40, pady = 20, command=lambda: input_key("tan")).grid(row=3, column=3)
Button(window, text=" cos ", padx = 40, pady = 20, command=lambda: input_key("cos")).grid(row=4, column=3)
Button(window, text=" sin ", padx = 41, pady = 20, command=lambda: input_key("sin")).grid(row=5, column=3)
Button(window, text=" exp ", padx = 38, pady = 20, command=lambda: input_key("exp")).grid(row=6, column=3)
Button(window, text=" = ", padx = 40, pady = 20, command=lambda: equal()).grid(row=5, column=4)
Button(window, text=" AC ", padx = 37, pady = 20, command=lambda: clear()).grid(row=2, column=4)

calc_input_text = StringVar()
Label(window, textvariable=calc_input_text).grid(row = 0, column = 0)
result_text = StringVar()
Label(window, textvariable=result_text).grid(row=1, column=2)

window.mainloop()
