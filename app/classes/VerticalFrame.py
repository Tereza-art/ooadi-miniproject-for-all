import tkinter as tk

class VerticalFrame(tk.Frame):
    def __init__(self, master, width, height, bg_color):
        super().__init__(master, width = width, height = height, bg=bg_color)
 
    def responsive_pack(self):
        self.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)