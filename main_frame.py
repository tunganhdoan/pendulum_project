import tkinter as tk
from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = dict(padx=5, pady=5)

        def length_slider_changed(event):
            length.set(round(length.get(), 1))
            renew_calculation()

        def length_spinbox_changed():
            length.set(round(length.get(), 1))
            renew_calculation()

        def mass_slider_changed(event):
            mass.set(round(mass.get(), 1))
            renew_calculation()

        def mass_spinbox_changed():
            mass.set(round(mass.get(), 1))
            renew_calculation()

        def renew_calculation():
            pass

        # get length of pendulum
        length = tk.DoubleVar(value=1.0)

        ttk.Label(self, text="Length (m)") \
            .grid(column=0, row=0, sticky=tk.E, **options)
        ttk.Scale(self, variable=length, command=length_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=0, sticky=tk.E, **options)
        ttk.Spinbox(self, textvariable=length, command=length_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=0, sticky=tk.E, **options)

        # get mass of pendulum
        mass = tk.DoubleVar(value=1.0)

        ttk.Label(self, text="Mass (kg)") \
            .grid(column=0, row=1, sticky=tk.E, **options)
        ttk.Scale(self, variable=mass, command=mass_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=1, sticky=tk.E, **options)
        ttk.Spinbox(self, textvariable=mass, command=mass_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=1, sticky=tk.E, **options)
        self.grid(padx=50, pady=50, sticky=tk.NSEW)


