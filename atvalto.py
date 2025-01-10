from tkinter import *
import tkinter
import time

tomeg = ["g", "dkg", "kg", "q", "t"]
tomegatvalt = [10, 100, 100, 10]

def build(nev):
    program = tkinter.Toplevel(root)
    program.title(nev)
    program.geometry("400x200")

    lbl_color = Label(program, text=f"{nev}")
    lbl_color.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    if nev == "Tömeg":
        meretkegysegek = tomeg



    ertek1 = StringVar()
    ertek1.set("Válasszon egy mértékegységet!")
    opt_ertek1 = OptionMenu(program, ertek1, *meretkegysegek)
    opt_ertek1.place(relx=0.50, rely=0.3, anchor=tkinter.CENTER)

    lbl_color = Label(program, text=f"-ból / -ből ba")
    lbl_color.place(relx=0.5, rely=0.425, anchor=tkinter.CENTER)

    ertek2 = StringVar()
    ertek2.set("Válasszon egy mértékegységet!")
    opt_ertek2 = OptionMenu(program, ertek2, *meretkegysegek)
    opt_ertek2.place(relx=0.50, rely=0.55, anchor=tkinter.CENTER)


def start():
    tipus = clicked.get()
    build(tipus)


root = Tk()
root.title("Mértékegységváltó")
root.geometry("400x200")

options = [
    "Űrtartalom",
    "Tömeg",
    "Terület",
]

clicked = StringVar()
clicked.set("Kérem válasszon egy átváltót!")
opt_program = OptionMenu(root, clicked, *options)
opt_program.place(relx=0.50, rely=0.35, anchor=tkinter.CENTER)

btn_start = Button(root, text="Inditás", command=start)
btn_start.place(relx=0.40, rely=0.55, anchor=tkinter.CENTER)
btn_start = Button(root, text="Kilépés")
btn_start.place(relx=0.60, rely=0.55, anchor=tkinter.CENTER)

root.mainloop()