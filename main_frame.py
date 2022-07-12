import math
import tkinter as tk
from tkinter import ttk

import matplotlib as plt
import numpy as np

plt.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = dict(padx=5, pady=5)
        set_font = "Bahnschrift 15 bold"
        self.option_add("*font", set_font)
        style = ttk.Style()
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=20)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=4)
        self.columnconfigure(4, weight=4)
        # TK common variables
        length = tk.DoubleVar(value=2.0)
        mass = tk.DoubleVar(value=1)
        gravity = tk.DoubleVar(value=9.8)
        initial_angle = tk.DoubleVar(value=1.0)
        angle_choice = tk.IntVar(value=0)
        initial_angular_velocity = tk.DoubleVar(value=0.0)
        velocity_choice = tk.IntVar(value=1)
        damping = tk.DoubleVar(value=0.0)
        force_amplitude = tk.DoubleVar(value=0.0)
        force_frequency = tk.DoubleVar(value=0.0)
        time_step = tk.DoubleVar(value=0.01)
        time_rate = tk.DoubleVar(value=0.0)
        dropdown_value = tk.StringVar(self)

        def length_slider_changed(event):
            length.set(round(length.get(), 1))
            update()

        def length_spinbox_changed():
            length.set(round(length.get(), 1))
            update()

        def mass_slider_changed(event):
            mass.set(round(mass.get(), 1))
            update()

        def mass_spinbox_changed():
            mass.set(round(mass.get(), 1))
            update()

        def gravity_slider_changed(event):
            gravity.set(round(gravity.get(), 1))
            update()

        def gravity_spinbox_changed():
            gravity.set(round(gravity.get(), 1))
            update()

        def initial_angle_slider_changed(event):
            if angle_choice.get() == 1:
                temp_rad = math.radians(initial_angle.get())
                initial_angle.set(round(temp_rad, 1))
            else:
                initial_angle.set(round(initial_angle.get(), 1))
            update()

        def initial_angle_spinbox_changed():
            if angle_choice.get() == 1:
                temp_rad = math.radians(initial_angle.get())
                initial_angle.set(round(temp_rad, 1))
            else:
                initial_angle.set(round(initial_angle.get(), 1))
            update()

        def initial_angle_choice_changed():
            if angle_choice.get() == 1:
                temp_rad = math.radians(initial_angle.get())
                initial_angle.set(round(temp_rad, 1))
            else:
                initial_angle.set(round(initial_angle.get(), 1))
            update()

        def initial_angular_velocity_slider_changed(event):
            initial_angular_velocity.set(round(initial_angular_velocity.get(), 1))
            update()

        def initial_angular_velocity_spinbox_changed():
            initial_angular_velocity.set(round(initial_angular_velocity.get(), 1))
            update()

        def damping_slider_changed(event):
            damping.set(round(damping.get(), 1))
            update()

        def damping_spinbox_changed():
            damping.set(round(damping.get(), 1))
            update()

        def force_amplitude_slider_changed(event):
            force_amplitude.set(round(force_amplitude.get(), 1))
            update()

        def force_amplitude_spinbox_changed():
            force_amplitude.set(round(force_amplitude.get(), 1))
            update()

        def force_frequency_slider_changed(event):
            force_frequency.set(round(force_frequency.get(), 1))
            update()

        def force_frequency_spinbox_changed():
            force_frequency.set(round(force_frequency.get(), 1))
            update()

        def time_step_slider_changed(event):
            time_step.set(round(time_step.get(), 1))
            update()

        def time_step_spinbox_changed():
            time_step.set(round(time_step.get(), 1))
            update()

        def time_rate_slider_changed(event):
            time_rate.set(round(time_rate.get(), 1))
            update()

        def time_rate_spinbox_changed():
            time_rate.set(round(time_rate.get(), 1))
            update()

        def popup_menu_changed(event):
            update()

        def autoscale_cb_changed():
            update()

        l = 2.0
        g = 9.8
        dt = 0.01
        t = np.arange(0, 30, dt)
        theta_0 = 1.0
        theta = theta_0 * np.cos(np.sqrt(g / l) * t)
        figure = Figure(constrained_layout=True, figsize=(3, 3), dpi=100)
        figure.patch.set_facecolor('whitesmoke')
        axes = figure.add_subplot()
        line, = axes.plot(t, theta, 'g', label='plot')
        axes.autoscale(enable=None, axis="x", tight=False)
        axes.set_title('Harmonic motion')
        axes.set_xlabel('Time')
        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, master=self)
        figure_canvas.draw()
        # pack_toolbar=False will make it easier to use a layout manager later on.
        toolbar = NavigationToolbar2Tk(figure_canvas, self, pack_toolbar=False)
        toolbar.update()
        # create axes
        figure_canvas.get_tk_widget().grid(column=10, row=0, rowspan=100, columnspan=100, padx=10, pady=20)
        autoscale = tk.IntVar()
        tk.Checkbutton(self, text='autoscale', variable=autoscale, onvalue=1, offvalue=0, command=autoscale_cb_changed) \
            .grid(column=10, row=9, padx=10, pady=0)

        def update():
            l = length.get()
            m = mass.get()
            g = gravity.get()
            theta_0 = initial_angle.get()
            v_0 = initial_angular_velocity.get()
            beta = damping.get()
            a = force_amplitude.get()
            f = force_frequency.get()
            dt = time_step.get()
            rate = time_rate.get()
            t_initial = 0
            t_stop = 30
            t = np.arange(t_initial, t_stop, dt)
            sim_points = len(t)
            index = np.arange(0, sim_points, 1)

            # Catch the choice of numerical method
            def euler(dt, v, theta):
                dt = dt * np.sqrt(g / l)
                d_theta = dt * v
                dv = dt * (-np.sin(theta))
                v = v + dv
                theta = theta + d_theta
                return (v, theta)

            def euler_array(v_0, theta_0, t_0, t_end):
                theta_prime = v_0
                theta = theta_0
                t = t_0
                euler_list = []
                while t < t_end:
                    (theta_prime, theta) = euler(dt, theta_prime, theta)
                    t = t + dt
                    euler_list.append((t, theta, theta_prime))

                return euler_list

            if dropdown_value.get() == 'Small angles':
                theta = theta_0 * np.cos(np.sqrt(g / l) * t)
            elif dropdown_value.get() == 'Euler':
                euler_list = []
                euler_list = euler_array(v_0, theta_0, t_initial, t_stop)
                t = [x[0] for x in euler_list]
                theta = [x[1] for x in euler_list]
            elif dropdown_value.get() == 'Improved Euler':
                theta = theta_0 * np.cos(np.sqrt(g / l) * t)
            elif dropdown_value.get() == 'RK4':
                theta = theta_0 * np.cos(np.sqrt(g / l) * t)
            else:
                theta = theta_0 * np.cos(np.sqrt(g / l) * t)

            line.set_data(t, theta)
            if autoscale.get() == 0:
                ax1_lim = ((min(t), min(theta)), (max(t), max(theta)))
                axes.update_datalim(ax1_lim)
            else:
                axes.relim()
            axes.autoscale(enable=True, axis="y", tight=True)
            figure_canvas.draw()

        # get length of pendulum


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


        ttk.Label(self, text="Initial Angle") \
            .grid(column=0, row=3, sticky=tk.E, **options)
        ttk.Scale(self, variable=initial_angle, command=initial_angle_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=3, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=initial_angle, command=initial_angle_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=3, sticky=tk.W, **options)

        # Dictionary to create multiple buttons
        rad_vs_degree = {"rad": 0, "degree": 1}
        for (text, choice_value) in rad_vs_degree.items():
            ttk.Radiobutton(self, text=text, variable=angle_choice, value=choice_value,
                            command=initial_angle_choice_changed) \
                .grid(column=4 + int(choice_value), row=3, sticky=tk.W, **options)

        # get initial_angular_velocity of pendulum


        ttk.Label(self, text="Initial Angular Velocity:") \
            .grid(column=0, row=4, sticky=tk.E, **options)

        ttk.Scale(self, variable=initial_angular_velocity, command=initial_angular_velocity_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=4, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=initial_angular_velocity, command=initial_angular_velocity_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=4, sticky=tk.W, **options)

        # Dictionary to create multiple buttons
        rads_vs_degrees = {"rad/s": 1, "degree/s": 2}
        for (text, rads_vs_degrees) in rads_vs_degrees.items():
            ttk.Radiobutton(self, text=text, variable=velocity_choice, value=rads_vs_degrees) \
                .grid(column=3 + int(rads_vs_degrees), row=4, sticky=tk.W, **options)

        # get damping of pendulum


        ttk.Label(self, text="Damping: ") \
            .grid(column=0, row=5, sticky=tk.E, **options)
        ttk.Scale(self, variable=damping, command=damping_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=5, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=damping, command=damping_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=5, sticky=tk.W, **options)

        # get force_amplitude of pendulum


        ttk.Label(self, text="Force Amplitude: ") \
            .grid(column=0, row=6, sticky=tk.E, **options)
        ttk.Scale(self, variable=force_amplitude, command=force_amplitude_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=6, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=force_amplitude, command=force_amplitude_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=6, sticky=tk.W, **options)

        # get force_frequency of pendulum


        ttk.Label(self, text="Force Frequency: ") \
            .grid(column=0, row=7, sticky=tk.E, **options)
        ttk.Scale(self, variable=force_frequency, command=force_frequency_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=7, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=force_frequency, command=force_frequency_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=7, sticky=tk.W, **options)

        # set time_step of pendulum


        ttk.Label(self, text="Time Step: ") \
            .grid(column=0, row=8, sticky=tk.E, **options)
        ttk.Scale(self, variable=time_step, command=time_step_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=8, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=time_step, command=time_step_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=8, sticky=tk.W, **options)

        # set time_rate of pendulum


        ttk.Label(self, text="Time Rate: ") \
            .grid(column=0, row=9, sticky=tk.E, **options)
        ttk.Scale(self, variable=time_rate, command=time_rate_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=9, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=time_rate, command=time_rate_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=9, sticky=tk.W, **options)

        # Create a Tkinter dropdown


        # Dictionary with options
        choices = ['Small angles', 'Euler', 'Improved Euler', 'RK4']
        # Find the length of maximum character in the option
        menu_width = len(max(choices, key=len))
        popup_menu = ttk.OptionMenu(self, dropdown_value, choices[0], *choices, command=popup_menu_changed)
        ttk.Label(self, text="Choose a numerical method").grid(row=10, column=0, sticky=tk.EW)
        popup_menu.grid(row=10, column=1)
        # set the default option
        popup_menu.config(width=menu_width)

        def change_dropdown(*args):
            pass
            # print(dropdown_value.get())

        # link function to change dropdown
        dropdown_value.trace('w', change_dropdown)

        style.configure("TMenubutton", font=set_font)
        style.configure("TRadiobutton", font=set_font)
        style.configure('TMenubutton', borderwidth=1)

        self.grid(padx=50, pady=50, sticky=tk.NSEW)
