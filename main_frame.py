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

        def gravity_slider_changed(event):
            gravity.set(round(gravity.get(), 1))
            renew_calculation()

        def gravity_spinbox_changed():
            gravity.set(round(gravity.get(), 1))
            renew_calculation()

        def initial_angle_slider_changed(event):
            initial_angle.set(round(initial_angle.get(), 1))
            renew_calculation()

        def initial_angle_spinbox_changed():
            initial_angle.set(round(initial_angle.get(), 1))
            renew_calculation()

        def initial_angular_velocity_slider_changed(event):
            initial_angular_velocity.set(round(initial_angular_velocity.get(), 1))
            renew_calculation()

        def initial_angular_velocity_spinbox_changed():
            initial_angular_velocity.set(round(initial_angular_velocity.get(), 1))
            renew_calculation()

        def renew_calculation():
            pass

        # get length of pendulum
        length = tk.DoubleVar(value=2.0)

        ttk.Label(self, text="Length (m)") \
            .grid(column=0, row=0, sticky=tk.E, **options)
        ttk.Scale(self, variable=length, command=length_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=0, sticky=tk.E, **options)
        ttk.Spinbox(self, textvariable=length, command=length_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=0, sticky=tk.E, **options)

        # get mass of pendulum
        mass = tk.DoubleVar(value=1)

        ttk.Label(self, text="Mass (kg)") \
            .grid(column=0, row=1, sticky=tk.E, **options)
        ttk.Scale(self, variable=mass, command=mass_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=1, sticky=tk.E, **options)
        ttk.Spinbox(self, textvariable=mass, command=mass_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=1, sticky=tk.E, **options)

        # get gravity of pendulum
        gravity = tk.DoubleVar(value=9.8)

        ttk.Label(self, text="Gravity (m/s^2)") \
            .grid(column=0, row=2, sticky=tk.E, **options)
        ttk.Scale(self, variable=gravity, command=gravity_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=2, sticky=tk.E, **options)
        ttk.Spinbox(self, textvariable=gravity, command=gravity_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=2, sticky=tk.E, **options)

        # get initial_angle of pendulum
        initial_angle = tk.DoubleVar(value=10.0)

        ttk.Label(self, text="Initial Angle (rad)") \
            .grid(column=0, row=3, sticky=tk.E, **options)
        ttk.Scale(self, variable=initial_angle, command=initial_angle_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=3, sticky=tk.E, **options)
        ttk.Spinbox(self, textvariable=initial_angle, command=initial_angle_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=3, sticky=tk.E, **options)
        angle_choice = tk.IntVar(value=1)
        # Dictionary to create multiple buttons
        rad_vs_degree = {"rad": 1, "degree": 2}
        for (text, rad_vs_degree) in rad_vs_degree.items():
            ttk.Radiobutton(self, text=text, variable=angle_choice, value=rad_vs_degree)\
                .grid(column=3+int(rad_vs_degree), row=3, sticky=tk.W, **options)

        # get initial_angular_velocity of pendulum
        initial_angular_velocity = tk.DoubleVar(value=0.0)

        ttk.Label(self, text="Initial Angular Velocity (rad/s)") \
            .grid(column=0, row=4, sticky=tk.E, **options)

        ttk.Scale(self, variable=initial_angular_velocity, command=initial_angular_velocity_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=4, sticky=tk.E, **options)
        ttk.Spinbox(self, textvariable=initial_angular_velocity, command=initial_angular_velocity_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=4, sticky=tk.E, **options)
        velocity_choice = tk.IntVar(value=1)
        # Dictionary to create multiple buttons
        rads_vs_degrees = {"rad/s": 1, "degree/s": 2}
        for (text, rads_vs_degrees) in rads_vs_degrees.items():
            ttk.Radiobutton(self, text=text, variable=velocity_choice, value=rads_vs_degrees)\
                .grid(column=3+int(rads_vs_degrees), row=4, sticky=tk.W, **options)

        self.grid(padx=50, pady=50, sticky=tk.NSEW)
