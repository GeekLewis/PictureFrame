import os

# Set the DISPLAY environment variable to the local display
os.environ["DISPLAY"] = ":0.0"

# Open a window using the tkinter library
import tkinter as tk
root = tk.Tk()
root.title("Hello, world!")
root.geometry("320x100")
label = tk.Label(root, text="This is a job running on the local display.")
label.pack()
root.mainloop()
