import tkinter as tk



class BuyTicketApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Book Your Ticket")
        frame = tk.Frame(master=self, borderwidth=1)
        frame.grid(row=0, column=1)
        self.title_label = tk.Label(frame, text="Ticket to buy")
        self.title_label.pack()
        self.tickets_entry = tk.Entry(frame, width=50)
        self.buy_button = tk.Button(frame, text="Buy", command=self.add_ticket, bg="#211A52", fg = "white")
        self.buy_button.pack(side="right")
    def add_ticket(self):
        user_tickets_entry = self.tickets_entry.get()
        
        

            #amount wish to buy: user can enter a number of tickets to buy n
            #check event.concerthall.max capacity, if the ticket is available, then user can buy it 
            #avaiable tickets = event.concerthall.max capacity-n
            #if avaiable tickets < n, then user can't buy it. 

       