import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Labels
my_label = tkinter.Label(text='Old Label', font=("Arial", 24, "bold"))
# my_label.config(text="New Text By Config")
# my_label.pack()
# my_label.place(x=10, y=200)
my_label.grid(column=0, row=0)

def button_clicked():
    my_label.config(text=input.get())
    
button1 = tkinter.Button(text="Click Me", command=button_clicked)
# button1.pack()
button2 = tkinter.Button(text="New Button")
button1.grid(column=1, row=1)
button2.grid(column=2, row=0)


input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()