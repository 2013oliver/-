# -*- coding:UTF-8 -*-
import tkinter as tk
import tkinter.messagebox as tkm
import pyclip
tkobj = tk.Tk()
tkobj.title("九九乘法表")
tkobj.resizable(False,False)
l = []
for y in range(1,10,1):
    for x in range(1,10,1):
        if x == 1:
            l.append(f"{x} * {y} = {x * y}")
        if x != 1 and x != y:
            l[y-1] = l[y-1] + f"        {x} * {y} = {x * y}"
        if x + y == 2:
            break
        if x == y:
            l[y-1] = l[y-1] + f"        {x} * {y} = {x * y}"
            break
def copy():
    s = ""
    for j in l:
        if bool(s) == False:
            s = j
        else:
            s = s + f"\n{j}"
    pyclip.copy(s)
    tkm.showinfo("复制","已复制")
for i in l:
    tk.Label(tkobj,text=i,justify=tk.LEFT).grid(column=1,sticky=tk.W)
tk.Button(tkobj,text="复制",command=copy).grid()
tk.mainloop()