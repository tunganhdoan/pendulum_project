import tkinter as tk
from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = dict(padx=5, pady=5)

        def length_slider_changed(event):
            pass

        # get length of pendulum
        length = tk.DoubleVar(value=1.0)

        ttk.Label(self, text="Length") \
            .grid(column=0, row=0, sticky=tk.E, **options)
        ttk.Scale(self, variable=length, command=length_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=0, sticky=tk.E, **options)
        ttk.Spinbox(self, textvariable=length, wrap=True, width=15, from_=1, to=50) \
            .grid(column=2, row=0, sticky=tk.E, **options)
        self.grid(padx=50, pady=50, sticky=tk.NSEW)
