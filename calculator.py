import tkinter as tk 
from tkinter import *
def button_press(num):

    global equation_txt
    

    equation_txt = equation_txt + str(num)

    equation_label.set(equation_txt)

def equals():
    try:

        global  equation_txt

        total = str(eval(equation_txt))

        equation_label.set(total)

        equation_txt = total
    except SyntaxError:
        equation_label.set("SyntexError")

    except ZeroDivisionError:
            equation_label.set("arithmetic error")

            equation_txt = ""

def clear():
    global equation_txt

    equation_label.set("")

    equation_txt = ""


window = tk.Tk()

window.title("Calculator Program")
window.geometry("500x500")
equation_txt = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=('cnsolas',20), bg="white", width=24, height=2)
img=PhotoImage(file="\icons\cacu.cacu")
window.iconphoto(False,img)
label.pack()






fram = Frame(window)

fram.pack()

button1 = Button(fram, text=1, height=4, width=9, font=36,
                 command=lambda: button_press('1'))
button1.grid(row=0,column=0)


button2 = Button(fram, text=2, height=4, width=9, font=35,
                command=lambda: button_press(2))

button2.grid(row=0,column=1)


button3 = Button(fram, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(fram, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(fram, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(fram, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(fram, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(fram, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(fram, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(fram, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3,column=0)

plus = Button(fram, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0,column=3)

minus = Button(fram, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1,column=3)

multiply = Button(fram, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2,column=3)

divide = Button(fram, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3,column=3)

equal = Button(fram, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3,column=2)

decimal = Button(fram, text='.', height=4, width=9, font=35,
                 command=lambda: button_press ('.'))
decimal.grid(row=3,column=1)

clear = Button(window, text='clear', height=2, width=12, font=35,
                 command=clear)
clear.pack()


window.mainloop()



