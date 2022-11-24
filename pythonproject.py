import tkinter as tk

window = tk.Tk()
window.geometry("550x800")

window.configure(background="powder blue")
window.wm_title("Number System")
Base_Number = ""
background_image = tk.PhotoImage(file="binry to hexa.png",)
background_label1 = tk.Label(window, image=background_image)
background_label1.place(x=0, y=0)
# ===============================Function to calculate =======================================#
def evaluate(event):
    if Base_Number == "Binary":  # For Binary to another
        try:
            dec = int(Myentry.get(), 2)
            mybin = bin(dec).lstrip("0b")
            mydec = str(dec)
            myhex = hex(dec).lstrip("0x")
            myoct = oct(dec).lstrip("0o")
            out1.insert(0.0, mybin)
            out2.insert(0.0, mydec)
            out3.insert(0.0, myoct)
            out4.insert(0.0, myhex)

        except ValueError:
            result1.configure(text="enter valid Binary", font="arial 16 bold")
    elif Base_Number == "Decimal":  # For decimal to another
        try:
            dec = int(Myentry.get(), 10)
            mybin = bin(dec).lstrip("0b")
            mydec = str(dec)
            myhex = hex(dec).lstrip("0x")
            myoct = oct(dec).lstrip("0o")
            out1.insert(0.0, mybin)
            out2.insert(0.0, mydec)
            out3.insert(0.0, myoct)
            out4.insert(0.0, myhex)
        except ValueError:
            result1.configure(text=" enter valid Decimal", font="arial 16 bold")

    elif Base_Number == "Hex":  # For HexaDecimal to another
        try:
            dec = int(Myentry.get(), 16)
            mybin = bin(dec).lstrip("0b")
            mydec = str(dec)
            myhex = hex(dec).lstrip("0x")
            myoct = oct(dec).lstrip("0o")
            out1.insert(0.0, mybin)
            out2.insert(0.0, mydec)
            out3.insert(0.0, myoct)
            out4.insert(0.0, myhex)
        except ValueError:
            result1.configure(text="enter valid Hexadecimal", font="arial 16 bold")
    elif Base_Number == "Octal":  # For Octal to another
        try:
            dec = int(Myentry.get(), 8)
            mybin = bin(dec).lstrip("0b")
            mydec = str(dec)
            myhex = hex(dec).lstrip("0x")
            myoct = oct(dec).lstrip("0o")
            out1.insert(0.0, mybin)
            out2.insert(0.0, mydec)
            out3.insert(0.0, myoct)
            out4.insert(0.0, myhex)
        except ValueError:
            result1.configure(text="enter valid Octal", font="arial 16 bold")
    else:
        result1.configure(text="select a BASE!", font="arial 18 bold")


# ===================================Explanation window==========================================#
def binarywin():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "A Binary number is always of base 2\n and it constists of 0 and 1.\n"
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack()


def decwin():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "A Decimal  number is always of base 10\n and it constists of 0 to 9.\n"
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack()


def octalwin():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "A Octal number is always of base 8\n and it constists of 0 to 7.\n"
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack()


def hexwin():
    # create child window
    win = tk.Toplevel()
    # display message
    message = "A hexadecimal is always of base 16\n and it constists of 0 to 9 and A to F.\n"
    tk.Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    tk.Button(win, text='OK', command=win.destroy).pack()




# ============================Function to Reset Entry Filed=====================#


def e1_delete():
    Myentry.delete(first=0, last=100)


def deltxt():
    out1.delete(1.0, tk.END)
    out2.delete(1.0, tk.END)
    out3.delete(1.0, tk.END)
    out4.delete(1.0, tk.END)




# =====================================Global Variable Declaration==========================================#

def calculate():
    global Base_Number
    Base_Number = base.get()


# ===================================================================================================#
MyTitle = tk.Label(window)
MyTitle.pack()
#==========================headline======================================================================
label1 = tk.Label(window, text="CONVERSION SYSTEM", font="arial 18 bold",width = 30, fg="white", bg="black",
                  pady=10, padx=20)
label1.place(x=30, y=2)
# ==================================Entry Field======================================================#
Myentry = tk.Entry(window, font="arial 25 bold", fg='white', bg='green',
                   justify='right', bd=12)
