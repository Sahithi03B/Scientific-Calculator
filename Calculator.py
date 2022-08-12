from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log

window = Tk()
screenSize = "279x442"
window.geometry(screenSize)
window.resizable(0, 0)
window.title("Calcualtor")
#function
def about():
    messagebox.showinfo('About',"\n \n \n   Made by Sahithi \n \n INSTAGRAM : @ssahithi03 \n \n Github : Sahithi03B \n \n")

def clickButton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def clearButton():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def expand():
    if screenSize=="279x500":
        window.geometry("279x555")
    else:
        window.geometry("279x555")
def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)
#menubar
menubar = Menu(window,bg="black",fg="white")
filemenu = Menu(menubar, tearoff=0,bg="black",fg="white")
filemenu.add_command(label="Copy")
filemenu.add_command(label="Paste")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0,bg="black",fg="white")
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

expression = ""
inputText = StringVar()

inputFrame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="gray",
                    highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 25, ), textvariable=inputText, width=50,fg="white", bg="black", bd=0,
                    justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=13)

mainFrame = Frame(window, width=312, height=272.5, bg="black")
mainFrame.pack()

ac = PhotoImage(file = r"images\ac.png")
acimage = ac.subsample(4,4)
ac = Button(mainFrame, text="AC", fg="black", image=acimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clearAll()).grid(row=0, column=0, padx=1, pady=1)

clear = PhotoImage(file = r"images\clear.png")
clearimage = clear.subsample(4,4)
clear = Button(mainFrame, text="AC", fg="black", image=clearimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clearButton()).grid(row=0, column=1, padx=1, pady=1)

expan_btn = PhotoImage(file = r"images\expan_btn.png")
expan_btnimage = expan_btn.subsample(4,4)
percentage = Button(mainFrame, fg="black", image=expan_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: expand()).grid(row=0, column=2, padx=1, pady=1)

divide = PhotoImage(file = r"images\divide.png")
divideimage = divide.subsample(4,4)
divide = Button(mainFrame, text="/", fg="white",image=divideimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("/")).grid(row=0, column=3, padx=1, pady=1)


seven = PhotoImage(file = r"images\seven.png")
sevenimage = seven.subsample(4,4)
seven = Button(mainFrame, text="7", fg="black", image=sevenimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(7)).grid(row=1, column=0, padx=1, pady=1)

eight = PhotoImage(file = r"images\eight.png")
eightimage = eight.subsample(4,4)
eight = Button(mainFrame, text="8", fg="black", image=eightimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(8)).grid(row=1, column=1, padx=1, pady=1)

nine = PhotoImage(file = r"images\nine.png")
nineimage = nine.subsample(4,4)
nine = Button(mainFrame, text="9", fg="black", image=nineimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(9)).grid(row=1, column=2, padx=1, pady=1)

multi = PhotoImage(file = r"images\multi.png")
multiimage = multi.subsample(4,4)
multiply = Button(mainFrame, text="*", fg="white",image=multiimage, bd=0, bg="black", cursor="hand2",
                  command=lambda: clickButton("*")).grid(row=1, column=3, padx=1, pady=1)

four = PhotoImage(file = r"imag