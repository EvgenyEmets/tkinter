import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess as sp
import sys
path = ""
in_file = ""
out_file = ""

def save_as(args):
    name = asksaveasfilename()

    t = T.get('1.0', 'end')
    arg = ['xxd', '-r', '-g1', '-',  name]
    sp.run(arg, input = t.encode("UTF-8"), stdout = sp.PIPE)

def save(args):
    print("save")
    global path, out_file
    if out_file != "":
        path = out_file
    if path != "":
        print("save")
        t = T.get('1.0', 'end')
        arg = ['xxd', '-r', '-g1', '-',  path]
        sp.run(arg, input = t.encode("UTF-8"), stdout = sp.PIPE)

def fun(args):
    print("ok")
    global path, in_file
    if in_file == "":
        path = askopenfilename()
    else:
        path = in_file
        in_file = ""
        out_file = ""
    print(path)
    if path:
        splt = path.split("/")
        F.master.title(splt[-1])
        arg = ["xxd", "-g1", path]
        t = sp.run(arg, stdout = sp.PIPE)
        T.delete('1.0', 'end')
        T.insert('1.0', t.stdout)

        
F = tk.Frame()
F.master.title("main window")
F.master.rowconfigure(1, weight=1)
F.master.columnconfigure(1, weight=1)
F.master.rowconfigure(0, weight=0)
F.master.columnconfigure(0, weight=0)
F.grid(sticky="NEWS", row=0, column=0)
F.rowconfigure(0, weight=1)
F.columnconfigure(0, weight=1)
F2 = tk.Frame(master=F)
F2.grid(sticky="W", column=0, row=0)
F2.master.rowconfigure(0, weight=0)
F2.master.columnconfigure(0, weight=0)
F2.master.columnconfigure(1, weight=0)
F2.master.columnconfigure(2, weight=0)
B1 = tk.Button(master = F2, text = "Save as")
B1.bind("<Button-1>", save_as)
B1.grid(sticky="W", column=2, row=0)
B2 = tk.Button(master = F2, text = "Save")
B2.bind("<Button-1>", save)
B2.grid(sticky="W", column=1, row=0)
B3 = tk.Button(master = F2, text = "Open")
B3.bind("<Button-1>", fun)
B3.grid(sticky="W", column=0, row=0)
scrl = tk.Scrollbar(F)
scrl.grid(sticky="NS", row=1, column=1)
T = tk.Text(master=F, height=24, width=80, font=("Source Code Pro", "14"), yscrollcommand=scrl.set)
T.grid(sticky="NEWS", column=0, row=1)
argv = sys.argv
if len(argv) == 2:
    in_file = argv[1]
    fun(1)
elif len(argv) == 3:
    in_file = argv[1]
    fun(1)
    out_file = argv[2]
    save(1)
tk.mainloop()
