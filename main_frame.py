import tkinter as tk
from tkinter import ttk

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}
        length_label = ttk.Label(self, text="Length").grid(column=0, row=0, sticky=tk.E, **options)

        self.grid(padx=5, pady=5, sticky=tk.NSEW)