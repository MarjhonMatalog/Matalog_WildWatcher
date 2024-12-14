import tkinter as tk
from tkinter import *
from tkinter.messagebox import askyesno,showinfo
from functools import partial #Delete Acc button will only work if pressed
import sqlite3
import os

#window
window = Tk()
window.geometry("1000x580")
window.title("Wild Watcher")
window.resizable(0,False)
window.configure(bg="#f5ede9")
#Logo
logo = PhotoImage(file="logoo/ikon.png")
window.iconphoto(True,logo)

frame11 = Frame(window)
frame11.pack (pady=10)
frame11.configure(height=1000, width=950,bg='White')
#prevent from resizing the frame11
frame11.pack_propagate(False)
frame11.grid_propagate(False)
#BORDERS
frame2 = Frame(window)
frame2.pack(pady=10)
frame2.configure(height=10,width=950,bg="#73533a")
frame2.place(x=25,y=330)
frame3 = Frame(window)
frame3.pack(pady=10)
frame3.configure(height=330,width=10,bg="#73533a")
frame3.place(x=20,y=10)
frame4 = Frame(window)
frame4.pack(pady=10)
frame4.configure(height=330,width=10,bg="#73533a")
frame4.place(x=970,y=10)
frame5 = Frame(window)
frame5.pack(pady=10)
frame5.configure(height=10,width=950,bg="#73533a")
frame5.place(x=25,y=10)
#ANIMAL SIGHTING LABEL
Sightings = Label(window,text="ANIMAL SIGHTINGS",font=("Ravie",15),bg="#73533a",fg="White")
Sightings.place(x=365,y=310)
                
