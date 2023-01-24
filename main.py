from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
# import csv
# from random import choice, randint, shuffle
# import pyperclip
import time
COLUMN = 0
COLUMN2 = 3
COLOR_WIDGET = ""

root = Tk()
root.geometry("800x480")
root.title("WELCOME TO BARISTAS !")

w1 = Label(text="WELCOME TO BARISTAS ! 😻 ", bg="white", fg="black", font=("Arial", 15, "bold"))
w1.grid(row=1, column=COLUMN)

def play():
    global img
    img = Image.open("mybc.gif")

    lbl = Label(root)
    lbl.grid(row=1, column=1)

    for img in ImageSequence.Iterator(img):
        img = img.resize((450, 350))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        time.sleep(0.09)
        root.update()
    root.after(0, play)

def exit():
    root.destroy()

Button(root, text="Play", command=play).grid(row=2, column=3)
Button(root, text="GO TO APP", command=exit).grid(row=3, column=3)
root.mainloop()
#
#
def save():
    a1 = q1_entry.get()
    a2 = q2_entry.get()
    a3 = q3_entry.get()
#     # a4 = q4_entry.get()
#     # a5 = q5_entry.get()
#     # a6 = q6_entry.get()
#     # a7 = q7_entry.get()
#     # a8 = q8_entry.get()
#     # a9 = q9_entry.get()
    # a10 = q10_entry.get()
    # a11 = q11_entry.get()
    # a12 = q12_entry.get()
    # a13 = q13_entry.get()
    # a14 = q14_entry.get()
    # a15 = q15_entry.get()
    # a16 = q16_entry.get()
    # a17 = q17_entry.get()
    # a18 = q18_entry.get()
    # a19 = q19_entry.get()
    # a20 = q20_entry.get()
    # a21 = q21_entry.get()
    # a22 = q22_entry.get()
    # a23 = q23_entry.get()
    #
    if len(a1) == 0 or len(a2) == 0 or len(a3) == 0 :

        is_empty = messagebox.showinfo(title="Oops! Empty Fields", message="Please fill up all the details")

    else:
        is_ok = messagebox.askokcancel(title="ORDER SUMMARY",message=f"Are you sure you wanna submit ?\n Your Order is {a3}")

        SUM = messagebox.showinfo(title ="ORDER", message = "Thank You for your order ! Your coffee will arive in 10 minutes 😻")
        with open("data.txt", "a") as data_file:
            data_file.write("\n_________________\n")
            data_file.write(f"NAME: {a1}\n PHONE: {a2}\n CHOICE: {a3}\n ")
            data_file.write(time.ctime())
            data_file.write("\n_________________")
            q1_entry.delete(0, END)
            q2_entry.delete(0, END)
            q3_entry.delete(0, END)
            # q4_entry.delete(0, END)
            # q5_entry.delete(0, END)
            # q6_entry.delete(0, END)
            # q7_entry.delete(0, END)
            # q8_entry.delete(0, END)
            # q9_entry.delete(0, END)
            # q10_entry.delete(0, END)
            # q11_entry.delete(0, END)
            # q12_entry.delete(0, END)
            # q13_entry.delete(0, END)
            # q14_entry.delete(0, END)
            # q15_entry.delete(0, END)
            # q16_entry.delete(0, END)
            # q17_entry.delete(0, END)
            # q18_entry.delete(0, END)
            # q19_entry.delete(0, END)
            # q20_entry.delete(0, END)
            # q21_entry.delete(0, END)
            # q22_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("COFFEE SHOP")
window.config(padx=10, pady=10, bg="white")

canvas = Canvas(height=450, width=450, bg="white", highlightthickness=0)
meena_image = PhotoImage(file="a.png")
canvas.create_image(150, 160, image=meena_image)
canvas.create_text(175, 380, text="ENJOY BARISTAS AND MORE !", fill="RED4", font=("Arial", 23, "bold"))

canvas.grid(row=0, column=1)
# _________________________________________________

# _________________________________________________
q1 = Label(text="NAME: ", bg="white", fg="black")
q1.grid(row=1, column=COLUMN)

q2 = Label(text="MOBILE NUMBER: ", bg="white", fg="black")
q2.grid(row=2, column=COLUMN)

q3 = Label(text="MOCHA: Rs. 150 | DARK: Rs. 99 | CAPPUCCINO: Rs. 199", bg="white", fg="black")
q3.grid(row=3, column=COLUMN + 1)

q4 = Label(text="ENTER YOUR CHOICE: ", bg="white", fg="black")
q4.grid(row=4, column=COLUMN)


q1_entry = Entry(width=40, bg="white", fg="black")
q1_entry.grid(row=1, column=1)

q2_entry = Entry(width=40, bg="white", fg="black")
q2_entry.grid(row=2, column=1)

q3_entry = Entry(width=40, bg="white", fg="black")
q3_entry.grid(row=4, column=1)


