import tkinter as tk
from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = dict(padx=5, pady=5)
        self.option_add("*font", "Bahnschrift 15 bold")
        style = ttk.Style()
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=20)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=4)
        self.columnconfigure(4, weight=4)

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

        def damping_slider_changed(event):
            damping.set(round(damping.get(), 1))
            renew_calculation()

        def damping_spinbox_changed():
            damping.set(round(damping.get(), 1))
            renew_calculation()

        def force_amplitude_slider_changed(event):
            force_amplitude.set(round(force_amplitude.get(), 1))
            renew_calculation()

        def force_amplitude_spinbox_changed():
            force_amplitude.set(round(force_amplitude.get(), 1))
            renew_calculation()

        def force_frequency_slider_changed(event):
            force_frequency.set(round(force_frequency.get(), 1))
            renew_calculation()

        def force_frequency_spinbox_changed():
            force_frequency.set(round(force_frequency.get(), 1))
            renew_calculation()

        def time_step_slider_changed(event):
            time_step.set(round(time_step.get(), 1))
            renew_calculation()

        def time_step_spinbox_changed():
            time_step.set(round(time_step.get(), 1))
            renew_calculation()

        def time_rate_slider_changed(event):
            time_rate.set(round(time_rate.get(), 1))
            renew_calculation()

        def time_rate_spinbox_changed():
            time_rate.set(round(time_rate.get(), 1))
            renew_calculation()

        def renew_calculation():
            pass

        # get length of pendulum
        length = tk.DoubleVar(value=2.0)

        ttk.Label(self, text="Length: ") \
            .grid(column=0, row=0, sticky=tk.E, **options)
        ttk.Label(self, text="(m)") \
            .grid(column=4, row=0, sticky=tk.W, **options)
        ttk.Scale(self, variable=length, command=length_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=0, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=length, command=length_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=0, sticky=tk.W, **options)

        # get mass of pendulum
        mass = tk.DoubleVar(value=1)

        ttk.Label(self, text="Mass: ") \
            .grid(column=0, row=1, sticky=tk.E, **options)
        ttk.Label(self, text=" (kg)") \
            .grid(column=4, row=1, sticky=tk.W, **options)
        ttk.Scale(self, variable=mass, command=mass_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=1, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=mass, command=mass_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=1, sticky=tk.W, **options)

        # get gravity of pendulum
        gravity = tk.DoubleVar(value=9.8)

        ttk.Label(self, text="Gravity: ") \
            .grid(column=0, row=2, sticky=tk.E, **options)
        ttk.Label(self, text="(m/s^2)") \
            .grid(column=4, row=2, sticky=tk.W, **options)
        ttk.Scale(self, variable=gravity, command=gravity_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=2, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=gravity, command=gravity_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=2, sticky=tk.W, **options)

        # get initial_angle of pendulum
        initial_angle = tk.DoubleVar(value=10.0)

        ttk.Label(self, text="Initial Angle") \
            .grid(column=0, row=3, sticky=tk.E, **options)
        ttk.Scale(self, variable=initial_angle, command=initial_angle_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=3, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=initial_angle, command=initial_angle_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=3, sticky=tk.W, **options)
        angle_choice = tk.IntVar(value=1)
        # Dictionary to create multiple buttons
        rad_vs_degree = {"rad": 1, "degree": 2}
        for (text, rad_vs_degree) in rad_vs_degree.items():
            ttk.Radiobutton(self, text=text, variable=angle_choice, value=rad_vs_degree) \
                .grid(column=3 + int(rad_vs_degree), row=3, sticky=tk.W, **options)

        # get initial_angular_velocity of pendulum
        initial_angular_velocity = tk.DoubleVar(value=0.0)

        ttk.Label(self, text="Initial Angular Velocity:") \
            .grid(column=0, row=4, sticky=tk.E, **options)

        ttk.Scale(self, variable=initial_angular_velocity, command=initial_angular_velocity_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=4, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=initial_angular_velocity, command=initial_angular_velocity_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=4, sticky=tk.W, **options)
        velocity_choice = tk.IntVar(value=1)
        # Dictionary to create multiple buttons
        rads_vs_degrees = {"rad/s": 1, "degree/s": 2}
        for (text, rads_vs_degrees) in rads_vs_degrees.items():
            ttk.Radiobutton(self, text=text, variable=velocity_choice, value=rads_vs_degrees) \
                .grid(column=3 + int(rads_vs_degrees), row=4, sticky=tk.W, **options)

        # get damping of pendulum
        damping = tk.DoubleVar(value=0.0)

        ttk.Label(self, text="Damping: ") \
            .grid(column=0, row=5, sticky=tk.E, **options)
        ttk.Scale(self, variable=damping, command=damping_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=5, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=damping, command=damping_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=5, sticky=tk.W, **options)

        # get force_amplitude of pendulum
        force_amplitude = tk.DoubleVar(value=0.0)

        ttk.Label(self, text="Force Amplitude: ") \
            .grid(column=0, row=6, sticky=tk.E, **options)
        ttk.Scale(self, variable=force_amplitude, command=force_amplitude_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=6, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=force_amplitude, command=force_amplitude_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=6, sticky=tk.W, **options)

        # get force_frequency of pendulum
        force_frequency = tk.DoubleVar(value=0.0)

        ttk.Label(self, text="Force Frequency: ") \
            .grid(column=0, row=7, sticky=tk.E, **options)
        ttk.Scale(self, variable=force_frequency, command=force_frequency_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=7, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=force_frequency, command=force_frequency_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=7, sticky=tk.W, **options)

        # set time_step of pendulum
        time_step = tk.DoubleVar(value=0.0)

        ttk.Label(self, text="Time Step: ") \
            .grid(column=0, row=8, sticky=tk.E, **options)
        ttk.Scale(self, variable=time_step, command=time_step_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=8, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=time_step, command=time_step_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=8, sticky=tk.W, **options)

        # set time_rate of pendulum
        time_rate = tk.DoubleVar(value=0.0)

        ttk.Label(self, text="Time Rate: ") \
            .grid(column=0, row=9, sticky=tk.E, **options)
        ttk.Scale(self, variable=time_rate, command=time_rate_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=9, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=time_rate, command=time_rate_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=9, sticky=tk.W, **options)

        # Create a Tkinter variable
        dropdown_value = tk.StringVar(self)
        dropdown_value.set('Small angles')  # set the default option
        # Dictionary with options
        choices = {'Small angles', 'Euler', 'Improved Euler', 'RK4'}
        # Find the length of maximum character in the option
        menu_width = len(max(choices, key=len))

        popup_menu = ttk.OptionMenu(self, dropdown_value, *choices)
        ttk.Label(self, text="Choose a numerical method").grid(row=10, column=0, sticky=tk.EW)
        popup_menu.grid(row=10, column=1)
        style.configure("TMenubutton", font="Bahnschrift 15 bold")
        popup_menu.config(width=menu_width)

        def change_dropdown(*args):
            print(dropdown_value.get())

        # link function to change dropdown
        dropdown_value.trace('w', change_dropdown)

        self.grid(padx=50, pady=50, sticky=tk.NSEW)
