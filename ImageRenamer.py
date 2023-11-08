import os
import tkinter as tk
from tkinter import filedialog

# Updated list of supported file formats
predefined_formats = ['jpg', 'png', 'jpeg', 'gif', 'webp', 'mp4', 'mkv', 'mp3', 'txt', 'docx', 'pdf', 'exe', 'zip']

def rename_images(selected_folder, prefix, suffix, selected_formats):
    for root, dirs, files in os.walk(selected_folder):
        for i, f in enumerate(files):
            absname = os.path.join(root, f)
            img_type = f.split('.')[-1]

            if img_type in selected_formats:
                new_name = str(i + 1)
                if prefix:
                    new_name = f'{prefix}_{new_name}'
                if suffix:
                    new_name = f'{new_name}_{suffix}'
                new_name = os.path.join(root, f'{new_name}.{img_type}')
                os.rename(absname, new_name)

def select_folder():
    folder_path = filedialog.askdirectory(title="Select a folder containing images")
    if folder_path:
        selected_folder_label.config(text=folder_path)

def rename_button_clicked():
    prefix = prefix_entry.get()
    suffix = suffix_entry.get()
    selected_folder = selected_folder_label.cget("text")
    selected_formats = [format for format, var in format_var.items() if var.get()]
    
    custom_format = custom_format_entry.get()
    
    # If a custom format is specified, process it
    if custom_format:
        custom_formats = custom_format.replace(" ", "").split(';')
        selected_formats.extend([format.strip('.') for format in custom_formats])
    
    if selected_folder and any(selected_formats):
        rename_images(selected_folder, prefix, suffix, selected_formats)
        result_label.config(text="Images renamed successfully!")

# Create the main application window
app = tk.Tk()
app.title("Image Renamer")

# Create and configure the main frame
frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

# Create and configure the user interface elements
title_label = tk.Label(frame, text="Image Renamer", font=("Helvetica", 16))
title_label.pack(pady=10)

select_folder_button = tk.Button(frame, text="Select Folder", command=select_folder)
select_folder_button.pack(pady=(0, 5))

selected_folder_label = tk.Label(frame, text="", wraplength=300)
selected_folder_label.pack(pady=10)

prefix_label = tk.Label(frame, text="Prefix:")
prefix_label.pack(pady=5)
prefix_entry = tk.Entry(frame)
prefix_entry.pack(pady=5)

suffix_label = tk.Label(frame, text="Suffix:")
suffix_label.pack(pady=5)
suffix_entry = tk.Entry(frame)
suffix_entry.pack(pady=5)

# Create a frame for file format selection
format_frame = tk.Frame(frame)
format_frame.pack(pady=10)

format_label = tk.Label(format_frame, text="Select File Formats:")
format_label.pack()

# Create checkboxes for predefined file formats
format_var = {format: tk.BooleanVar() for format in predefined_formats}
format_checkboxes = {format: tk.Checkbutton(format_frame, text=f'.{format}', variable=format_var[format]) for format in predefined_formats}

for checkbox in format_checkboxes.values():
    checkbox.pack(side='left', padx=5)

# Custom Format Entry
custom_format_label = tk.Label(frame, text="Custom Format:")
custom_format_label.pack(pady=5)
custom_format_entry = tk.Entry(frame)
custom_format_entry.pack(pady=5)

# Rename button
rename_button = tk.Button(frame, text="Rename", command=rename_button_clicked)
rename_button.pack(pady=10)

result_label = tk.Label(frame, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
