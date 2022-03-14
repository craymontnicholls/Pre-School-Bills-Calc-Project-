#imports all from tkinter
from tkinter import *
import os
def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Success").pack()
    Button(screen3 , text = "OK", command = delete3).pack()

#Removes the 3rd screen after usage
def delete3():
    screen3.destroy()

#Removes the 4th screen after usage
def delete4():
    screen4.destroy()

#Removes the 5th screen after usage
def delete5():
    screen5.destroy()


#Creates screen with options for user to enter different parts of the app
def session():
    screen8 = Toplevel(screen)
    screen8.title("BillsCal")
    screen8.geometry("400x400")
    Label(screen8, text = "Home", bg= "grey", font = "calibre", width = "300", height= "3").pack()
    Label(screen8, text="").pack()
    Button(screen8, text = "Enter Calculator", command = calculator).pack()
    Label(screen8, text="").pack()
    Button(screen8, text= "Enter new Child's Data").pack()
    Label(screen8, text="").pack()
    Button(screen8, text = "Enter Database").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Button(screen8, text = "Back").pack()

#Calculates the cost of child's time at the pre-school
def calculator():
    screen9 = Toplevel(screen)
    screen9.title("Calculator")
    screen9.geometry("400x400")
    Label(screen9, text = "Calculator", bg= "grey", font = "calibre", width = "300", height= "3").pack()
    Label(screen9, text="").pack()
    Label(screen9, text = "Enter Hours per week").pack()
    Entry(screen9,textvariable = "Hours").pack()

#Displays the database for the user to see
def open_database():
    print("pass")


#Tells the user that the password was inncorrect
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Error")
    screen4.geometry("150x100")
    Label(screen4, text = "Password not recognised").pack()
    Button(screen4 , text = "OK", command = delete4).pack()


#Tells the user that the username was not found
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User Error")
    screen5.geometry("150x100")
    Label(screen5, text = "User not found").pack()
    Button(screen5 , text = "OK", command = delete5).pack()


#Function that allows the user the create an account

def register_user() :

    username_info = username.get()
    password_info = password.get()
    #opens the file so text can be stroed there
    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.close()
    #clears both of the fields to stop erros
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    #tells the user that the account has been created
    Label(screen1 , text ="Registration complete", fg = "green").pack()

#Verifys the password and username of the user
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1 , "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()




def login_success():
    session()



#Makes the account for the user
def register():
    #means that these variables can be used in any fucntion
    global screen1
    global username
    global password
    global password_entry
    global username_entry

    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    #createss string variables for username and password so text can be stroed here
    username = StringVar()
    password = StringVar()
    #creates lables of text in the gui
    Label( screen1 , text="Enter Details", bg= "grey", width ="300", height = "2", font = ("Calibre", 16)).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1,textvariable = username)
    username_entry.pack()
    Label(screen1,text="Password * ").pack()
    password_entry = Entry(screen1,textvariable = password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text = "Register", width = "20", height = "2", command = register_user ).pack()

#Creates the login screen for the user to use
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Enter Details", bg="grey", width="300", height="2", font=("Calibre", 16)).pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text = "Login" ,width = 10, height = 1, command = login_verify ).pack()






#Creates the First screen for the user
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("BillsCalc")
    Label(text="BillsCalc", bg= "grey", width ="300", height = "2", font = ("Calibre", 16)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text="").pack()
    Button(text = "Register", height = "2", width = "30" ,command = register).pack()

    screen.mainloop()

#calls the main function
main_screen()