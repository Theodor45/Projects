from tkinter import *

window = Tk()
window.title("Mile To Km")
window.minsize(width=600, height=600)
window.config(padx=30, pady=30)

entry = Entry(width=20)
entry.grid(column=1, row=0)

label1 = Label(text='Miles')
label1.grid(column=3, row=0)

label2 = Label(text='equals to')
label2.grid(column=0, row=1)

answer = Label(text='0')
answer.config(width=10)
answer.grid(column=1, row=1)

label3 = Label(text='Km')
label3.grid(column=2, row=1)

def convert():
    try:
        miles = float(entry.get())
    except ValueError:
        raise Exception("Enter a valid number dummy")
    km = miles * 1.609
    answer.config(text=round(km, 2))

calculate = Button(text='Calculate', command=convert)
calculate.grid(column=1, row=2)

















window.mainloop()