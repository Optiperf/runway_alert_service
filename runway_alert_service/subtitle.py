import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re

def clean_line(line):
    # Remove all HTML-like tags (e.g., <i>, </i>, <b>, etc.)
    return re.sub(r'<[^>]+>', '', line)

def srt_to_text(srt_file, txt_file, encoding):
    with open(srt_file, "r", encoding=encoding) as f:
        lines = f.readlines()

    text_lines = []
    for line in lines:
        line = line.strip()
        if line.isdigit():
            continue
        if "-->" in line:
            continue
        if not line:
            continue
        cleaned = clean_line(line)
        if cleaned:
            text_lines.append(cleaned)

    with open(txt_file, "w", encoding=encoding) as f:
        f.write("\n".join(text_lines))

def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("SRT files", "*.srt"), ("All files", "*.*")]
    )
    if file_path:
        srt_path_var.set(file_path)

def convert():
    srt_file = srt_path_var.get()
    encoding = encoding_var.get()
    if not srt_file:
        messagebox.showerror("Error", "Please select an SRT file.")
        return
    try:
        folder = os.path.dirname(srt_file)
        output_file = os.path.join(folder, "output.txt")
        srt_to_text(srt_file, output_file, encoding)
        messagebox.showinfo("Success", f"output.txt created in:\n{folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed: {e}")

root = tk.Tk()
root.title("SRT to Text Converter")
root.geometry("400x180")
root.resizable(False, False)

srt_path_var = tk.StringVar()
encoding_var = tk.StringVar(value="utf-8")
encodings = ["utf-8", "utf-16", "latin-1"]

tk.Label(root, text="Select SRT file:").pack(pady=(15, 0))
frame = tk.Frame(root)
frame.pack()
tk.Entry(frame, textvariable=srt_path_var, width=35).pack(side=tk.LEFT, padx=(0, 5))
tk.Button(frame, text="Browse", command=browse_file).pack(side=tk.LEFT)

tk.Label(root, text="Select encoding:").pack(pady=(10, 0))
tk.OptionMenu(root, encoding_var, *encodings).pack()

tk.Button(root, text="Convert", command=convert, width=15).pack(pady=15)

root.mainloop()