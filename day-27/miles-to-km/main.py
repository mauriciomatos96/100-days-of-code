from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=100)
window.config(padx=50, pady=50)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="Is equal to ")
equal_label.grid(column=0, row=1)

km_input = Entry()
km_input.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def calculate():
    km_input.delete(0, END)
    miles = int(miles_input.get())
    km = miles * 1.609
    km_input.insert(END, km)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2, pady=5)












window.mainloop()