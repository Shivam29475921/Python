from tkinter import *

window = Tk()
window.title("Converter")
window.minsize(width=100, height=50)
window.config(padx=50, pady=50)

distance_in_miles = Entry(width=10)
distance_in_miles.grid(column=1, row=0)

miles_text = Label(text="miles")
miles_text.grid(column=2, row=0)

is_equal_to_text = Label(text="is equal to")
is_equal_to_text.grid(column=0, row=1)

km_text = Label(text="km")
km_text.grid(column=2, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)


# convert
def convert():
    miles = int(distance_in_miles.get())
    km = miles * 1.6
    answer.config(text=f"{km}")


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
