from tkinter import *

def add_item():
    i = e.get()
    if i:
        listbox.insert(END, i)
        e.delete(0, END)

def remove_item():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index[0])

def clear_list():
    listbox.delete(0, END)

GP = Tk()
GP.title("Listbox Example")

e = Entry(GP)
e.pack()

add_button = Button(GP, text="Add", command= add_item)
add_button.pack()

remove_button = Button(GP, text="Remove", command= remove_item)
remove_button.pack()

clear_button = Button(GP, text="Clear", command= clear_list)
clear_button.pack()

listbox = Listbox(GP)
listbox.pack()

GP.mainloop()