add_button = Button(text="🐹 SUBMIT 🐹", bg="black",width=32, command=save)
add_button.grid(row=6, column=2)
# __________________________________________


#
# q10 = Label(text="Greek God 😏", bg="pink", fg="black")
# q10.grid(row=10, column=COLUMN)
# #___________________________________________________
# q11 = Label(text="Medium Hair", bg="pink", fg="black")
# q11.grid(row=11, column=COLUMN)
#
# q12 = Label(text="Wavy curled", bg="pink", fg="black")
# q12.grid(row=1, column=COLUMN2)
#
# q13 = Label(text="Glasses (emotional damage🥲 -creator of this program)", bg="pink", fg="black")
# q13.grid(row=2, column=COLUMN2)
#
# q14 = Label(text="Indian/American", bg="pink", fg="black")
# q14.grid(row=3, column=COLUMN2)
#
# q15 = Label(text="Protective and Yandere", bg="pink", fg="black")
# q15.grid(row=4, column=COLUMN2)
#
# #___________________________________________________
#
# q16 = Label(text="Expressive Guy 🥹", bg="pink", fg="black")
# q16.grid(row=5, column=COLUMN2)
#
# q17 = Label(text="Story Teller", bg="pink", fg="black")
# q17.grid(row=6, column=COLUMN2)
#
# q18 = Label(text="Into Aesthetics/Can Cook", bg="pink", fg="black")
# q18.grid(row=7, column=COLUMN2)
#
# q19 = Label(text="Know it all but doesn't show off 😎", bg="pink", fg="black")
# q19.grid(row=8, column=COLUMN2)
#
# q20 = Label(text="innocent with Pure ❤️", bg="pink", fg="black")
# q20.grid(row=9, column=COLUMN2)
#
# #___________________________________________________
# q21 = Label(text="Wants only Meenakshi (Duuhhh 😤😤😤 !!!)", bg="pink", fg="black")
# q21.grid(row=10, column=COLUMN2)
#
# q22 = Label(text="Loyal 😻", bg="pink", fg="black")
# q22.grid(row=11, column=COLUMN2)
#
# q23 =Label(text="N A M E", bg="pink", fg="BLACK")
# q23.grid(row=12, column=COLUMN2)
# # _________________________________________________
# # _________________________________________________
# # _________________________________________________
# # _________________________________________________
#

#
# q4_entry = Entry(width=10, bg="red1", fg="white")
# q4_entry.grid(row=4, column=1)
#
# q5_entry = Entry(width=10, bg="yellow2")
# q5_entry.grid(row=5, column=1)
#
# #___________________________________________________
# q6_entry = Entry(width=10, bg="yellow3")
# q6_entry.grid(row=6, column=1)
#
# q7_entry = Entry(width=10, bg="yellow4")
# q7_entry.grid(row=7, column=1)
#
# q8_entry = Entry(width=10, bg="green4", fg="white")
# q8_entry.grid(row=8, column=1)
#
# q9_entry = Entry(width=10, bg="green3", fg="white")
# q9_entry.grid(row=9, column=1)
#
# q10_entry = Entry(width=10, bg="green2")
# q10_entry.grid(row=10, column=1)
#
# #___________________________________________________
# q11_entry = Entry(width=10, bg="green1")
# q11_entry.grid(row=11, column=1)
#
# q12_entry = Entry(width=10, bg="blue", fg="white")
# q12_entry.grid(row=1, column=4)
# #
# q13_entry = Entry(width=10, bg="blue2", fg="white")
# q13_entry.grid(row=2, column=4)
#
# q14_entry = Entry(width=10, bg="blue3", fg="white")
# q14_entry.grid(row=3, column=4)
#
# q15_entry = Entry(width=10, bg="purple4", fg="white")
# q15_entry.grid(row=4, column=4)
#
# #___________________________________________________
# q16_entry = Entry(width=10, bg="purple3", fg="white")
# q16_entry.grid(row=5, column=4)
#
# q17_entry = Entry(width=10, bg="purple2", fg="white")
# q17_entry.grid(row=6, column=4)
#
# q18_entry = Entry(width=10, bg="purple1", fg="white")
# q18_entry.grid(row=7, column=4)
#
# q19_entry = Entry(width=10, bg="black", fg="white")
# q19_entry.grid(row=8, column=4)
#
# #___________________________________________________
# q20_entry = Entry(width=10, bg="grey")
# q20_entry.grid(row=9, column=4)
#
# q21_entry = Entry(width=10, bg="white")
# q21_entry.grid(row=10, column=4)
#
# q22_entry = Entry(width=10, bg="red4", fg="white")
# q22_entry.grid(row=11, column=4)
#
#
# q23_entry = Entry(width=10, bg="red4", fg="white")
# q23_entry.grid(row=12, column=4)
# #___________________________________________________
# # __________________________________________________

window.mainloop()