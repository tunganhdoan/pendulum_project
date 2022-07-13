import math
import tkinter as tk
from tkinter import ttk

import matplotlib
import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

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
        self.length = tk.DoubleVar(value=2.0)
        self.mass = tk.DoubleVar(value=1)
        self.gravity = tk.DoubleVar(value=9.8)
        self.initial_angle = tk.DoubleVar(value=1.0)
        self.angle_choice = tk.IntVar(value=0)
        self.initial_angular_velocity = tk.DoubleVar(value=0.0)
        self.velocity_choice = tk.IntVar(value=1)
        self.damping = tk.DoubleVar(value=0.0)
        self.force_amplitude = tk.DoubleVar(value=0.0)
        self.force_frequency = tk.DoubleVar(value=0.0)
        self.time_step = tk.DoubleVar(value=0.01)
        self.time_rate = tk.DoubleVar(value=0.0)
        self.dropdown_value = tk.StringVar(self)

        self.t = np.arange(0, 30, self.time_step.get())
        self.theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)
        self.figure = Figure(constrained_layout=True, figsize=(3, 3), dpi=100)
        self.figure.patch.set_facecolor('whitesmoke')
        self.axes = self.figure.add_subplot()
        self.line, = self.axes.plot(self.t, self.theta, 'g', label='plot')
        self.axes.autoscale(enable=None, axis="x", tight=False)
        self.axes.set_title('Harmonic motion')
        self.axes.set_xlabel('Time')
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.figure_canvas.draw()
        # pack_toolbar=False will make it easier to use a layout manager later on.
        self.toolbar = NavigationToolbar2Tk(self.figure_canvas, self, pack_toolbar=False)
        self.toolbar.update()
        # create axes
        self.figure_canvas.get_tk_widget().grid(column=10, row=0, rowspan=20, columnspan=20, padx=10, pady=20)

        self.fig = plt.Figure()
        self.t = np.arange(0, 30, self.time_step.get())

        def animate(i):
            # line.set_ydata(np.sin(t + i / 10.0))  # update the data
            self.line1.set_ydata(self.initial_angle.get() * np.cos(
                np.sqrt(self.gravity.get() / self.length.get()) * (self.t + i / 10.0)))
            return self.line1,

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0, row=22, rowspan=10, columnspan=10, padx=10, pady=20)

        self.ax = self.fig.add_subplot(111)
        self.line1, = self.ax.plot(self.t, self.initial_angle.get() * np.cos(
            np.sqrt(self.gravity.get() / self.length.get()) * self.t))
        self.ani = animation.FuncAnimation(self.fig, animate, np.arange(1, 200), interval=25, blit=True)

        self.autoscale = tk.IntVar()
        tk.Checkbutton(self, text='autoscale', variable=self.autoscale, onvalue=1, offvalue=0,
                       command=self.autoscale_cb_changed) \
            .grid(column=10, row=9, padx=10, pady=0)

        # get length of pendulum
        ttk.Label(self, text="Length: ") \
            .grid(column=0, row=0, sticky=tk.E, **options)
        ttk.Label(self, text="(m)") \
            .grid(column=4, row=0, sticky=tk.W, **options)
        ttk.Scale(self, variable=self.length, command=self.length_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=0, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.length, command=self.length_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=0, sticky=tk.W, **options)

        # get mass of pendulum
        ttk.Label(self, text="Mass: ") \
            .grid(column=0, row=1, sticky=tk.E, **options)
        ttk.Label(self, text=" (kg)") \
            .grid(column=4, row=1, sticky=tk.W, **options)
        ttk.Scale(self, variable=self.mass, command=self.mass_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=1, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.mass, command=self.mass_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=1, sticky=tk.W, **options)

        # get gravity of pendulum
        ttk.Label(self, text="Gravity: ") \
            .grid(column=0, row=2, sticky=tk.E, **options)
        ttk.Label(self, text="(m/s^2)") \
            .grid(column=4, row=2, sticky=tk.W, **options)
        ttk.Scale(self, variable=self.gravity, command=self.gravity_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=2, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.gravity, command=self.gravity_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=2, sticky=tk.W, **options)

        # get initial_angle of pendulum
        ttk.Label(self, text="Initial Angle") \
            .grid(column=0, row=3, sticky=tk.E, **options)
        ttk.Scale(self, variable=self.initial_angle, command=self.initial_angle_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=3, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.initial_angle, command=self.initial_angle_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=3, sticky=tk.W, **options)

        # Dictionary to create multiple buttons
        rad_vs_degree = {"rad": 0, "degree": 1}
        for (text, choice_value) in rad_vs_degree.items():
            ttk.Radiobutton(self, text=text, variable=self.angle_choice, value=choice_value,
                            command=self.initial_angle_choice_changed) \
                .grid(column=4 + int(choice_value), row=3, sticky=tk.W, **options)

        # get initial_angular_velocity of pendulum
        ttk.Label(self, text="Initial Angular Velocity:") \
            .grid(column=0, row=4, sticky=tk.E, **options)

        ttk.Scale(self, variable=self.initial_angular_velocity, command=self.initial_angular_velocity_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=4, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.initial_angular_velocity,
                    command=self.initial_angular_velocity_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=4, sticky=tk.W, **options)

        # Dictionary to create multiple buttons
        rads_vs_degrees = {"rad/s": 1, "degree/s": 2}
        for (text, rads_vs_degrees) in rads_vs_degrees.items():
            ttk.Radiobutton(self, text=text, variable=self.velocity_choice, value=rads_vs_degrees) \
                .grid(column=3 + int(rads_vs_degrees), row=4, sticky=tk.W, **options)

        # get damping of pendulum
        ttk.Label(self, text="Damping: ") \
            .grid(column=0, row=5, sticky=tk.E, **options)
        ttk.Scale(self, variable=self.damping, command=self.damping_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=5, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.damping, command=self.damping_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=5, sticky=tk.W, **options)

        # get force_amplitude of pendulum
        ttk.Label(self, text="Force Amplitude: ") \
            .grid(column=0, row=6, sticky=tk.E, **options)
        ttk.Scale(self, variable=self.force_amplitude, command=self.force_amplitude_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=6, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.force_amplitude, command=self.force_amplitude_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=6, sticky=tk.W, **options)

        # get force_frequency of pendulum
        ttk.Label(self, text="Force Frequency: ") \
            .grid(column=0, row=7, sticky=tk.E, **options)
        ttk.Scale(self, variable=self.force_frequency, command=self.force_frequency_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=7, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.force_frequency, command=self.force_frequency_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=7, sticky=tk.W, **options)

        # set time_step of pendulum
        ttk.Label(self, text="Time Step: ") \
            .grid(column=0, row=8, sticky=tk.E, **options)
        ttk.Scale(self, variable=self.time_step, command=self.time_step_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=8, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.time_step, command=self.time_step_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=8, sticky=tk.W, **options)

        # set time_rate of pendulum
        ttk.Label(self, text="Time Rate: ") \
            .grid(column=0, row=9, sticky=tk.E, **options)
        ttk.Scale(self, variable=self.time_rate, command=self.time_rate_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=9, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.time_rate, command=self.time_rate_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=9, sticky=tk.W, **options)

        # Create a Tkinter dropdown
        # Dictionary with options
        choices = ['Small angles', 'Euler', 'Improved Euler', 'RK4']
        # Find the length of maximum character in the option
        menu_width = len(max(choices, key=len))
        popup_menu = ttk.OptionMenu(self, self.dropdown_value, choices[0], *choices, command=self.popup_menu_changed)
        ttk.Label(self, text="Choose a numerical method").grid(row=10, column=0, sticky=tk.EW)
        popup_menu.grid(row=10, column=1)
        # set the default option
        popup_menu.config(width=menu_width)

        def change_dropdown(*args):
            pass
            # print(self.dropdown_value.get())

        # link function to change dropdown
        self.dropdown_value.trace('w', change_dropdown)

        style.configure("TMenubutton", font=set_font)
        style.configure("TRadiobutton", font=set_font)
        style.configure('TMenubutton', borderwidth=1)

        self.grid(padx=50, pady=50, sticky=tk.NSEW)

    def length_slider_changed(self, event):
        self.length.set(round(float(event), 1))
        self.update()

    def length_spinbox_changed(self):
        self.length.set(round(self.length.get(), 1))
        self.update()

    def mass_slider_changed(self, event):
        self.mass.set(round(self.mass.get(), 1))
        self.update()

    def mass_spinbox_changed(self):
        self.mass.set(round(self.mass.get(), 1))
        self.update()

    def gravity_slider_changed(self, event):
        self.gravity.set(round(self.gravity.get(), 1))
        self.update()

    def gravity_spinbox_changed(self):
        self.gravity.set(round(self.gravity.get(), 1))
        self.update()

    def initial_angle_slider_changed(self, event):
        if self.angle_choice.get() == 1:
            temp_rad = math.radians(self.initial_angle.get())
            self.initial_angle.set(round(temp_rad, 1))
        else:
            self.initial_angle.set(round(self.initial_angle.get(), 1))
        self.update()

    def initial_angle_spinbox_changed(self):
        if self.angle_choice.get() == 1:
            temp_rad = math.radians(self.initial_angle.get())
            self.initial_angle.set(round(temp_rad, 1))
        else:
            self.initial_angle.set(round(self.initial_angle.get(), 1))
        self.update()

    def initial_angle_choice_changed(self):
        if self.angle_choice.get() == 1:
            temp_rad = math.radians(self.initial_angle.get())
            self.initial_angle.set(round(temp_rad, 1))
        else:
            self.initial_angle.set(round(self.initial_angle.get(), 1))
        self.update()

    def initial_angular_velocity_slider_changed(self, event):
        self.initial_angular_velocity.set(round(self.initial_angular_velocity.get(), 1))
        self.update()

    def initial_angular_velocity_spinbox_changed(self):
        self.initial_angular_velocity.set(round(self.initial_angular_velocity.get(), 1))
        self.update()

    def damping_slider_changed(self, event):
        self.damping.set(round(self.damping.get(), 1))
        self.update()

    def damping_spinbox_changed(self):
        self.damping.set(round(self.damping.get(), 1))
        self.update()

    def force_amplitude_slider_changed(self, event):
        self.force_amplitude.set(round(self.force_amplitude.get(), 1))
        self.update()

    def force_amplitude_spinbox_changed(self):
        self.force_amplitude.set(round(self.force_amplitude.get(), 1))
        self.update()

    def force_frequency_slider_changed(self, event):
        self.force_frequency.set(round(self.force_frequency.get(), 1))
        self.update()

    def force_frequency_spinbox_changed(self):
        self.force_frequency.set(round(self.force_frequency.get(), 1))
        self.update()

    def time_step_slider_changed(self, event):
        self.time_step.set(round(self.time_step.get(), 1))
        self.update()

    def time_step_spinbox_changed(self):
        self.time_step.set(round(self.time_step.get(), 1))
        self.update()

    def time_rate_slider_changed(self, event):
        self.time_rate.set(round(self.time_rate.get(), 1))
        self.update()

    def time_rate_spinbox_changed(self):
        self.time_rate.set(round(self.time_rate.get(), 1))
        self.update()

    def popup_menu_changed(self, event):
        self.update()

    def autoscale_cb_changed(self):
        self.update()

    def update(self):

        t_initial = 0
        t_stop = 30
        t = np.arange(t_initial, t_stop, self.time_step.get())

        # Catch the choice of numerical method
        def euler(dt, v, i_theta):
            dt = dt * np.sqrt(self.gravity.get() / self.length.get())
            d_theta = dt * v
            dv = dt * (-np.sin(i_theta))
            v = v + dv
            i_theta = i_theta + d_theta
            return v, i_theta

        def euler_array(v_0, i_theta, t_0, t_end):
            temp_list = []
            t_temp = t_0
            while t_temp < t_end:
                v_0, i_theta = euler(self.time_step.get(), v_0, i_theta)
                t_temp = t_temp + self.time_step.get()
                temp_list.append((t, i_theta, v_0))
            return temp_list

        if self.dropdown_value.get() == 'Small angles':
            theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * t)
        elif self.dropdown_value.get() == 'Euler':
            euler_list = []
            euler_list = euler_array(self.initial_angular_velocity.get(), self.initial_angle.get(), t_initial, t_stop)
            t = [x[0] for x in euler_list]
            theta = [x[1] for x in euler_list]
        elif self.dropdown_value.get() == 'Improved Euler':
            theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * t)
        elif self.dropdown_value.get() == 'RK4':
            theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * t)
        else:
            theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * t)

        self.line.set_data(t, theta)

        if self.autoscale.get() == 0:
            ax1_lim = ((min(t), min(theta)), (max(t), max(theta)))
            self.axes.update_datalim(ax1_lim)
        else:
            self.axes.relim()
        self.axes.autoscale(enable=True, axis="y", tight=True)
        self.figure_canvas.draw()
        self.fig1 = plt.Figure()
        self.t = np.arange(0, 30, self.time_step.get())

        def animate1(i):
            # line.set_ydata(np.sin(t + i / 10.0))  # update the data
            self.line1.set_ydata(self.initial_angle.get() * np.cos(
                np.sqrt(self.gravity.get() / self.length.get()) * (self.t + i / 10.0)))
            return self.line1,

        canvas = FigureCanvasTkAgg(self.fig1, master=self)
        canvas.get_tk_widget().grid(column=0, row=22, rowspan=10, columnspan=10, padx=10, pady=20)

        self.ax = self.fig1.add_subplot(111)
        self.line1, = self.ax.plot(self.t, self.initial_angle.get() * np.cos(
            np.sqrt(self.gravity.get() / self.length.get()) * t))
        self.ani = animation.FuncAnimation(self.fig1, animate1, frames=200, interval=2, blit=True)

        plt.show()
