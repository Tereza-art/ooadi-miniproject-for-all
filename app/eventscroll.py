import tkinter as tk
import tkinter.ttk as ttk
from classes.Event import *    

new_event= Event("Event1", "5.1.2023", "Rasmus Seebach", "Music House", 800.00,"This is the first event")
new_event2=Event("Event2", "5.3.2023", "Justin Bieber", "Music House", 1000.00, "This is the second event")
new_event3=Event("Event3", "17.4.2023", "Jada", "Music House", 750.00, "This is the third event")
new_event4=Event("Event4", "9.6.2023", "Thomas Helmig", "Music House", 900.00,"This is the forth event")


root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

def itemAdded():
    print("ahoj")
    
for i in range(len(new_calendar.events)):
    ttk.Label(scrollable_frame, text=f'{new_calendar.events[i]}').pack()
    tk.Button(scrollable_frame, text="Buy", width=10, command=itemAdded).pack()
    ttk.Label(scrollable_frame, text="\n").pack()

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


root.mainloop()
