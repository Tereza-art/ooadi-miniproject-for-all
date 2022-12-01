import tkinter as tk
from PIL import ImageTk, Image
import tkinter.ttk as ttk
from tkinter import messagebox 
from classes.Event import Event
from classes.Calendar import new_calendar
from classes.BuyTicketApp import BuyTicketApp

class EventApp():
    def __init__(self) :
        container = ttk.Frame()
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        def itemAdded():
            
            #File "c:\Users\PETL\Documents\GitHub\ooadi-miniproject-repo\app\classes\EventApp.py", line 26, in itemAdded
            #self.amount_entry.delete(0, 'end')
            #AttributeError: 'NoneType' object has no attribute 'delete'
            
            #entered_amount = self.amount_entry
            #self.amount_entry.delete(0, 'end')
            #print(entered_amount)
            

            #amount wish to buy: user can enter a number of tickets to buy n
            #check event.concerthall.max capacity, if the ticket is available, then user can buy it 
            #avaiable tickets = event.concerthall.max capacity-n
            #if avaiable tickets < n, then user can't buy it. 
            BuyTicketApp()


            #messagebox.showinfo("Beaware", "You have booked the ticket")
        
        new_event= Event("Event1", "5.1.2023", "Rasmus Seebach", "Music House", 800.00,"This is the first event")
        new_event2=Event("Event2", "5.3.2023", "Justin Bieber", "Music House", 1000.00, "This is the second event")
        new_event3=Event("Event3", "17.4.2023", "Jada", "Music House", 750.00, "This is the third event")
        new_event4=Event("Event4", "9.6.2023", "Thomas Helmig", "Music House", 900.00,"This is the forth event")
            
            
        for i in range(len(new_calendar.events)):
            ttk.Label(scrollable_frame, text=f'{new_calendar.events[i]}').pack()
            self.amount_label = tk.Label(scrollable_frame, text="Amount:").pack()
            self.amount_entry = tk.Entry(scrollable_frame, width=10).pack()
            tk.Button(scrollable_frame, text="Buy", width=10, command=itemAdded).pack()
            ttk.Label(scrollable_frame, text="\n").pack()

        container.place(x=0,y=150, width=600, height=400)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
