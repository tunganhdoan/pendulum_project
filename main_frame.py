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
        self.initial_angle_deg = tk.DoubleVar(value=30.0)
        self.initial_velocity = tk.DoubleVar(value=0.0)
        self.velocity_choice = tk.IntVar(value=1)
        self.damping = tk.DoubleVar(value=0.0)
        self.force_amplitude = tk.DoubleVar(value=0.0)
        self.force_frequency = tk.DoubleVar(value=0.0)
        self.time_step = tk.DoubleVar(value=0.01)
        self.time_rate = tk.DoubleVar(value=0.01)
        self.dropdown_value = tk.StringVar(self)
        self.autoscale = tk.IntVar(value=1)
        # INTERMEDIATE VARIABLES
        self.t_initial = 0
        self.t_stop = 30
        self.t = np.arange(self.t_initial, self.t_stop, self.time_step.get())
        self.theta_0 = math.radians(self.initial_angle_deg.get())
        self.theta = self.theta_0 * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)

        # FIGURE LAYOUTS
        self.fig1 = Figure(constrained_layout=True, figsize=(3, 3), dpi=100)
        self.fig1.patch.set_facecolor('whitesmoke')
        self.ax1 = self.fig1.add_subplot()
        self.ax1.autoscale(enable=True, axis="y", tight=True)
        self.line1, = self.ax1.plot([], [])
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self)

        def plot_figure_1():
            self.line1, = self.ax1.plot(self.t, self.theta, 'k', label='Figure 1')
            self.ax1.autoscale(enable=True, axis="y", tight=False)
            self.ax1.set_title('Harmonic motion')
            self.ax1.set_xlabel('Time')
            self.canvas1.draw()
            self.canvas1.get_tk_widget().grid(column=5, row=0, rowspan=10, columnspan=10, padx=10, pady=10)

        def plot_figure_2():
            self.fig2 = plt.Figure()
            self.ax2 = self.fig2.add_subplot(111)
            self.line2, = self.ax2.plot([], [], label='Figure 2')
            self.point2, = self.ax2.plot([], [], label='Figure 2')
            self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self)
            self.canvas2.draw()

            def update_point(n, x, y, point):
                point.set_data(np.array([x[n], y[n]]))
                return point,

            self.canvas2.get_tk_widget().grid(column=0, row=22, rowspan=10, columnspan=10, padx=10, pady=20)
            self.line2, = self.ax2.plot(self.t, self.theta, linestyle='solid', markerfacecolor='black', color='black')
            self.point2, = self.ax2.plot([self.t[0]], [self.theta[0]], 'o', markersize=15, markerfacecolor='black',
                                         color='black')
            self.ani2 = animation.FuncAnimation(self.fig2, update_point, frames=len(self.t),
                                                fargs=(self.t, self.theta, self.point2),
                                                interval=self.time_rate.get(), blit=True)

        def plot_figure_3():
            self.fig3 = plt.Figure()
            self.ax3 = self.fig3.add_subplot(111)
            self.point3, = self.ax3.plot([], [], label='Figure 3')
            self.arm3, = self.ax3.plot([], [], label='Figure 3')
            self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self)
            self.ax3.axis('equal')
            self.ax3.set_xlabel('X')  # x label
            self.ax3.set_ylabel('Y')  # y label
            self.canvas3.get_tk_widget().grid(column=8, row=22, rowspan=10, columnspan=10, padx=10, pady=20)
            ax3_lim = ((-10, -10), (10, 10))
            self.ax3.update_datalim(ax3_lim)
            # Euler's Method (approximately integrates the differential equation)
            # for i in range(1, len(self.t)):
            #     theta_vec[i] = theta_vec[i - 1] + v_vec[i - 1] * self.time_step.get()
            #     v_vec[i] = v_vec[i - 1] + (-self.gravity.get() / self.length.get() * np.sin(theta_vec[i - 1])) * \
            #                self.time_step.get()
            simulation_size = len(self.t)  # number of sim time points
            x_pendulum = np.zeros(simulation_size)
            y_pendulum = np.zeros(simulation_size)

            for i in range(0, simulation_size):
                x_pendulum[i] = self.length.get() * np.sin(self.theta[i])
                y_pendulum[i] = -self.length.get() * np.cos(self.theta[i])

            def update_bob(n, x, y, bob, arm):
                bob.set_data(np.array([x[n], y[n]]))
                arm.set_data(np.array(([0, x[n]], [0, y[n]])))
                return arm, bob,

            self.point3, = self.ax3.plot([x_pendulum[0]], [y_pendulum[0]], 'o',
                                         markersize=15, markerfacecolor='black')
            self.arm3, = self.ax3.plot([0, x_pendulum[0]], [0, y_pendulum[0]])
            self.ani3 = animation.FuncAnimation(self.fig3, update_bob, frames=len(x_pendulum),
                                                fargs=(x_pendulum, y_pendulum, self.point3, self.arm3),
                                                interval=self.time_rate.get(), blit=True)

        def create_widgets():
            # get length of pendulum
            ttk.Label(self, text="Length: ").grid(column=0, row=0, sticky=tk.E, **options)
            ttk.Label(self, text="(m)").grid(column=4, row=0, sticky=tk.W, **options)
            ttk.Scale(self, variable=self.length, command=length_slider_changed, orient='horizontal', length=150, from_=1, to=10) \
                .grid(column=1, row=0, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.length, command=length_spinbox_changed, increment=1, wrap=True, width=5, from_=1, to=10) \
                .grid(column=2, row=0, sticky=tk.W, **options)

            # get mass of pendulum
            ttk.Label(self, text="Mass: ").grid(column=0, row=1, sticky=tk.E, **options)
            ttk.Label(self, text=" (kg)").grid(column=4, row=1, sticky=tk.W, **options)
            ttk.Scale(self, variable=self.mass, command=mass_slider_changed, orient='horizontal', length=150, from_=1, to=50) \
                .grid(column=1, row=1, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.mass, command=mass_spinbox_changed, increment=0.1, wrap=True, width=5, from_=1, to=50) \
                .grid(column=2, row=1, sticky=tk.W, **options)

            # get gravity of pendulum
            ttk.Label(self, text="Gravity: ").grid(column=0, row=2, sticky=tk.E, **options)
            ttk.Label(self, text="(m/s^2)").grid(column=4, row=2, sticky=tk.W, **options)
            ttk.Scale(self, variable=self.gravity, command=gravity_slider_changed,
                      orient='horizontal', length=150, from_=1, to=50).grid(column=1, row=2, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.gravity, command=gravity_spinbox_changed, increment=0.1, wrap=True, width=5, from_=1, to=50) \
                .grid(column=2, row=2, sticky=tk.W, **options)

            # get initial_angle of pendulum
            ttk.Label(self, text="Initial Angle").grid(column=0, row=3, sticky=tk.E, **options)
            ttk.Scale(self, variable=self.initial_angle_deg, command=initial_angle_slider_changed, orient='horizontal', length=150, from_=1, to=100) \
                .grid(column=1, row=3, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.initial_angle_deg, command=initial_angle_spinbox_changed, increment=0.1, wrap=True, width=5, from_=1, to=100) \
                .grid(column=2, row=3, sticky=tk.W, **options)

            # get initial_angular_velocity of pendulum
            ttk.Label(self, text="Initial Velocity:").grid(column=0, row=4, sticky=tk.E, **options)

            ttk.Scale(self, variable=self.initial_velocity, command=initial_velocity_slider_changed, orient='horizontal', length=150, from_=1, to=50) \
                .grid(column=1, row=4, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.initial_velocity, command=initial_velocity_spinbox_changed, increment=0.1, wrap=True, width=5, from_=1, to=50) \
                .grid(column=2, row=4, sticky=tk.W, **options)

            # get damping of pendulum
            ttk.Label(self, text="Damping: ").grid(column=0, row=5, sticky=tk.E, **options)
            ttk.Scale(self, variable=self.damping, command=damping_slider_changed,orient='horizontal', length=150, from_=1, to=50) \
                .grid(column=1, row=5, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.damping, command=damping_spinbox_changed, increment=0.1, wrap=True, width=5, from_=1, to=50) \
                .grid(column=2, row=5, sticky=tk.W, **options)

            # get force_amplitude of pendulum
            ttk.Label(self, text="Force Amplitude: ").grid(column=0, row=6, sticky=tk.E, **options)
            ttk.Scale(self, variable=self.force_amplitude, command=force_amplitude_slider_changed, orient='horizontal', length=150, from_=1, to=50) \
                .grid(column=1, row=6, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.force_amplitude, command=force_amplitude_spinbox_changed, increment=0.1, wrap=True, width=5, from_=1, to=50) \
                .grid(column=2, row=6, sticky=tk.W, **options)

            # get force_frequency of pendulum
            ttk.Label(self, text="Force Frequency: ").grid(column=0, row=7, sticky=tk.E, **options)
            ttk.Scale(self, variable=self.force_frequency, command=force_frequency_slider_changed,
                      orient='horizontal', length=150, from_=1, to=50).grid(column=1, row=7, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.force_frequency, command=force_frequency_spinbox_changed,
                        increment=0.1, wrap=True, width=5, from_=1, to=50).grid(column=2, row=7, sticky=tk.W, **options)

            # set time_step of pendulum
            ttk.Label(self, text="Time Step: ").grid(column=0, row=8, sticky=tk.E, **options)
            ttk.Scale(self, variable=self.time_step, command=time_step_slider_changed, orient='horizontal', length=150, from_=0.01, to=0.1) \
                .grid(column=1, row=8, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.time_step, command=time_step_spinbox_changed, increment=0.01, wrap=True, width=5, from_=0.01, to=0.1) \
                .grid(column=2, row=8, sticky=tk.W, **options)

            # set time_rate of pendulum
            ttk.Label(self, text="Time Rate: ").grid(column=0, row=9, sticky=tk.E, **options)
            ttk.Scale(self, variable=self.time_rate, command=time_rate_slider_changed, orient='horizontal', length=150, from_=0.01, to=0.1) \
                .grid(column=1, row=9, sticky=tk.W, **options)
            ttk.Spinbox(self, textvariable=self.time_rate, command=time_rate_spinbox_changed, increment=0.01, wrap=True, width=5, from_=0.01, to=0.1) \
                .grid(column=2, row=9, sticky=tk.W, **options)
            ttk.Button(self, text='Update animation plot', command=show_animation) \
                .grid(column=4, row=10, columnspan=2, sticky=tk.E, **options)

            # Create a Tkinter dropdown
            # Dictionary with options
            choices = ['Small angles', 'Euler', 'Improved Euler', 'RK4']
            # Find the length of maximum character in the option
            menu_width = len(max(choices, key=len))
            popup_menu = ttk.OptionMenu(self, self.dropdown_value, choices[0], *choices, command=popup_menu_changed)
            ttk.Label(self, text="Choose a numerical method").grid(row=10, column=0, sticky=tk.EW)
            popup_menu.grid(row=10, column=1)
            # set the default option
            popup_menu.config(width=menu_width)
            tk.Checkbutton(self, text='autoscale', variable=self.autoscale, onvalue=1, offvalue=0, command=autoscale_cb_changed) \
                .grid(column=10, row=9, padx=10, pady=0)

            def change_dropdown(*args):
                pass
                # print(self.dropdown_value.get())

            # link function to change dropdown
            self.dropdown_value.trace('w', change_dropdown)

        def length_slider_changed(passed_value):
            self.length.set(round(float(passed_value), 1))
            update_data()
            update_plot1()

        def length_spinbox_changed():
            self.length.set(round(self.length.get(), 1))
            update_data()
            update_plot1()

        def mass_slider_changed(passed_value):
            self.mass.set(round(float(passed_value), 1))
            update_data()
            update_plot1()

        def mass_spinbox_changed():
            self.mass.set(round(self.mass.get(), 1))
            update_data()
            update_plot1()

        def gravity_slider_changed(passed_value):
            self.gravity.set(round(float(passed_value), 1))
            update_data()
            update_plot1()

        def gravity_spinbox_changed():
            self.gravity.set(round(self.gravity.get(), 1))
            update_data()
            update_plot1()

        def initial_angle_slider_changed(passed_value):
            self.initial_angle_deg.set(round(float(passed_value), 1))
            self.theta_0 = math.radians(self.initial_angle_deg.get())
            update_data()
            update_plot1()

        def initial_angle_spinbox_changed():
            self.initial_angle_deg.set(round(self.initial_angle_deg.get(), 1))
            update_data()
            update_plot1()

        def initial_velocity_slider_changed(passed_value):
            self.initial_velocity.set(round(float(passed_value), 1))
            update_data()
            update_plot1()

        def initial_velocity_spinbox_changed():
            self.initial_velocity.set(round(self.initial_velocity.get(), 1))
            update_data()
            update_plot1()

        def damping_slider_changed(passed_value):
            self.damping.set(round(float(passed_value), 1))
            update_data()
            update_plot1()

        def damping_spinbox_changed():
            self.damping.set(round(self.damping.get(), 1))
            update_data()
            update_plot1()

        def force_amplitude_slider_changed(passed_value):
            self.force_amplitude.set(round(float(passed_value), 1))
            update_data()
            update_plot1()

        def force_amplitude_spinbox_changed():
            self.force_amplitude.set(round(self.force_amplitude.get(), 1))
            update_data()
            update_plot1()

        def force_frequency_slider_changed(passed_value):
            self.force_frequency.set(round(float(passed_value), 1))
            update_data()
            update_plot1()

        def force_frequency_spinbox_changed():
            self.force_frequency.set(round(self.force_frequency.get(), 1))
            update_data()
            update_plot1()

        def time_step_slider_changed(passed_value):
            self.time_step.set(round(float(passed_value), 2))
            update_data()
            update_plot1()

        def time_step_spinbox_changed():
            self.time_step.set(round(self.time_step.get(), 2))
            update_data()
            update_plot1()

        def time_rate_slider_changed(passed_value):
            self.time_rate.set(round(float(passed_value), 2))
            update_data()
            update_plot1()

        def time_rate_spinbox_changed():
            self.time_rate.set(round(self.time_rate.get(), 2))
            update_data()
            update_plot1()

        def popup_menu_changed(passed_value):
            update_data()
            update_plot1()

        def autoscale_cb_changed():
            update_data()
            update_plot1()

        def show_animation():
            update_data()
            update_plot()

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
                temp_list.append((self.t, i_theta, v_0))
            return temp_list

        create_widgets()
        plot_figure_1()
        plot_figure_2()
        plot_figure_3()

        # UPDATE DATA AND UPDATE PLOT
        def update_data():
            if self.dropdown_value.get() == 'Small angles':
                self.theta = self.theta_0 * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)
            elif self.dropdown_value.get() == 'Euler':
                euler_list = euler_array(self.initial_velocity.get(), self.theta_0, self.t_initial, self.t_stop)
                t = [x[0] for x in euler_list]
                self.theta = [x[1] for x in euler_list]
            elif self.dropdown_value.get() == 'Improved Euler':
                self.theta = self.theta_0 * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)
            elif self.dropdown_value.get() == 'RK4':
                self.theta = self.theta_0 * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)
            else:
                self.theta = self.theta_0 * np.cos(np.sqrt(self.gravity.get() / self.length.get()) * self.t)

        def update_plot1():

            if self.autoscale.get() == 0:
                ax1_lim = ((min(self.t), min(self.theta)), (max(self.t), max(self.theta)))
                self.ax1.update_datalim(ax1_lim)
            else:
                self.ax1.relim()
            self.ax1.autoscale(enable=True, axis="y", tight=True)
            self.canvas1.draw()
            plt.ion()
            self.line1.set_data(self.t, self.theta)

        def update_plot():
            time.sleep(1)
            plot_figure_2()
            plot_figure_3()


