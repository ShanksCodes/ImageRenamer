import os
import tkinter as tk
from tkinter import filedialog

img_types = ['jpg', 'png', 'jpeg']

def rename_images(selected_folder):
    for root, dirs, files in os.walk(selected_folder):
        for i, f in enumerate(files):
            absname = os.path.join(root, f)
            img_type = absname.split('.')[-1]

            if img_type in img_types:
                newname = os.path.join(root, '{}.{}'.format(i, img_type))
                os.rename(absname, newname)

def select_folder():
    folder_path = filedialog.askdirectory(title="Select a folder containing images")
    if folder_path:
        rename_images(folder_path)
        result_label.config(text="Images renamed successfully!")

# Create the main application window
app = tk.Tk()
app.title("Image Renamer")

# Create and configure the main frame
frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

# Create and configure the user interface elements
title_label = tk.Label(frame, text="Image Renamer")
title_label.pack()

select_button = tk.Button(frame, text="Select Folder", command=select_folder)
select_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

# Start the Tkinter event loop
app.mainloop()