#Database
def create_database():
    if not os.path.exists("users_data.db"):
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT,
                password TEXT
            )
        """)      
        #Create Animal_Sigthings Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS animal_sightings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal_name TEXT,
                location TEXT,
                date TEXT,
                description TEXT,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        connection.commit()
        connection.close()

def register_account(user, password):
    try:
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()
        
        cursor.execute("INSERT INTO users (user, password) VALUES (?, ?)", (user, password))
        connection.commit()
        
        cursor.execute("SELECT * FROM users")
        print(cursor.fetchall())
        connection.close()
        return True
    except Exception as error:
        return False

def check_existing_user(user):
    connection = sqlite3.connect("users_data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT user FROM users WHERE user = ?", (user,))
    response = cursor.fetchall()
    connection.close()
    return response
#Use to see if the user is already created
def verify_password(user,password):
    connection = sqlite3.connect("users_data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT user FROM users WHERE user = ? AND password =?", (user,password))
    response = cursor.fetchall()
    connection.close()
    return response
#Delete a user account
def delete_account(user):
    try:
        connection = sqlite3.connect("users_data.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE user = ?", (user,))
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print(f"Error deleting account: {e}")

#CONFIRMATION IN DELETING THE ACCOUNT
def ask_yes_no(user):
    ask = askyesno(title="Delete Account", message="Are you sure you want to delete your account? This action cannot be undone.")

    if ask:
        delete_account(user)
        exit_logout.destroy()
        dashboard_frame.destroy()
        animal_entry.destroy()
        animal_name.destroy()
        location_lb.destroy()
        location_entry.destroy()
        date_lb.destroy()
        date_entry.destroy()
        description_lb.destroy()
        description_entry.destroy()
        save_button.destroy
        delete_acc.destroy()
        display_button.destroy()
        hide_button.destroy()
        delete_data.destroy()
        welcome.destroy()
        login_page()
        message_box(msg="Your account has been \nsuccessfully deleted.")

    else:
        showinfo(title="Action Cancelled", message="Your account was not deleted.")
#SAVE DATA
def save_data():
    name = animal_entry.get()
    location = location_entry.get()
    date = date_entry.get()
    description = description_entry.get()

    if not name or not location or not date or not description:
        message_box(msg="Please fill in all fields.")
        return
    try:
        conn = sqlite3.connect('users_data.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO animal_sightings (animal_name, location, date, description)
            VALUES (?, ?, ?, ?)
        ''', (name, location, date, description))
        
        conn.commit()
        conn.close()
        message_box(msg="Data saved successfully!")
    except Exception as e:
        message_box(msg=f"Error saving data: {e}")

def display_data():
    try:
        conn = sqlite3.connect('users_data.db')
        cursor = conn.cursor()

        # Fetch all data from the animal_sightings table
        cursor.execute('SELECT * FROM animal_sightings')
        records = cursor.fetchall()
        conn.close()

        # Clear the frame before displaying new data
        for widget in frame11.winfo_children():
            widget.destroy()

        #SCROLLBAR
        canvas = Canvas(frame11, bg="White", width=950, height=500)
        canvas.pack(side="left", fill="both", expand=True)

        data_frame = Frame(canvas, bg="White")
        canvas.create_window((0, 0), window=data_frame, anchor="nw")

        v_scrollbar = Scrollbar(frame11, orient="vertical", command=canvas.yview)
        h_scrollbar = Scrollbar(frame11, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        v_scrollbar.place(x=3, y=50, height=200)  # Place vertical scrollbar
        h_scrollbar.place(x=5, y=305, width=940)   # Place horizontal scrollbar

        # Check if there are records
        if records:
            headers = ["Animal Name", "Location", "Date", "Description"]
            for col, header in enumerate(headers):
                header_label = tk.Label(data_frame, text=header, font=("Georgia", 14, "bold"), bg="White", fg="Black")
                header_label.grid(row=0, column=col, padx=63, pady=5, sticky="w")

            for row_index, record in enumerate(records, start=1):
                for col_index, value in enumerate(record[1:-1]):  # Exclude ID and User ID
                    data_label = tk.Label(data_frame, text=value, font=("Garamond", 12), bg="White", fg="black")
                    data_label.grid(row=row_index, column=col_index, padx=68, pady=5, sticky="w")
        else:
            no_data_label = Label(data_frame, text="No records found.", font=("Georgia", 14), bg="White", fg="Black")
            no_data_label.pack(pady=50,padx=410)

        v_scrollbar.config(command=canvas.yview)
        h_scrollbar.config(command=canvas.xview)

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    except Exception as e:
        message_box(msg=f"Error displaying data: {e}")
#DELETING A SIGHTING
def delete_by_id(record_id):
    try:
        if not record_id.isdigit():
            message_box(msg="Please enter a valid ID.")
            return

        record_id = int(record_id)

        conn = sqlite3.connect('users_data.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM animal_sightings WHERE id = ?", (record_id,))
        record = cursor.fetchone()

        if record:
            cursor.execute("DELETE FROM animal_sightings WHERE id = ?", (record_id,))
            conn.commit()
            message_box(msg="Data deleted successfully!")
        else:
            message_box(msg="Record not found.")

        conn.close()
        display_data()  # Refresh the displayed data after deletion

    except Exception as e:
        message_box(msg=f"Error deleting record: {e}")
def create_delete_button(frame, record_id, row_index):
    delete_button = Button(frame, text="Delete", font=("Garamond", 12), bg="red", fg="white", command=lambda: delete_data(record_id))
    delete_button.grid(row=row_index, column=5, padx=20, pady=10)
#HIDE TABLE
def hide_data():
    for data in frame11.winfo_children():
        data.destroy()
#MESSAGE BOX       
def message_box(msg):
    message_frame = Frame(window, relief=SOLID, highlightthickness=2, highlightbackground="gray")
    close_btn = Button(message_frame, text="X", font=("Bold", 12), bd=0, command=message_frame.destroy)
    close_btn.pack(side=TOP, anchor=E)
    message_lb = Label(message_frame, text=msg, font=("Bold", 15))
    message_lb.pack(pady=20)
    message_frame.place(x=350, y=330, width=300, height=180)
#LOGIN
def login_page():
    def verify():
        if user.get() !="":
            if password.get !="":
                if check_existing_user(user.get()):
                  if verify_password(user=user.get(), password=password.get()):

                    name = user.get()
                    login_frame.destroy()
                    username_lb.destroy()
                    user.destroy()
                    password_lb.destroy()
                    password.destroy()
                    login_btn.destroy()
                    register.destroy()
                    display_button.destroy()
                    hide_button.destroy()
                    new_dashboard(user=name)

                  else:
                    message_box(msg="Invalid Password")
                            
                else:
                    message_box(msg="Invalid Username")
            else:
                message_box(msg="Password Required")
        else:
            message_box(msg="Username Required")
    #GO TO LOGIN
    def swictch_frame():
        login_frame.destroy()
        username_lb.destroy()
        user.destroy()
        password_lb.destroy()
        password.destroy()
        login_btn.destroy()
        register.destroy()
        register_page()
        display_button.destroy()
        hide_button.destroy()

    login_frame = Frame(window)
    login_frame.pack (pady=10)
    login_frame.pack_propagate(True)
    login_frame.configure(height=220, width=207,bg= "#edcaac")
    login_frame.place(x=390,y=345)

    username_lb = Label(text="Enter User", font=("Arial",12),bg="#edcaac")
    username_lb.place(x=450,y=355)
    user = Entry(font=("Bold",12))
    user.place(x=400,y=385)

    password_lb = Label(text="Enter Password", font=("Arial",12),bg="#edcaac")
    password_lb.place(x=440,y=415)
    password = Entry(font=("Bold",12),show="●")
    password.place(x=400,y=445)

    login_btn = Button(text= "LogIn",font=("Bold", 12),bg="#d7bd82",command=verify)
    login_btn.place(x=465,y=475)

    register = Button(text="Register Now!",font=("Bold",12),bd=0, underline=True,fg="blue",bg="#edcaac",command=swictch_frame)
    register.place(x=440,y=515 )

    display_button = Button(text="Show Table", font=("Arial", 12),bg="#d2a057", command=display_data)
    display_button.pack(side="bottom")
    display_button.place(x=28,y=480)

    hide_button = Button(text="Hide Table", font=("Arial", 12),bg="#d2a057", command=hide_data)
    hide_button.pack(side="bottom")
    hide_button.place(x=28,y=520)
#REGISTER    
def register_page():
    def verify():
        if user.get() != "":
            if password.get() != "":
                if repeat_password.get() == password.get():
                    if not check_existing_user(user.get()):
                     response= register_account(user=user.get(),password=password.get())

                     if response:
                        user.delete(0,END)
                        password.delete(0,END)
                        repeat_password.delete(0,END)
                        message_box(msg="Account Created.")
                    
                    else:
                        message_box(msg="Username already exist")
                else:
                    message_box(msg="Please re-enter the password")
            else:
                message_box(msg="Password Is Required")
        else:
            message_box(msg="Username Is Required")
    #GO BACK IN LOGIN
    def go_back():
        register_frame.destroy()
        username_rg.destroy()
        user.destroy()
        password_rg.destroy()
        password.destroy()
        repeat_password_rg.destroy()
        repeat_password.destroy()
        register_btn.destroy()
        login_page_link.destroy()
        login_page()

    register_frame = Frame(window)
    register_frame.pack (pady=10)
    register_frame.pack_propagate(True)
    register_frame.configure(height=220, width=207,bg= "#edcaac")
    register_frame.place(x=390,y=345)

    username_rg = Label(text="Enter Username", font=("Arial",12),bg="#edcaac")
    username_rg.place(x=440,y=350)
    user = Entry(font=("Bold",12))
    user.place(x=400,y=375)

    password_rg = Label(text="Enter Password", font=("Arial",12),bg="#edcaac")
    password_rg.place(x=440,y=400)
    password = Entry(font=("Bold",12),show="")
    password.place(x=400,y=420)

    repeat_password_rg = Label(text="Repeat Password", font=("Arial",12),bg="#edcaac")
    repeat_password_rg.place(x=430,y=445)
    repeat_password = Entry(font=("Bold",12),show="●")
    repeat_password.place(x=400,y=465)

    register_btn = Button(text= "Register",font=("Bold", 12),bg="#d7bd82",command=verify)
    register_btn.place(x=455,y=500)

    login_page_link = Button(text="Login",font=("Bold",12),bd=0, underline=True,fg="blue",bg="#edcaac",command=go_back)
    login_page_link.place(x=465,y=535)
#NEW WINDOW FOR DELETION OF DATA INPUTED
def new_window():
        if not askyesno(title="Delete Animal Sighting?", message="Are you sure you want to delete a data? This action cannot be undone."):
         return
        new = Tk()
        new.geometry("300x200")
        new.title("Delete Data")
        def close():
             delete_by_id(delete_entry.get())  # Call delete_by_id function
             new.destroy()
        delete_data = Button(new,text="Delete Data",font=("Arial",12),command = close)
        delete_entry = Entry(new,font=("Bold", 12), bd=0, highlightthickness=2, highlightcolor="Gray", highlightbackground="Gray",width=10)
        delete_entry.insert(0,"Enter row")
        delete_entry.place(x=100,y=50)
        delete_data.place(x=100,y=100)

def new_dashboard(user):
    def logout():
        # Clear the dashboard and navigate back to the login page
        welcome.destroy()
        exit_logout.destroy()
        login_page()
        exit_logout.destroy()
        dashboard_frame.destroy()
        animal_entry.destroy()
        animal_name.destroy()
        location_lb.destroy()
        location_entry.destroy()
        date_lb.destroy()
        date_entry.destroy()
        description_lb.destroy()
        description_entry.destroy()
        save_button.destroy
        delete_acc.destroy()
        display_button.destroy()
        hide_button.destroy()
        delete_data.destroy()

     # Declare as global for access
    global dashboard_frame,welcome,animal_name,animal_entry,location_lb,location_entry,date_lb,date_entry,description_lb,description_entry,save_button,exit_logout,delete_acc,display_button,hide_button,delete_data
    # Create the dashboard
    dashboard_frame = Frame(window)
    dashboard_frame.pack(pady=10)
    dashboard_frame.pack_propagate(True)
    dashboard_frame.configure(height=220, width=950, bg="#edcaac")
    dashboard_frame.place(x=25,y=345)

    welcome = Label(text=f"Welcome {user}!", font=("Tw Cen MT Condensed", 28), bg="#edcaac")
    welcome.place(x=390, y=355)

    # Animal name input
    animal_name = Label(text="What animal did you see?", font=("Arial", 12), bg="#edcaac")
    animal_name.place(x=270, y=415)
    animal_entry = Entry(font=("Bold", 12), bd=0, highlightthickness=2, highlightcolor="Gray", highlightbackground="Gray")
    animal_entry.place(x=270, y=435)

    # Location input
    location_lb = Label(text="Where did you see the animal?", font=("Arial", 12), bg="#edcaac")
    location_lb.place(x=540, y=415)
    location_entry = Entry(font=("Bold", 12), bd=0, highlightthickness=2, highlightcolor="Gray", highlightbackground="Gray")
    location_entry.place(x=540, y=435, width=250)

    # Date input
    date_lb = Label(text="When did you see it?", font=("Arial", 12), bg="#edcaac")
    date_lb.place(x=280, y=465)
    date_entry = Entry(font=("Bold", 12), bd=0, highlightthickness=2, highlightcolor="Gray", highlightbackground="Gray")
    date_entry.insert(0,"YYYY-MM-DD")
    date_entry.place(x=270, y=485)

    # Description input
    description_lb = Label(text="Can you explain how or what it was doing?",font=("Arial", 12),bg="#edcaac")
    description_lb.place(x=520, y=465)
    description_entry = Entry(font=("Bold", 12), bd=0, highlightthickness=2, highlightcolor="Gray", highlightbackground="Gray")
    description_entry.place(x=540, y=485,width=250)

    # Save button
    save_button = Button(text="Save", font=("arial", 12),bg="#d7bd82", command=save_data)
    save_button.place(x=470, y=515)

    # Logout button
    exit_logout = Button(text="Logout", font=("arial", 12),bg="#d7bd82", command=logout)
    exit_logout.place(x=890, y=525)

    #Delete account button
    delete_acc = Button(text="Delete Account?",font=("Arial",12),bd=0, underline=True,fg="blue",bg="#edcaac",command=partial(ask_yes_no,user))
    delete_acc.pack(side="top")
    delete_acc.place(x=820,y=345)
    
    #DISPLAY,HIDE & DELETE DATA
    display_button = Button(text="Show Table", font=("Arial", 12),bg="#d2a057", command=display_data)
    display_button.pack(side="top")
    display_button.place(x=40,y=355)

    hide_button = Button(text="Hide Table", font=("Arial", 12),bg="#d2a057", command=hide_data)
    hide_button.pack(side="top")
    hide_button.place(x=40,y=395)

    delete_data = Button(text="Delete Data",font=("Arial",12),bg="#d2a057",command = new_window)
    delete_data.pack(side="top")
    delete_data.place(x=40,y=435)
    
create_database()
login_page()
window.mainloop()