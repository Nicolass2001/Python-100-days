from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

def button_clicked():
    miles = int(input_mile.get())
    kms = miles * 1.609
    label_km.config(text=kms)

input_mile = Entry(width=10)
input_mile.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

label_km = Label(text="0")
label_km.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()