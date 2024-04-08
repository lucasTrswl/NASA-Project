import tkinter as tk
from tkinter import ttk

def start_progress(parent_frame, color):
    style = ttk.Style()
    style.configure("custom.Horizontal.TProgressbar", troughcolor="#000", background=color)  # Change color here
    progress_bar = ttk.Progressbar(parent_frame, style="custom.Horizontal.TProgressbar", orient='horizontal', mode='determinate', length=200)
    progress_bar.pack(pady=10)
    return progress_bar

def update_progress(progress_bar, value):
    progress_bar['value'] = value

def stop_progress(progress_bar):
    progress_bar.destroy()

