import tkinter as tk
import socket
#from classes.UserLog import UserLog
from tkinter import messagebox
from classes.EventApp import EventApp
from classes.ClientConnectionManager import ClientConnectionManager

class GridLoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Log In")
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=0, column=1)
        self.title_label = tk.Label(frame, text="Log In")
        self.title_label.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=1, column=0)
        self.username_label = tk.Label(frame,text="Username")
        self.username_label.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=1, column=1)
        self.username_entry = tk.Entry(frame, width=50)
        self.username_entry.pack()
 
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=2, column=0)
        self.pwd_label = tk.Label(frame,text="Password")
        self.pwd_label.pack()
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=2, column=1)
        self.pwd_entry = tk.Entry(frame, width=50)
        self.pwd_entry.pack()
 
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=3, column=1)
        self.login_button = tk.Button(frame, text="Log In",command=self.log_in, bg="#211A52", fg = "white")
        self.login_button.pack(side="left")
        self.exit_button = tk.Button(frame, text="Exit", command=self.quit, bg="#211A52", fg = "white")
        self.exit_button.pack(side="right")
 
    def log_in(self):

        entered_username = self.username_entry.get()
        self.username_entry.delete(0, 'end')
        entered_pwd = self.pwd_entry.get()
        self.pwd_entry.delete(0, 'end')


        message_to_send = ['Log_Book_Login',entered_username,entered_pwd]
        mangager = ClientConnectionManager(message_to_send)
        message = mangager.send_message()
        
        
        if  message == True:
            self.title_label.config(text="Login Successful!", fg="blue")
            messagebox.showinfo("Congrats!","Login successful!")
            self.destroy()
            EventApp()
          
        elif message == False:
            self.title_label.config(text="Incorrect username and/or password!", fg="red")
        else:
            self.title_label.config(text="something went horribly wrong!", fg="red")
    def quit(self):
        self.destroy()