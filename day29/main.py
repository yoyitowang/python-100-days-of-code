from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pwd_gen():
    pwo = PasswordGenerator()
    pwo.minlen=pwo.maxlen=20

    password_entry.delete(0, END)
    password_entry.insert(0, pwo.generate())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.askretrycancel(title='Alert', message='Please enter your information!')
    else:
        ok = messagebox.askokcancel(title='Message', message='Do you want to save password?')
        if ok:
            with open('password', 'a+') as f:
                f.write(f"{website} | {email} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, 'demo@email.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=26, show="*")
password_entry.grid(row=3, column=1)
password_generator = Button(text="generate", command=pwd_gen)
password_generator.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()