# filepath: c:\Users\EthanChan\Music\python项目\计算器\计算器.py
import tkinter as tk
add = str()
def Zero():
    global add
    add += "0"
    x.config(text=add)
def One():
    global add
    add += "1"
    x.config(text=add)

def Two():
    global add
    add += "2"
    x.config(text=add)

def Three():
    global add
    add += "3"
    x.config(text=add)
def Four():
    global add
    add += "4"
    x.config(text=add)
def Five():
    global add
    add += "5"
    x.config(text=add)
def Six():
    global add
    add += "6"
    x.config(text=add)
def Seven():
    global add
    add += "7"
    x.config(text=add)
def Eight():
    global add
    add += "8"
    x.config(text=add)
def Nine():
    global add
    add += "9"
    x.config(text=add)
def addition():
    global add
    add += "+"
    x.config(text=add)
def subtraction():
    global add
    add += "-"
    x.config(text=add)
def multiplication():
    global add
    add += "*"
    x.config(text=add)

def division():
    global add
    add += "/"
    x.config(text=add)

def outcome():
    global add
    result = eval(add)
    x.config(text=result)


def clear():
    global add
    add = str()
    x.config(text="                    ")

def dian():
    global add
    add += "."
    x.config(text=add)
def delete():
    global add
    add = add[:-1]
    x.config(text=add)

def double():
    global add
    add += "**"
    x.config(text=add)

windows = tk.Tk()
windows = windows
windows.geometry ('350x120')
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

button = tk.Button(windows, text=".", command=dian)
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

button = tk.Button(windows, text="开方", command=double)
button.config(bg='white', fg='black')
button.pack(side='left')

button = tk.Button(windows, text="=", command=outcome)
button.config(bg='white', fg='black')
button.pack(side='left')

button = tk.Button(windows, text="<—", command=delete)
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