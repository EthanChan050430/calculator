# filepath: c:\Users\EthanChan\Music\python项目\计算器\计算器2.py
import tkinter as tk
add = []
total = None
add5 = []
def Zero():
    global add
    add.append("0")
def One():
    global add
    add.append("1")

def Two():
    global add
    add.append("2")

def Three():
    global add
    add.append("3")

def Four():
    global add
    add.append("4")

def Five():
    global add
    add.append("5")

def Six():
    global add
    add.append("6")

def Seven():
    global add
    add.append("7")

def Eight():
    global add
    add.append("8")

def Nine():
    global add
    add.append("9")


def addition():
    global add,total,add2,add5
    total = "+"
    add2 = ""
    for n in add:
        add2 = add2 + n
    add5.append(add2)
    add5.append("+")
    add = []
    add6 = ""
    for n in add5:
        add6 += n
    x.config(text=str(add6))
def subtraction():
    global add,total,add2,add5
    total = "-"
    add2 = ""
    for n in add:
        add2 = add2 + n
    add5.append(add2)
    add5.append("-")
    add = []
    add6 = ""
    for n in add5:
        add6 += n
    x.config(text=str(add6))
def multiplication():
    global add,total,add2,add5
    total = "*"
    add2 = ""
    for n in add:
        add2 = add2 + n
    add5.append(add2)
    add5.append("*")
    add = []
    add6 = ""
    for n in add5:
        add6 += n
    x.config(text=str(add6))

def division():
    global add, total,add2,add5
    total = "/"
    add2 = ""
    for n in add:
        add2 = add2 + n
    add5.append(add2)
    add5.append("/")
    add = []
    add6 = ""
    for n in add5:
        add6 += n
    x.config(text=str(add6))

def outcome():
    global add,total,add2,result
    result = 0
    add3 = ""
    if total == "+":
        for n in add:
            add3 += n
        result = int(add2) + int(add3)
    elif total == "-":
        for n in add:
            add3 += n
        result = int(add2) - int(add3)
    elif total == "*":
        for n in add:
            add3 += n
        result = int(add2) * int(add3)
    elif total == "/":
        for n in add:
            add3 += n
        result = int(add2) / int(add3)
    x.config(text=str(result))


def clear():
    global add,total,add2,add3,add5
    add2 = ""
    add = []
    add3 = ''
    total = None
    add5 = []
    x.config(text="       ")



windows = tk.Tk()
windows = windows
windows.geometry ('330x120')
windows.title("计算器")
windows.resizable(0, 0)

y = tk.Label(windows, text='计算器')
y.pack()

button = tk.Button(windows, text="0", command=Zero)
button.config(bg='white',fg='black')
button.pack(side='left')

button = tk.Button(windows, text="1", command=One)
button.config(bg='white',fg='black')
button.pack(side='left')

button = tk.Button(windows, text="2", command=Two)
button.config(bg='white',fg='black')
button.pack(side='left')

button = tk.Button(windows, text="3", command=Three)
button.config(bg='white',fg='black')
button.pack(side='left')

button = tk.Button(windows, text="4", command=Four)
button.config(bg='white',fg='black')
button.pack(side='left')

button = tk.Button(windows, text="5", command=Five)
button.config(bg='white',fg='black')
button.pack(side='left')


button = tk.Button(windows, text="6", command=Six)
button.config(bg='white',fg='black')
button.pack(side='left')

button = tk.Button(windows, text="7", command=Seven)
button.config(bg='white',fg='black')
button.pack(side='left')

button = tk.Button(windows, text="8", command=Eight)
button.config(bg='white',fg='black')
button.pack(side='left')

button = tk.Button(windows, text="9", command=Nine)
button.config(bg='white',fg='black')
button.pack(side='left')

button = tk.Button(windows, text="+", command=addition)
button.config(bg='white', fg='black')
button.pack(side='left')

button = tk.Button(windows, text="-", command=subtraction)
button.config(bg='white', fg='black')
button.pack(side='left')

button = tk.Button(windows, text="*", command=multiplication)
button.config(bg='white', fg='black')
button.pack(side='left')

button = tk.Button(windows, text="/", command=division)
button.config(bg='white', fg='black')
button.pack(side='left')

button = tk.Button(windows, text="=", command=outcome)
button.config(bg='white', fg='black')
button.pack(side='left')

button = tk.Button(windows, text="C", command=clear)
button.config(bg='white', fg='black')
button.pack(side='left')

z = tk.Label(windows, text="结果：")
z.place(x=120, y=100)
x = tk.Label(windows, text="")
x.place(x=160, y=100)


windows.mainloop()