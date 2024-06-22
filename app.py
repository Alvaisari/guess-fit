import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from signal_utils import generate_signal, gauss

plt.style.use("ggplot")


class FitApp:
    """Tkinter-based application window"""

    def __init__(self, root):
        self.root = root
        self.root.title("Guess Fit App")

        # Create a frame for the matplotlib figure
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)

        # Get init raw signal
        self.canvas = None
        self.dots = []
        self.x, self.y, self.peaks, self.baseline = generate_signal()
        self.true_y = np.sum(self.peaks, axis=0)

        # Show widgets and the first figure
        self.create_widgets()
        self.plot_signal()

    def create_widgets(self):
        """Adds buttons and figure widget"""
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.X)

        new_button = ttk.Button(
            button_frame, text="New signal", command=self.new_signal
        )
        new_button.pack(side=tk.LEFT, padx=5, pady=5)

        reset_button = ttk.Button(button_frame, text="Reset", command=self.reset_dots)
        reset_button.pack(side=tk.LEFT, padx=5, pady=5)

        fit_button = ttk.Button(button_frame, text="Fit", command=self.fit_signal)
        fit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.figure, self.ax = plt.subplots(figsize=(10, 5))
        self.figure.canvas.mpl_connect("button_press_event", self.on_click)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

    def plot_signal(self):
        """Updates figure widgets if something pressed"""
        self.ax.clear()
        self.ax.scatter(self.x, self.y, label="Signal", s=10)
        for dot in self.dots:
            self.ax.plot(dot[0], dot[1], marker="$\U0001F610$", ms=30, color="black")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Intensity")
        self.ax.set_title("Generated signal")
        self.ax.legend()
        self.canvas.draw()

    def new_signal(self):
        """Adds new signal"""
        # New random signal
        self.x, self.y, self.peaks, self.baseline = generate_signal()
        # Update True signal
        self.true_y = np.sum(self.peaks, axis=0)
        # Drop dots and call update figure
        self.dots = []
        self.plot_signal()

    def reset_dots(self):
        """Removes added dots from the figure"""
        self.dots = []
        self.plot_signal()

    def on_click(self, event):
        """Adds points in a figure on click"""
        if event.inaxes:
            self.dots.append((event.xdata, event.ydata))
            self.plot_signal()

    def fit_signal(self):
        """Fits the signal and draw result"""
        # In case no dots added does nothing
        if len(self.dots) == 0:
            return

        # Initial guess for linear background
        initial_guess = [0, 0]
        for dot in self.dots:
            initial_guess += [dot[1], dot[0], 1]

        # Fit the raw curve using dots added by user as a initial guess
        popt, _ = curve_fit(gauss, self.x, self.y, p0=initial_guess)

        # Restore the signal from fitted parameters
        y_fit = gauss(self.x, *popt)

        # Plot results
        for peak in self.peaks:
            self.ax.plot(
                self.x, peak, linestyle="--", linewidth=2, color="black", label=None
            )
        self.ax.plot(
            self.x,
            self.true_y + self.baseline,
            label="True signal",
            linewidth=2,
            linestyle="--",
            color="black",
        )
        self.ax.plot(self.x, y_fit, label="Fitted signal", linewidth=4)
        self.ax.legend()
        self.canvas.draw()
