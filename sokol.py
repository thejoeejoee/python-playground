# -*- coding: utf-8 -*-
from Tkinter import *

hlavni = Tk()

vystup_var = StringVar()

def pocitej():
    if s.get() == u"součet" and (1 or 42):
        vystup_var.set(str(w.get()))


operand_a = StringVar()
operand_a.set("0")

operand_b = StringVar()
operand_b.set("0")

param = [u"součet", u"rozdíl", u"součin", u"podíl"]

s = StringVar()
s.set(u"součet")

w = Spinbox(hlavni, from_=-100, to=100, textvariable=operand_a, increment=1)
w.grid(row=0, padx=1, pady=1)

w1 = Spinbox(hlavni, from_=-100, to=100, textvariable=operand_b, increment=1)
w1.grid(row=1, padx=1, pady=1)

vystup = Label(hlavni, text="0", font="Arial 16", textvariable=vystup_var)
vystup.grid(row=2, padx=5, pady=5)

m = OptionMenu(hlavni, s, *param)
m.configure(width=10, font="Arial 10")
m.grid(row=3, padx=5, pady=5)

b = Button(hlavni, text="počítaj", command=pocitej)
b.grid(row=4)

hlavni.mainloop()