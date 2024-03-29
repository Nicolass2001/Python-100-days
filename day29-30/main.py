import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    pass_input.delete(0, END)
    pass_input.insert(0, password)
    
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n Password: {password} \nIs it ok to save?")

    if is_ok:
        email_input.delete(0, END)
        email_input.insert(0, "example@mail.com")
        website_input.delete(0, END)
        pass_input.delete(0, END)

        try:
            with open(file="data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    try:
        file = open(file="data.json")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        data = json.load(file)
        website = website_input.get()
        data_to_show = data.get(website)
        if data_to_show:
            email = data_to_show.get("email")
            password = data_to_show.get("password")
            messagebox.showinfo(message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")
        file.close()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(width=200, height=200)
myimg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myimg)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(width=18, text="Search", command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=46)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example@mail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

pass_generator_button = Button(width=18, text="Generate Password", command=generate_password)
pass_generator_button.grid(column=2, row=3)

add_button = Button(width=43, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()