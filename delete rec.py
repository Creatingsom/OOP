from tkinter import *
import sqlite3

root = Tk()
root.title("My test Project")
root.geometry("500x500")

#database
conn = sqlite3.connect("MyDB")

#create cursor
c = conn.cursor()

#create table
'''

c.execute("""CREATE TABLE "Input" (
	"Fname"	TEXT,
	"Lname"	TEXT,
	"Age"	INTEGER,
	"Address"	TEXT,
	"Email"	TEXT
)""")
'''


def submit():
    
    #database
    conn = sqlite3.connect('C:/Users/STUDENTS.DESKTOP-EUO7O66/Downloads/MyDB.db')

    #create cursor
    c = conn.cursor()
    
    #insert into Table
    c.execute("INSERT INTO Input VALUES(:Fname, :Lname, :Age, :Address, :Email)",

    {
        'Fname':Fname.get(),
        'Lname':Lname.get(),
        'Age':Age.get(),
        'Address':Address.get(),
        'Email':Email.get(),
    })

    #commit changes
    conn.commit()

    #Close connection
    conn.close()

    #Clear the text boxes
    Fname.delete(0,END)
    Lname.delete(0,END)
    Age.delete(0,END)
    Address.delete(0,END)
    Email.delete(0,END)

def query():

    conn = sqlite3.connect('C:/Users/STUDENTS.DESKTOP-EUO7O66/Downloads/MyDB.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM Input")
    records = c.fetchall()

    #print(records)
    printrec = ""
    for record in records:
        printrec+=str(x) + ". " + str(record[0])+ " " + str(record[1])+ " " + str(record[2])+ " " + str(record[3])+ " " + str(record[4])+"\n"
        
    querylabel = Label(root, text = printrec)
    querylabel.grid(row = 8, column = 0, columnspan = 2)

    conn.commit()
    conn.close()

def delete():

    #database
    conn = sqlite3.connect('C:/Users/STUDENTS.DESKTOP-EUO7O66/Downloads/MyDB.db')
    c = conn.cursor()

    c.execute("DELETE from Input WHERE oid=" + delete_box.get())
    conn.commit()
    conn.close()

#create text boxes
Fname = Entry(root, width = 30)
Fname.grid(row = 1, column = 1, padx = 20)
Lname = Entry(root, width = 30)
Lname.grid(row = 2, column = 1, padx = 20)
Age = Entry(root, width = 30)
Age.grid(row = 3, column = 1, padx = 20)
Address = Entry(root, width = 30)
Address.grid(row = 4, column = 1, padx = 20)
Email = Entry(root, width = 30)
Email.grid(row = 5, column = 1, padx = 20)
#for delete
delete_box = Entry(root, width = 30)
delete_box.grid(row = 10, column = 1, padx = 30)

#create text box label
Fname_label = Label(root, text = "First name")
Fname_label.grid(row = 1, column = 0)
Lname_label = Label(root, text = "Last Name")
Lname_label.grid(row = 2, column = 0)
Age_label = Label(root, text = "Age")
Age_label.grid(row = 3, column = 0)
Address_label = Label(root, text = "Address")
Address_label.grid(row = 4, column = 0)
Email_label = Label(root, text = "Email")
Email_label.grid(row = 5, column = 0)
#for delete label
deletebox_label = Label(root, text = "Select ID No")
deletebox_label.grid(row = 10, column = 0)


#Buttons
submit_but = Button(root, text = "Add Record to Database", command = submit)
submit_but.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

querybut = Button(root, text = "Show records", command = query)
querybut.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

deletebox_button = Button(root, text = "Delete Record", command = delete)
deletebox_button.grid(row = 12, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 136)


root.mainloop()
