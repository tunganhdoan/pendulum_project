import math
import time
import tkinter as tk
from tkinter import ttk

import matplotlib
import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

matplotlib.use('TkAgg')


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Config theme styles
        options = dict(padx=5, pady=5)
        set_font = "Bahnschrift 15 bold"
        self.option_add("*font", set_font)
        style = ttk.Style()
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=20)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=4)
        self.columnconfigure(4, weight=4)
        style.configure("TMenubutton", font=set_font)
        style.configure("TRadiobutton", font=set_font)
        style.configure('TMenubutton', borderwidth=1)
        self.grid(padx=20, pady=20, sticky=tk.NSEW)

        # TK common variables
        self.length = tk.DoubleVar(value=2.0)
        self.mass = tk.DoubleVar(value=1)
        self.gravity = tk.DoubleVar(value=9.8)
        self.initial_angle = tk.DoubleVar(value=1.0)
        self.angle_choice = tk.IntVar(value=0)
        self.initial_velocity = tk.DoubleVar(value=0.0)
        self.velocity_choice = tk.IntVar(value=1)
        self.damping = tk.DoubleVar(value=0.0)
        self.force_amplitude = tk.DoubleVar(value=0.0)
        self.force_frequency = tk.DoubleVar(value=0.0)
        self.time_step = tk.DoubleVar(value=0.01)
        self.time_rate = tk.DoubleVar(value=0.01)
        self.dropdown_value = tk.StringVar(self)
        self.autoscale = tk.IntVar()
        # INTERMEDIATE VARIABLES
        self.t = np.arange(0, 30, self.time_step.get())
        self.theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)
        self.t_initial = 0
        self.t_stop = 30
        # STATIC FIGURE 1
        self.figure = Figure(constrained_layout=True, figsize=(3, 3), dpi=100)
        self.figure.patch.set_facecolor('whitesmoke')
        self.axes = self.figure.add_subplot()
        self.line, = self.axes.plot(self.t, self.theta, 'k', label='plot')
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
        self.figure_canvas.get_tk_widget().grid(column=5, row=0, rowspan=10, columnspan=10, padx=10, pady=10)

        # ANIMATING FIGURE 1
        self.fig = plt.Figure()
        self.t = np.arange(self.t_initial, self.t_stop, self.time_step.get())

        # def animate(i):
        #     # line.set_ydata(np.sin(t + i / 10.0))  # update the data
        #     self.line1.set_ydata(self.initial_angle.get() * np.cos(
        #         np.sqrt(self.gravity.get() / self.length.get()) * (self.t + i / (1 / self.time_step.get()))))
        #     return self.line1,

        def update_point(n, x, y, point):
            point.set_data(np.array([x[n], y[n]]))
            return point,

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0, row=22, rowspan=10, columnspan=10, padx=10, pady=20)

        self.ax = self.fig.add_subplot(111)
        self.theta = self.initial_angle.get() * np.cos(
            np.sqrt(self.gravity.get() / self.length.get()) * self.t)
        self.line1, = self.ax.plot(self.t, self.theta, linestyle='solid', markerfacecolor='black', color='black')
        self.point, = self.ax.plot([self.t[0]], [self.theta[0]], 'o', markersize=15, markerfacecolor='black',
                                   color='black')
        self.ani = animation.FuncAnimation(self.fig, update_point, len(self.t), fargs=(self.t, self.theta, self.point),
                                           interval=self.time_rate.get(), blit=True)
        plt.show()

        # ANIMATING FIGURE 2
        self.ani_fig1 = plt.Figure()
        self.ani_canvas1 = FigureCanvasTkAgg(self.ani_fig1, master=self)
        self.ani_canvas1.get_tk_widget().grid(column=8, row=22, rowspan=10, columnspan=10, padx=10, pady=20)
        self.ani_ax1 = self.ani_fig1.add_subplot(111)
        ani_ax1_lim = ((-10, -10), (10, 10))
        self.ani_ax1.update_datalim(ani_ax1_lim)
        self.ani_ax1.axis('equal')
        self.ani_ax1.set_xlabel('X')  # x label
        self.ani_ax1.set_ylabel('Y')  # y label
        # create a plot on those axes, which is currently empty
        self.t = np.arange(self.t_initial, self.t_stop, self.time_step.get())
        # Initialize a vector of zeros
        theta_vec = np.zeros(len(self.t))
        v_vec = np.zeros(len(self.t))
        # Set our initial condition
        theta_vec[0] = self.initial_angle.get()  # initial angle
        v_vec[0] = self.initial_velocity.get()  # initial angular velocity
        # Loop through time
        # Small angle approximation method

        # Euler's Method (approximately integrates the differential equation)
        # for i in range(1, len(self.t)):
        #     theta_vec[i] = theta_vec[i - 1] + v_vec[i - 1] * self.time_step.get()
        #     v_vec[i] = v_vec[i - 1] + (-self.gravity.get() / self.length.get() * np.sin(theta_vec[i - 1])) * \
        #                self.time_step.get()
        theta_vec = self.theta
        # create a plot on those axes, which is currently empty
        # self.ani_point1, = self.ani_ax1.plot([], [], color='mediumblue')  # initializes an empty plot
        # Now we want to plot stuff
        # Now we're putting the rod and bob in the right place
        # initialize an array containing the positions of the pendulum
        simulation_size = len(self.t)  # number of sim time points
        x_pendulum = np.zeros(simulation_size)
        y_pendulum = np.zeros(simulation_size)

        for i in range(0, simulation_size):
            x_pendulum[i] = self.length.get() * np.sin(theta_vec[i])
            y_pendulum[i] = -self.length.get() * np.cos(theta_vec[i])

        def update_bob(n, x, y, bob, arm):
            bob.set_data(np.array([x[n], y[n]]))
            arm.set_data(np.array(([0, x[n]], [0, y[n]])))
            return arm, bob,

        # self.ani_line1, = self.ani_ax1.plot(x_pendulum, y_pendulum, 'k', label='plot')
        self.ani_point1, = self.ani_ax1.plot([x_pendulum[0]], [y_pendulum[0]], 'o',
                                             markersize=15, markerfacecolor='black')
        self.ani_arm1, = self.ani_ax1.plot([0, x_pendulum[0]], [0, y_pendulum[0]])
        self.ani_bob_1 = animation.FuncAnimation(self.ani_fig1, update_bob, len(x_pendulum),
                                                     fargs=(x_pendulum, y_pendulum, self.ani_point1, self.ani_arm1),
                                                     interval=self.time_rate.get(), blit=True)
        plt.show()

        # INPUT WIDGETS
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
        ttk.Label(self, text="Initial Velocity:") \
            .grid(column=0, row=4, sticky=tk.E, **options)

        ttk.Scale(self, variable=self.initial_velocity, command=self.initial_velocity_slider_changed,
                  orient='horizontal', length=150, from_=1, to=50) \
            .grid(column=1, row=4, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.initial_velocity,
                    command=self.initial_velocity_spinbox_changed,
                    increment=0.1, wrap=True, width=5, from_=1, to=50) \
            .grid(column=2, row=4, sticky=tk.W, **options)

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
                  orient='horizontal', length=150, from_=0.01, to=0.1) \
            .grid(column=1, row=8, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.time_step, command=self.time_step_spinbox_changed,
                    increment=0.01, wrap=True, width=5, from_=0.01, to=0.1) \
            .grid(column=2, row=8, sticky=tk.W, **options)

        # set time_rate of pendulum
        ttk.Label(self, text="Time Rate: ") \
            .grid(column=0, row=9, sticky=tk.E, **options)
        ttk.Scale(self, variable=self.time_rate, command=self.time_rate_slider_changed,
                  orient='horizontal', length=150, from_=0.01, to=0.1) \
            .grid(column=1, row=9, sticky=tk.W, **options)
        ttk.Spinbox(self, textvariable=self.time_rate, command=self.time_rate_spinbox_changed,
                    increment=0.01, wrap=True, width=5, from_=0.01, to=0.1) \
            .grid(column=2, row=9, sticky=tk.W, **options)
        ttk.Button(self, text='Update animation plot', command=self.show_animation) \
            .grid(column=4, row=10, columnspan=2, sticky=tk.E, **options)

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
        tk.Checkbutton(self, text='autoscale', variable=self.autoscale, onvalue=1, offvalue=0,
                       command=self.autoscale_cb_changed) \
            .grid(column=10, row=9, padx=10, pady=0)

        def change_dropdown(*args):
            pass
            # print(self.dropdown_value.get())

        # link function to change dropdown
        self.dropdown_value.trace('w', change_dropdown)

    # Widget changed function handler
    def length_slider_changed(self, passed_value):
        self.length.set(round(float(passed_value), 1))
        self.update_data()

    def length_spinbox_changed(self):
        self.length.set(round(self.length.get(), 1))
        self.update_data()

    def mass_slider_changed(self, passed_value):
        self.mass.set(round(float(passed_value), 1))
        self.update_data()

    def mass_spinbox_changed(self):
        self.mass.set(round(self.mass.get(), 1))
        self.update_data()

    def gravity_slider_changed(self, passed_value):
        self.gravity.set(round(float(passed_value), 1))
        self.update_data()

    def gravity_spinbox_changed(self):
        self.gravity.set(round(self.gravity.get(), 1))
        self.update_data()

    def initial_angle_slider_changed(self, passed_value):
        if self.angle_choice.get() == 1:
            temp_rad = math.radians(float(passed_value))
            self.initial_angle.set(round(temp_rad, 1))
        else:
            self.initial_angle.set(round(float(passed_value), 1))
        self.update_data()

    def initial_angle_spinbox_changed(self):
        if self.angle_choice.get() == 1:
            temp_rad = math.radians(self.initial_angle.get())
            self.initial_angle.set(round(temp_rad, 1))
        else:
            self.initial_angle.set(round(self.initial_angle.get(), 1))
        self.update_data()

    def initial_angle_choice_changed(self):
        if self.angle_choice.get() == 1:
            temp_rad = math.radians(self.initial_angle.get())
            self.initial_angle.set(round(temp_rad, 1))
        else:
            self.initial_angle.set(round(self.initial_angle.get(), 1))
        self.update_data()

    def initial_velocity_slider_changed(self, passed_value):
        self.initial_velocity.set(round(float(passed_value), 1))
        self.update_data()

    def initial_velocity_spinbox_changed(self):
        self.initial_velocity.set(round(self.initial_velocity.get(), 1))
        self.update_data()

    def damping_slider_changed(self, passed_value):
        self.damping.set(round(float(passed_value), 1))
        self.update_data()

    def damping_spinbox_changed(self):
        self.damping.set(round(self.damping.get(), 1))
        self.update_data()

    def force_amplitude_slider_changed(self, passed_value):
        self.force_amplitude.set(round(float(passed_value), 1))
        self.update_data()

    def force_amplitude_spinbox_changed(self):
        self.force_amplitude.set(round(self.force_amplitude.get(), 1))
        self.update_data()

    def force_frequency_slider_changed(self, passed_value):
        self.force_frequency.set(round(float(passed_value), 1))
        self.update_data()

    def force_frequency_spinbox_changed(self):
        self.force_frequency.set(round(self.force_frequency.get(), 1))
        self.update_data()

    def time_step_slider_changed(self, passed_value):
        self.time_step.set(round(float(passed_value), 2))
        self.update_data()

    def time_step_spinbox_changed(self):
        time.sleep(1)
        self.time_step.set(round(self.time_step.get(), 2))
        self.update_data()

    def time_rate_slider_changed(self, passed_value):
        self.time_rate.set(round(float(passed_value), 2))
        self.update_data()

    def time_rate_spinbox_changed(self):
        self.time_rate.set(round(self.time_rate.get(), 2))
        self.update_data()

    def popup_menu_changed(self, passed_value):
        self.update_data()

    def autoscale_cb_changed(self):
        self.update_data()

    def show_animation(self):
        self.update_data()
        self.update_plot()

    # UPDATE DATA AND UPDATE PLOT
    def update_data(self):
        self.t = np.arange(self.t_initial, self.t_stop, self.time_step.get())

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
            theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)
        elif self.dropdown_value.get() == 'Euler':
            euler_list = euler_array(self.initial_velocity.get(), self.initial_angle.get(), self.t_initial, self.t_stop)
            t = [x[0] for x in euler_list]
            theta = [x[1] for x in euler_list]
        elif self.dropdown_value.get() == 'Improved Euler':
            theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)
        elif self.dropdown_value.get() == 'RK4':
            theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)
        else:
            theta = self.initial_angle.get() * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)

        self.line.set_data(self.t, theta)

        if self.autoscale.get() == 0:
            ax1_lim = ((min(self.t), min(theta)), (max(self.t), max(theta)))
            self.axes.update_datalim(ax1_lim)
        else:
            self.axes.relim()
        self.axes.autoscale(enable=True, axis="y", tight=True)
        self.figure_canvas.draw()
        plt.ion()
        self.fig = plt.Figure()
        # setting for animation 2
        self.ani_ax1.autoscale(enable=True, axis="both", tight=True)

    def update_plot(self):
        time.sleep(1)

        # def init():
        #     self.line1.set_ydata(self.initial_angle.get() * np.cos(
        #         np.sqrt(self.gravity.get() / self.length.get()) * self.t))
        #     # time_text.set_text('')
        #     return self.line1,

        # def animate(i):
        #     self.line1.set_ydata(self.initial_angle.get() * np.cos(
        #         np.sqrt(self.gravity.get() / self.length.get()) * (self.t + i / 10)))
        #     return self.line1,
        def update_point(n, x, y, point):
            point.set_data(np.array([x[n], y[n]]))
            return point,

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0, row=22, rowspan=10, columnspan=10, padx=10, pady=20)

        self.ax = self.fig.add_subplot(111)

        self.theta = self.initial_angle.get() * np.cos(
            np.sqrt(self.gravity.get() / self.length.get()) * self.t)

        self.line1, = self.ax.plot(self.t, self.theta, linestyle='solid', markerfacecolor='black')
        self.point, = self.ax.plot([self.t[0]], [self.theta[0]], 'o', markersize=15, markerfacecolor='black')

        self.ani = animation.FuncAnimation(self.fig, update_point, len(self.t), fargs=(self.t, self.theta, self.point),
                                           interval=self.time_rate.get(), blit=True)
        plt.show()

        # 2nd
        self.ani_fig1 = plt.Figure()
        self.ani_canvas1 = FigureCanvasTkAgg(self.ani_fig1, master=self)
        self.ani_canvas1.get_tk_widget().grid(column=8, row=22, rowspan=10, columnspan=10, padx=10, pady=20)
        self.ani_ax1 = self.ani_fig1.add_subplot(111)
        ani_ax1_lim = ((-10, -10), (10, 10))
        self.ani_ax1.update_datalim(ani_ax1_lim)
        self.ani_ax1.axis('equal')
        self.ani_ax1.set_xlabel('X')  # x label
        self.ani_ax1.set_ylabel('Y')  # y label
        # create a plot on those axes, which is currently empty
        self.t = np.arange(0, 30, self.time_step.get())
        # Initialize a vector of zeros
        theta_vec = np.zeros(len(self.t))
        v_vec = np.zeros(len(self.t))
        # Set our initial condition
        theta_vec[0] = self.initial_angle.get()  # initial angle
        v_vec[0] = self.initial_velocity.get()  # initial angular velocity
        # Loop through time
        # Small angle approximation method

        # Euler's Method (approximately integrates the differential equation)
        # for i in range(1, len(self.t)):
        #     theta_vec[i] = theta_vec[i - 1] + v_vec[i - 1] * self.time_step.get()
        #     v_vec[i] = v_vec[i - 1] + (-self.gravity.get() / self.length.get() * np.sin(theta_vec[i - 1])) * \
        #                self.time_step.get()
        theta_vec = self.theta
        # create a plot on those axes, which is currently empty
        # self.ani_point1, = self.ani_ax1.plot([], [], color='mediumblue')  # initializes an empty plot
        # Now we want to plot stuff
        # Now we're putting the rod and bob in the right place
        # initialize an array containing the positions of the pendulum
        simulation_size = len(self.t)  # number of sim time points
        x_pendulum = np.zeros(simulation_size)
        y_pendulum = np.zeros(simulation_size)

        for i in range(0, simulation_size):
            x_pendulum[i] = self.length.get() * np.sin(theta_vec[i])
            y_pendulum[i] = -self.length.get() * np.cos(theta_vec[i])

        def update_bob(n, x, y, bob, arm):
            bob.set_data(np.array([x[n], y[n]]))
            arm.set_data(np.array(([0, x[n]], [0, y[n]])))
            return arm, bob,

        # self.ani_line1, = self.ani_ax1.plot(x_pendulum, y_pendulum, 'k', label='plot')
        self.ani_point1, = self.ani_ax1.plot([x_pendulum[0]], [y_pendulum[0]], 'o',
                                             markersize=15, markerfacecolor='black')
        self.ani_arm1, = self.ani_ax1.plot([0, x_pendulum[0]], [0, y_pendulum[0]])
        self.ani_bob_1 = animation.FuncAnimation(self.ani_fig1, update_bob,
                                                 fargs=(x_pendulum, y_pendulum, self.ani_point1, self.ani_arm1),
                                                 frames=len(self.theta)*5, interval=self.time_rate.get(), blit=True)
        plt.show()
        print(f"time step : {self.time_step.get()}")
        print(f"time rate : {self.time_rate.get()}")

