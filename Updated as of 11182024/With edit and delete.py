
from tkinter import *
import sqlite3
import tkinter.messagebox


     



    

def submit():
    conn = sqlite3.connect('C:/Users/STUDENTS.DESKTOP-183N938/Desktop/GP/Input.db')
    c = conn.cursor()

    c.execute("INSERT INTO Input VALUES (:Fname, :Lname, :Age, :Address, :Email)",
              {
                'Fname': f_name.get(),
                'Lname': l_name.get(),
                'Age': age.get(),
                'Address': address.get(),
                'Email': email.get(),
              })
    
    conn.commit()
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)

    tkinter.messagebox.showinfo("Info",  "Added Successfully")

def query():
    querywin = Tk()
    querywin.title('Record from Database Input')
    querywin.geometry("500x500")

    def delete():
        conn = sqlite3.connect('C:/Users/STUDENTS.DESKTOP-183N938/Desktop/GP/Input.db')
        c = conn.cursor()
        c.execute("DELETE FROM Input WHERE oid=?", (delete_box.get(),))
        conn.commit()

        delete_box.delete(0, END)

        conn.close()
        querywin.destroy()
        tkinter.messagebox.showinfo("Info",  "Deleted Successfully")
    
    conn = sqlite3.connect('C:/Users/STUDENTS.DESKTOP-183N938/Desktop/GP/Input.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM Input")
    records = c.fetchall()
    conn.close()

    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) >= 30:
            widget.grid_forget()

    print_records = ''
    for record in records:
        print_records += f"(ID: {record[5]}) {record[0]} {record[1]} {record[2]} {record[3]} {record[4]} \n"
    
    query_label = Label(querywin, text=print_records)
    query_label.grid(row=0, column=0, columnspan=2)

    delete_box = Entry(querywin, width=30)
    delete_box.grid(row=1, column=1, padx=30)

    delete_box_label = Label(querywin, text="Select ID No.")
    delete_box_label.grid(row=1, column=0)

    delete_btn = Button(querywin, text="Delete Record", command=delete)
    delete_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=105)

    
    
    def edit():
        editor = Tk()
        editor.title('Update Record from Database')
        editor.geometry("500x500")

        conn = sqlite3.connect('C:/Users/STUDENTS.DESKTOP-183N938/Desktop/GP/Input.db')
        c = conn.cursor()

        record_id = delete_box.get()

        if not record_id.isdigit():
            error_label = Label(editor, text="Please enter a valid ID number.")
            error_label.grid(row=0, column=0, columnspan=2)
            return

        c.execute("SELECT * FROM Input WHERE oid=?", (record_id,))
        record = c.fetchone()

        if not record:
            error_label = Label(editor, text="Record not found!")
            error_label.grid(row=0, column=0, columnspan=2)
            return

        Fname_editor = Entry(editor, width=30)
        Fname_editor.grid(row=0, column=1, pady=(10, 0))
        Fname_editor.insert(0, record[0])  # First name

        Fname_label = Label(editor, text="First Name")
        Fname_label.grid(row=0, column=0, padx=10, pady=(10, 0))

        # Last Name Entry and Label
        Lname_editor = Entry(editor, width=30)
        Lname_editor.grid(row=1, column=1, pady=(10, 0))
        Lname_editor.insert(0, record[1])  # Last name

        Lname_label = Label(editor, text="Last Name")
        Lname_label.grid(row=1, column=0, padx=10, pady=(10, 0))

        # Age Entry and Label
        Age_editor = Entry(editor, width=30)
        Age_editor.grid(row=2, column=1, pady=(10, 0))
        Age_editor.insert(0, record[2])  # Age

        Age_label = Label(editor, text="Age")
        Age_label.grid(row=2, column=0, padx=10, pady=(10, 0))

        # Address Entry and Label
        Address_editor = Entry(editor, width=30)
        Address_editor.grid(row=3, column=1, pady=(10, 0))
        Address_editor.insert(0, record[3])  # Address

        Address_label = Label(editor, text="Address")
        Address_label.grid(row=3, column=0, padx=10, pady=(10, 0))

        # Email Entry and Label
        Email_editor = Entry(editor, width=30)
        Email_editor.grid(row=4, column=1, pady=(10, 0))
        Email_editor.insert(0, record[4])  # Email

        Email_label = Label(editor, text="Email")
        Email_label.grid(row=4, column=0, padx=10, pady=(10, 0))

        querywin.destroy()

        def save_update():
            updated_Fname = Fname_editor.get()
            updated_Lname = Lname_editor.get()
            updated_Age = Age_editor.get()
            updated_Address = Address_editor.get()
            updated_Email = Email_editor.get()

            c.execute('''UPDATE Input SET
                            Fname = ?, Lname = ?, Age = ?, Address = ?, Email = ?
                            WHERE oid = ?''', 
                      (updated_Fname, updated_Lname, updated_Age, updated_Address, updated_Email, record_id))

            conn.commit()
            conn.close()

            editor.destroy()

            tkinter.messagebox.showinfo("Info",  "Edited Successfully")
            
        save_btn = Button(editor, text="Save Changes", command=save_update)
        save_btn.grid(row=5, column=0, columnspan=2, pady=20, padx=10, ipadx=104)

        
        
        editor.mainloop()
    update_btn = Button(querywin, text="Edit Record", command=edit)
    update_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=105)
    
    
    
root = Tk()
root.title('My CRUD Project')
root.geometry("500x500")

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

age = Entry(root, width=30)
age.grid(row=2, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=3, column=1, padx=20)

email = Entry(root, width=30)
email.grid(row=4, column=1, padx=20)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

age_label = Label(root, text="Age")
age_label.grid(row=2, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)

email_label = Label(root, text="Email")
email_label.grid(row=4, column=0)



submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=77)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=104)


root.mainloop()
