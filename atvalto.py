from tkinter import *
import tkinter
import time

muvelet = True

terulet = ["mm2", "cm2", "dm2", "m2", "ha", "km2"]
teruletatvalt = [100, 100, 100, 100, 100]

tomeg = ["g", "dkg", "kg", "q", "t"]
tomegatvalt = [10, 100, 100, 10]

hossz = ["mm", "cm", "dm", "m", "km"]
hosszatvalt = [10, 10, 10, 1000]

terfogat = ["mm3", "cm3", "dm3", "m3", "l", "kl"]
terfogatvalt = [1000, 1000, 1000, 1000, 1000]

urtartalom = ["mm3", "cm3", "dm3", "m3", "l", "kl"]
urtartalomvalt = [1000, 1000, 1000, 1000, 1000]

"""!!!!!!!!!!! Valtok befejezése !!!!!!!!!!!!!!!!!!!!"""

def szamolo(nev):
    global muvelet
    mezo1 = ertek1.get()
    mezo2 = ertek2.get()
    bemenet =int(ent_mezo1.get())
    szorzo = 1
    if nev == "Tömeg":
        elso = tomeg.index(mezo1)
        masodik = tomeg.index(mezo2)
        valto = tomegatvalt
    elif nev == "Terület":
        elso = terulet.index(mezo1)
        masodik = terulet.index(mezo2)
        valto = teruletatvalt
    elif nev == "Hossz":
        elso = hossz.index(mezo1)
        masodik = hossz.index(mezo2)
        valto = hosszatvalt
    elif nev == "Térfogat":
        elso = terfogat.index(mezo1)
        masodik = terfogat.index(mezo2)
        valto =terfogatvalt
    elif nev == "Ürtartalom":
        elso = urtartalom.index(mezo1)
        masodik = urtartalom.index(mezo2)
        valto = urtartalomvalt

    if elso > masodik:
        muvelet = False
        seged2 = elso
        elso = masodik
        masodik = seged2
    else:
        muvelet = True
    for i in range(elso, masodik):
        szorzo =  szorzo * valto[i]
    if muvelet:
        eredmeny = bemenet / szorzo
    else:
        eredmeny = bemenet * szorzo
    lbl_eredmeny.config(text=f"{eredmeny}{mezo2}")

def build(nev):
    global ertek1, ertek2, ent_mezo1, lbl_eredmeny
    def csere():
        global ertek1, ertek2
        seged = ertek1.get()
        ertek1.set(ertek2.get())
        ertek2.set(seged)
        opt_ertek1.place(relx=0.50, rely=0.35, anchor=tkinter.CENTER)
        opt_ertek2.place(relx=0.50, rely=0.65, anchor=tkinter.CENTER)
        szamolo(nev)

    program = tkinter.Toplevel(root)
    program.title(nev)
    program.geometry("400x200")

    lbl_color = Label(program, text=f"{nev} átváltó")
    lbl_color.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

    if nev == "Tömeg":
        meretkegysegek = tomeg
    elif nev == "Terület":
        meretkegysegek = terulet
    elif nev == "Hossz":
        meretkegysegek = hossz
    elif nev == "Térfogat":
        meretkegysegek = terfogat
    elif nev == "Ürtartalom":
        meretkegysegek = urtartalom

    ent_mezo1 = Entry(program)
    ent_mezo1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    ertek1 = StringVar()
    ertek1.set("Válasszon egy mértékegységet!")
    opt_ertek1 = OptionMenu(program, ertek1, *meretkegysegek)
    opt_ertek1.place(relx=0.50, rely=0.35, anchor=tkinter.CENTER)

    lbl_color = Label(program, text=f"-ból / -ből ba")
    lbl_color.place(relx=0.5, rely=0.525, anchor=tkinter.CENTER)

    ertek2 = StringVar()
    ertek2.set("Válasszon egy mértékegységet!")
    opt_ertek2 = OptionMenu(program, ertek2, *meretkegysegek)
    opt_ertek2.place(relx=0.50, rely=0.65, anchor=tkinter.CENTER)

    btn_szamol = Button(program, text="Átváltás", bg="#42f566",command=lambda:szamolo(nev))
    btn_szamol.place(relx=0.85, rely=0.525, anchor=tkinter.CENTER)

    btn_cere = Button(program, text="Csere", bg="#f5a442",command=lambda: csere())
    btn_cere.place(relx=0.85, rely=0.4, anchor=tkinter.CENTER)

    lbl_eredmeny = Label(program, text=f"", bg="green", fg="white") # !!!!!!!!!
    lbl_eredmeny.place(relx=0.85, rely=0.65, anchor=tkinter.CENTER)


def start():
    tipus = clicked.get()
    build(tipus)

root = Tk()
root.title("Mértékegységváltó")
root.geometry("400x200")

options = [
    "Tömeg",
    "Terület",
    "Hossz",
    "Térfogat",
    "Űrtartalom",
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
