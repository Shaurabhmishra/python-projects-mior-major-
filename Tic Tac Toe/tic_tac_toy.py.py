from tkinter import *
from random import randint
from tkinter import messagebox

ActivePlayer = 1
p1 = []
p2 = []

root = Tk()
root.title('Tic Tac Toe : Player 1')
'''
style = style()
style.theme_use('classic')
'''
button1 = Button(root, text="", activebackgroun="yellow", width=10, height=5, relief="sunken")
button1.grid(row=0, column=0, ipadx=10, ipady=10)
button1.config(command=lambda: BUttonClick(1))

button2 = Button(root, text="", activebackgroun="yellow", width=10, height=5, relief="sunken")
button2.grid(row=0, column=1, ipadx=10, ipady=10)
button2.config(command=lambda: BUttonClick(2))

button3 = Button(root, text="", activebackgroun="yellow", width=10, height=5, relief="sunken")
button3.grid(row=0, column=2, ipadx=10, ipady=10)
button3.config(command=lambda: BUttonClick(3))

button4 = Button(root, text="", activebackgroun="yellow", width=10, height=5, relief="sunken")
button4.grid(row=1, column=0, ipadx=10, ipady=10)
button4.config(command=lambda: BUttonClick(4))

button5 = Button(root, text="", activebackgroun="yellow", width=10, height=5, relief="sunken")
button5.grid(row=1, column=1, ipadx=10, ipady=10)
button5.config(command=lambda: BUttonClick(5))

button6 = Button(root, text="", activebackgroun="yellow", width=10, height=5, relief="sunken")
button6.grid(row=1, column=2, ipadx=10, ipady=10)
button6.config(command=lambda: BUttonClick(6))

button7 = Button(root, text="", activebackgroun="yellow", width=10, height=5, relief="sunken")
button7.grid(row=2, column=0, ipadx=10, ipady=10)
button7.config(command=lambda: BUttonClick(7))

button8 = Button(root, text="", activebackgroun="yellow", width=10, height=5, relief="sunken")
button8.grid(row=2, column=1, ipadx=10, ipady=10)
button8.config(command=lambda: BUttonClick(8))

button9 = Button(root, text="", activebackgroun="yellow", width=10, height=5, relief="sunken")
button9.grid(row=2, column=2, ipadx=10, ipady=10)
button9.config(command=lambda: BUttonClick(9))


def BUttonClick(id):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id, "X")
        p1.append(id)
        root.title("Tic Tac Toe : Player 2")
        ActivePlayer = 2
        print("P1 : {}".format(id))
        Autoplay()
    elif(ActivePlayer==2):
        SetLayout(id, "O")
        p2.append(id)
        root.title("Tic Tac Toe : Player 1")
        ActivePlayer = 1
        print("P2 : {}".format(id))

    CheckWinner()

def SetLayout(id,input):
    if(id==1):
        button1.config(text=input, state=DISABLED)

    elif(id==2):
        button2.config(text=input, state=DISABLED)

    elif (id==3):
        button3.config(text=input, state=DISABLED)

    elif(id==4):
        button4.config(text=input, state=DISABLED)

    elif(id==5):
        button5.config(text=input, state=DISABLED)

    elif(id==6):
        button6.config(text=input, state=DISABLED)

    elif(id==7):
        button7.config(text=input, state=DISABLED)

    elif(id==8):
        button8.config(text=input, state=DISABLED)

    elif(id==9):
        button9.config(text=input, state=DISABLED)


def CheckWinner():
    Winner=-1
    if( (1 in p1) and (2 in p1) and (3 in p1)):
        Winner=1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        Winner = 2

    if ((4 in p1) and (5 in p1) and (6 in p1)):
        Winner = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        Winner = 2

    if ((7 in p1) and (8 in p1) and (9 in p1)):
        Winner = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        Winner = 2

    if ((1 in p1) and (4 in p1) and (7 in p1)):
        Winner = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        Winner = 2

    if ((2 in p1) and (5 in p1) and (8 in p1)):
        Winner = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        Winner = 2

    if ((3 in p1) and (6 in p1) and (9 in p1)):
        Winner = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        Winner = 2

    if ((1 in p1) and (5 in p1) and (9 in p1)):
        Winner = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        Winner = 2

    if ((3 in p1) and (5 in p1) and (7 in p1)):
        Winner = 1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        Winner = 2

    if(Winner==1):
        messagebox.showinfo(title="Congrats.", message="Player 1 is the Winner")
    elif(Winner==2):
        messagebox.showinfo(title="Congrats.", message="Player 2 is the Winner")


def Autoplay():
        global p1
        global p2
        EmptyCells = []
        for cell in range(9):
            if(not( (cell+1 in p1) or (cell+1 in p2))):
                EmptyCells.append(cell+1)

        RandIndex = randint(0, len(EmptyCells)-1)
        BUttonClick(EmptyCells[RandIndex])

root.mainloop()
