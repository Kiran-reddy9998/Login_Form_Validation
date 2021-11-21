from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("LOGIN PAGE")
top.geometry("400x300")
top.configure(bg="powder blue")


def sign_in():
    user = e1.get()
    password = e2.get()
    if user == "12345" and password == "Kirru":
        messagebox.showinfo("Message", "Logged in successfully")
    else:
        messagebox.showerror("Invalid", "please enter valid username and password")


# ---------------------------------creating label-----------------------------------------------------------

l1 = Label(top, text="USER ID :", bg="powder blue", fg="black", font="Times 12 bold")
l1.place(x=50, y=90)
l2 = Label(top, text="PASSWORD :", bg="powder blue", fg="black", font="Times 12 bold")
l2.place(x=35, y=130)

# --------------------------------creating entry boxes------------------------------------------------------

e1 = Entry(top, bg="white", fg="blue", width="34")
e1.place(x=150, y=90)
e2 = Entry(top, bg="white", fg="blue", width="34")
e2.place(x=150, y=130)

# ---------------------------------creating button-----------------------------------------------------------

b1 = Button(top, text="SIGN IN", fg="black", bg="green", width="20", height="2",
            font="Times 10 bold", command=sign_in)
b1.place(x=145, y=182)
top.mainloop()

