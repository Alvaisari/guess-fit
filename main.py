import tkinter as tk
import sv_ttk
from app import FitApp


if __name__ == "__main__":
    root = tk.Tk()
    app = FitApp(root)
    sv_ttk.set_theme("light")
    root.mainloop()
