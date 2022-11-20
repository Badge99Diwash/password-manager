from tkinter import *
from tkinter import messagebox
import json
from random import  randint,choice,shuffle

#functions
def add_click():
    website_data=website_entry.get()
    email_data=email_entry.get()
    password_data=password_entry.get()
    new_data={
        website_data:{
            'email':email_data,
            'password':password_data
        }
    }
    if len(website_data)==0 or len(email_data)==0 or len(password_data)==0:
        messagebox.showerror(title='ERROR',message='Please fill all the fields')
    else:
        try:
            with open('data.json')as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open('data.json','w')as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open('data.json','w')as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)
def click_search():
    user=website_entry.get()
    with open('data.json')as data:
        user_data=json.load(data)
    if user in user_data:
        email_name=user_data[user]['email']
        password_name=user_data[user]['password']
        messagebox.showinfo(title='info',message=f"website:{user}\nemail:{email_name}\npassword:{password_name}")
def generate_click():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    n_l=[choice(letters)for i in range(randint(8,10))]
    n_n=[choice(numbers)for i in range(randint(8,10))]
    n_s=[choice(symbols)for i in range(randint(8,10))]
    passwords=n_l+n_n+n_s
    shuffle(passwords)
    new_password="".join(passwords)
    password_entry.insert(0,new_password)

window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=50)
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)
website = Label(text='website')
website.grid(column=0, row=1)
email = Label(text='Email')
email.grid(column=0, row=2)
password = Label(text='Password')
password.grid(column=0, row=3)
#buttons
add = Button(text='Add',command=add_click)
add.grid(column=1, row=4)
generate = Button(text='Generate',command=generate_click)
generate.grid(column=2, row=3)
search = Button(text='Search',command=click_search)
search.grid(column=3, row=1)
# entry
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(END,'@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

window.mainloop()
