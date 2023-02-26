import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Text
text = tkinter.Text(height=5, width=30)
text.focus()
text.insert(tkinter.END, "Example of text entry...")
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Check button
def checkbutton_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is ON?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radio button
def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text='Option 1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text='Option 2', value=2, variable=radio_state, command=radio_used)
radiobutton3 = tkinter.Radiobutton(text='Option 3', value=3, variable=radio_state, command=radio_used)
radiobutton4 = tkinter.Radiobutton(text='Option 4', value=4, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

# list box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ['apples', 'pear', 'banana', 'orange']
for idx, item in enumerate(fruits):
    listbox.insert(idx, item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop() 