Myentry.bind("<Return>", evaluate)
Myentry.pack(padx=50, pady=45)
# ====================================Label========================================#
label1 = tk.Label(window, text="Enter value and press Enter", font="arial 10 bold", fg="white", bg="blue",
                  pady=10, padx=20)
label1.place(x=162, y=130)
result1 = tk.Label(window, text="Choose a Base", font="arial 18 bold", bg="blue", fg="white", pady=10, padx=20)
result1.place(x=158, y=220)
# =========================Button to choose base of the number===========================================#

base = tk.StringVar()
base.set(None)

btn1 = tk.Radiobutton(window, padx=61, pady=3, bd=8, fg = 'black', font="arial 15 bold",
                      text='Binary', variable=base, value="Binary", command=calculate).place(x=29, y=300)

btn2 = tk.Radiobutton(window, padx=32, pady=3, bd=8, fg='black', font="arial 15 bold",
                      text='Decimal', variable=base, value="Decimal", command=calculate).place(x=300, y=300)

btn3 = tk.Radiobutton(window, padx=27, pady=3, bd=8, fg='black', font="arial 15 bold",
                      text='Hexa Decimal', variable=base, value="Hex", command=calculate).place(x=30, y=350)

btn4 = tk.Radiobutton(window, padx=45, pady=3, bd=8, fg='black', font="arial 15 bold",
                      text='Octal', variable=base, value="Octal", command=calculate).place(x=300, y=350)

label2 = tk.Label(window, text="Result", font="arial 15 bold", bg="black",width = 39, fg="white", pady=10, padx=20)
label2.place(x=22, y=420)

# ==================================Output Text Box Field=========================================================================#

l1 = tk.Label(window, text="Binary", font="arial 15 bold", bg="blue", fg="white", pady=8, padx=52)
l1.place(x=8, y=473)
out1 = tk.Text(window, width=25, height=2, font="arial 15 bold", fg="black", bg="powder blue")
out1.place(x=180, y=470)
tk.Button(window, text='Explain', padx=27, pady=10, bd=8, fg='white', font="arial 8 bold", bg="blue",
          command=binarywin).place(x=435, y=470)

l2 = tk.Label(window, text="Decimal", font="arial 15 bold", bg="blue", fg="white", pady=8, padx=45)
l2.place(x=10, y=522)
out2 = tk.Text(window, width=25, height=2, font="arial 15 bold", fg="black")
out2.place(x=180, y=520)
tk.Button(window, text='Explain', padx=27, pady=10, bd=8, fg='white', font="arial 8 bold", bg="blue",
          command=decwin).place(x=435, y=520)

l3 = tk.Label(window, text="Octal", font="arial 15 bold", bg="blue", fg="white", pady=8, padx=57)
l3.place(x=10, y=574)
out3 = tk.Text(window, width=25, height=2, font="arial 15 bold", fg="black", bg="powder blue")
out3.place(x=180, y=570)
tk.Button(window, text='Explain', padx=27, pady=10, bd=8, fg='white', font="arial 8 bold", bg="blue",
          command=octalwin).place(x=435, y=570)

l4 = tk.Label(window, text="Hexa Decimal", font="arial 15 bold", bg="blue", fg="white", pady=8, padx=18)
l4.place(x=10, y=624)
out4 = tk.Text(window, width=25, height=2, font="arial 15 bold", fg="black")
out4.place(x=180, y=620)
tk.Button(window, text='Explain', padx=27, pady=10, bd=8, fg='white', font="arial 8 bold", bg="blue",
          command=hexwin).place(x=435, y=620)

# =================================Reset Button=====================================================#
tk.Button(window, text='Reset', padx=10, pady=4, bd=5, fg='white', font="arial 8 bold", bg="black",
          command=lambda: [e1_delete(), deltxt()]).place(x=240, y=176)

#=========================label -- name =========================================
label9 = tk.Label(window, text="made by - Chirag ",justify="left", font="arial 8 bold",width = 70, fg="black", bg="grey",
                  pady=0, padx=30)
label9.place(x = 1, y = 679)


window.mainloop()
# ====================================END of Program===============================#