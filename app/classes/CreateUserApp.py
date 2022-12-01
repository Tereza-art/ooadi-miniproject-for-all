import tkinter as tk
import socket
from tkinter import messagebox
from classes.ClientConnectionManager import ClientConnectionManager

class CreateUserApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sign Up")
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=0, column=1)
        self.title_label = tk.Label(frame, text="Create Account")
        self.title_label.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=1, column=0)
        self.fullname_label = tk.Label(frame,text="Full name*")
        self.fullname_label.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=1, column=1)
        self.fullname_entry = tk.Entry(frame, width=50)
        self.fullname_entry.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=2, column=0)
        self.username_label = tk.Label(frame,text="Username*")
        self.username_label.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=2, column=1)
        self.username_entry = tk.Entry(frame, width=50)
        self.username_entry.pack()
 
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=3, column=0)
        self.email_label = tk.Label(frame,text="E-mail*")
        self.email_label.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=3, column=1)
        self.mail_entry = tk.Entry(frame, width=50)
        self.mail_entry.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=4, column=0)
        self.phone_label = tk.Label(frame, text="Phone*")
        self.phone_label.pack()
         
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=4, column=1)
        self.phone_entry = tk.Entry(frame, width=50)
        self.phone_entry.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=5, column=0)
        self.pwd_label = tk.Label(frame, text="Password*")
        self.pwd_label.pack()
         
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=5, column=1)
        self.pwd_entry = tk.Entry(frame, width=50)
        self.pwd_entry.pack()

        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=6, column=0)
        self.req_label = tk.Label(frame, text="* = Required")
        self.req_label.pack()
 
 
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=7, column=1)
        self.login_button = tk.Button(frame, text="Confirm",command=self.createUser, bg="#211A52", fg = "white")
        self.login_button.pack(side="left")
        self.exit_button = tk.Button(frame, text="Exit", command=self.quit, bg="#211A52", fg = "white")
        self.exit_button.pack(side="right")
 
 
    def createUser(self):
        entered_fullname = self.fullname_entry.get()
        self.fullname_entry.delete(0, 'end')
        entered_username = self.username_entry.get()
        self.username_entry.delete(0, 'end')
        entered_pwd = self.pwd_entry.get()
        self.pwd_entry.delete(0, 'end')
        entered_email = self.mail_entry.get()
        self.mail_entry.delete(0, 'end')
        entered_phone = self.phone_entry.get()
        self.phone_entry.delete(0, 'end')
 
        if '' not in (entered_fullname, entered_username, entered_pwd, entered_email, entered_phone):
            #Need to check whether a user is created successfully and credentials added to UserLog
            message_to_send = ['Log_Book_Register',entered_fullname,entered_username,entered_pwd,entered_email,entered_phone]
            manager = ClientConnectionManager(message_to_send)
            message_returned = manager.send_message() #info is loaded message sent from client to server, when server receives, and returns a True


            #Log_book.add_user(entered_username, entered_pwd)
            if message_returned == True:
                self.title_label.config(text="Sign up successful!", fg="#211A52")
                messagebox.showinfo("Congrats!","Signup successful!")
                self.destroy()
            elif message_returned == False:
                self.title_label.config(text="The username/email is already taken. Try again.", fg="red")
        else:
            self.title_label.config(text="Please enter the required information.", fg="red")
       
    def quit(self):
        self.destroy()