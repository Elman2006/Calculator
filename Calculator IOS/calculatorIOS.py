from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Calculator")
win.geometry("260x340")
win.resizable(False, False)
win.config(bg="black")
operator = ""
text_input = StringVar()
# ======================================================== FUNCTIONS ================================================
# --------------------------------- MENU FUNCTIONS -------------------------------------


def exit():
    win.destroy()


def save():
    pass


def save_as():
    pass


def export():
    pass


def import_():
    pass


def info():
    messagebox.showinfo("Auther", "Developed by Elman")


def cut():
    pass


def paste():
    pass


# --------------------------------- COMMAND FUNCTIONS ---------------------------------
def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btn_clear_display():
    global operator
    operator = ""
    text_input.set("")


def btn_equals_input():
    global operator
    sum_up = str(eval(operator))
    text_input.set(sum_up)
    operator = ""


# ------------------------------------- MENU ---------------------------------------------
menubar = Menu(win)
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="SaveAs", command=save_as)
file_menu.add_command(label="Export", command=export)
file_menu.add_command(label="Import", command=import_)
Editmenu = Menu(win, tearoff=0)
menubar.add_cascade(label="Edit", menu=Editmenu)
Editmenu.add_command(label="Cut", command=cut)
Editmenu.add_command(label="Paste", command=paste)
menubar.add_command(label="Info", command=info)
menubar.add_command(label="Exit", command=exit)
win.config(menu=menubar)


# ------------------------------------------ DISPLAY--------------------------------------------------
txtDisplay = Entry(win,
                   font=('arial', 20, 'bold'),
                   textvariable=text_input,
                   insertwidth=4,
                   bg='black',
                   fg='white',
                   justify='left',
                   width=17,
                   bd=0).grid(columnspan=4)

# ------------------------------------------ BUTTONS ------------------------------------------
# ------------------------------------------ FIRST ROW ------------------------------------------
photo_0 = PhotoImage(file="BUTTONS/iOS-button0.png")
button_0 = Button(win, image=photo_0, bd=0, bg='black', command=lambda: btn_click(0))
button_0.place(x=1, y=280)
photo_DOT = PhotoImage(file="BUTTONS/iOS-buttonDOT.png")
button_DOT = Button(win, image=photo_DOT, bd=0, bg='black', command=lambda: btn_click('.'))
button_DOT.place(x=135, y=280)
photo_IS = PhotoImage(file="BUTTONS/iOS-buttonIS.png")
button_IS = Button(win, image=photo_IS, bd=0, bg='black', command=btn_equals_input)
button_IS.place(x=200, y=280)
# ------------------------------------------ 2TH ROW ------------------------------------------
photo_1 = PhotoImage(file="BUTTONS/iOS-button1.png")
button_1 = Button(win, image=photo_1, bd=0, bg='black', command=lambda: btn_click(1))
button_1.place(x=5, y=220)
photo_2 = PhotoImage(file="BUTTONS/iOS-button2.png")
button_2 = Button(win, image=photo_2, bd=0, bg='black', command=lambda: btn_click(2))
button_2.place(x=71, y=220)
photo_3 = PhotoImage(file="BUTTONS/iOS-button3.png")
button_3 = Button(win, image=photo_3, bd=0, bg='black', command=lambda: btn_click(3))
button_3.place(x=135, y=220)
photo_SUM = PhotoImage(file="BUTTONS/iOS-buttonSUM.png")
button_SUM = Button(win, image=photo_SUM, bd=0, bg='black', command=lambda: btn_click(' + '))
button_SUM.place(x=198, y=220)
# ------------------------------------------ 3TH ROW ------------------------------------------
photo_4 = PhotoImage(file="BUTTONS/iOS-button4.png")
button_4 = Button(win, image=photo_4, bd=0, bg='black', command=lambda: btn_click(4))
button_4.place(x=3, y=160)
photo_5 = PhotoImage(file="BUTTONS/iOS-button5.png")
button_5 = Button(win, image=photo_5, bd=0, bg='black', command=lambda: btn_click(5))
button_5.place(x=68, y=160)
photo_6 = PhotoImage(file="BUTTONS/iOS-button6.png")
button_6 = Button(win, image=photo_6, bd=0, bg='black', command=lambda: btn_click(6))
button_6.place(x=135, y=160)
photo_NEG = PhotoImage(file="BUTTONS/iOS-buttonNEG.png")
button_NEG = Button(win, image=photo_NEG, bd=0, bg='black', command=lambda: btn_click(' - '))
button_NEG.place(x=199, y=160)
# ------------------------------------------ 4TH ROW ------------------------------------------
photo_7 = PhotoImage(file="BUTTONS/iOS-button7.png")
button_7 = Button(win, image=photo_7, bd=0, bg='black', command=lambda: btn_click(7))
button_7.place(x=5, y=100)
photo_8 = PhotoImage(file="BUTTONS/iOS-button8.png")
button_8 = Button(win, image=photo_8, bd=0, bg='black', command=lambda: btn_click(8))
button_8.place(x=70, y=100)
photo_9 = PhotoImage(file="BUTTONS/iOS-button9.png")
button_9 = Button(win, image=photo_9, bd=0, bg='black', command=lambda: btn_click(9))
button_9.place(x=132, y=100)
photo_MULT = PhotoImage(file="BUTTONS/iOS-buttonMULT.png")
button_MULT = Button(win, image=photo_MULT, bd=0, bg='black', command=lambda: btn_click(' * '))
button_MULT.place(x=200, y=100)
# ------------------------------------------ 5TH ROW ------------------------------------------
photo_AC = PhotoImage(file="BUTTONS/iOS-buttonAC.png")
button_Ac = Button(win, image=photo_AC, bd=0, bg='black', command=btn_clear_display)
button_Ac.place(x=5, y=40)
photo_NEGSUM = PhotoImage(file="BUTTONS/iOS-buttonNEGSUM.png")
button_NEGSUM = Button(win, image=photo_NEGSUM, bd=0, bg='black')
button_NEGSUM.place(x=66, y=37)
photo_100 = PhotoImage(file="BUTTONS/iOS-button100.png")
button_100 = Button(win, image=photo_100, bd=0, bg='black')
button_100.place(x=137, y=40)
photo_DIVE = PhotoImage(file="BUTTONS/iOS-buttonDIVE.png")
button_DIVE = Button(win, image=photo_DIVE, bd=0, bg='black', command=lambda: btn_click(' / '))
button_DIVE.place(x=200, y=40)
# ------------------------------------------ MAIN LOOP ------------------------------------------
win.mainloop()
