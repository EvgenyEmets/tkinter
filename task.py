import tkinter as tk

def fun(args):
    print("ok")
    path = tk.filedialog.askopenfilename()

tk.Tk.withdraw()
F = tk.Frame()
F.master.rowconfigure(0, weight=1)
F.master.columnconfigure(0, weight=1)
F.grid(sticky="NEWS", row=0, column=0)
F.rowconfigure(0, weight=1)
F.columnconfigure(0, weight=1)
B = tk.Button(master = F, text = "Open")
B.bind("<Button-1>", fun)
B.grid(sticky="NEWS", column=0, row=0)
tk.mainloop()
