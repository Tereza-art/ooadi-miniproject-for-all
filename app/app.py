import tkinter as tk
from PIL import ImageTk, Image
import tkinter.ttk as ttk
from tkinter.constants import *



from classes.Artist import Artist
from classes.Concerthall import Concerthall
from classes.CreateUserApp import CreateUserApp
from classes.Event import Event
from classes.GridLoginApp import GridLoginApp
from classes.Order import Order
from classes.Schedule import Schedule
from classes.User import User
from classes.VerticalFrame import VerticalFrame
from classes.UserLog import UserLog

def login_in_bt():        
        app=GridLoginApp()
        app.mainloop()

def sign_up_bt():
    app = CreateUserApp()
    app.mainloop()

if __name__=="__main__":   
    
    root = tk.Tk()
    root.title("TicketEasy")
    root.geometry("800x600+200-50")
    web_label = tk.Label(root, text="TicketEasy", bg="#000080", fg="#FFFFF0", font=('150%', 20, 'bold italic')).pack()
    login = tk.Button(root, text="Log In", command=login_in_bt).pack(padx=5,pady=5) 
    signup = tk.Button(root, text="Sign Up", command=sign_up_bt).pack(padx=5,pady=5)
    
    root.mainloop()    

    

    '''
    colored_window_horizontal = tk.Tk()
    hframe1 = tk.Frame(master=colored_window_horizontal, width=800, height = 600, bg="white")
    hframe2 = tk.Frame(master=colored_window_horizontal, width=600, height = 800, bg="gray")
    hframe3 = tk.Frame(master=colored_window_horizontal, width=600, height = 100, bg="lightblue")
    hframe1.pack(fill=tk.X)
   
    #hframe2.pack(fill=tk.X)
    #hframe3.pack(fill=tk.X)
    colored_window_horizontal.mainloop()
    '''