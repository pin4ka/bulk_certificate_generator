import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from csv import DictReader
from PIL import Image, ImageDraw, ImageFont
import webbrowser

# ------------------ Logic Functions ------------------ #
def dataReadFromCsv(fileName=''):
    data = []
    try:
        with open(fileName, newline='', encoding='utf-8') as csvfile:
            dataOfFile = DictReader(csvfile)
            for row in dataOfFile:
                name = str(row.get('NAME', '')).title().strip()
                id = str(row.get('ID', '')).strip()
                folder = str(row.get('FOLDER', '')).strip()
                data.append([name, id if id else None, folder])
        return data
    except Exception as e:
        messagebox.showerror("CSV Error", f"Couldn't read CSV file.\n\n{e}")
        return []

def cerGenerat(name, id, folder, sampleTemplate, saveDir, font_color):
    try:
        image = Image.open(sampleTemplate).convert("RGBA")
        drawingObj = ImageDraw.Draw(image)
        color = font_color  # Use selected font color
        font_path = './fonts/Photograph Signature.ttf'

        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")

        font = ImageFont.truetype(font_path, 70)
        image_width = image.size[0]
        bbox = drawingObj.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]
        pos = ((image_width - text_width) // 2, 276)
        drawingObj.text(pos, name, fill=color, font=font)

        folderPath = os.path.join(saveDir, folder) if folder else saveDir
        os.makedirs(folderPath, exist_ok=True)

        safe_name = name.replace(" ", "_")
        filename = f"{safe_name}_Certificate.png" if not id else f"{safe_name}_{id}_Certificate.png"
        image.save(os.path.join(folderPath, filename))
    except Exception as e:
        messagebox.showerror("Generation Error", f"Error creating certificate for {name}:\n\n{e}")

def generateCertificates():
    csvFileAddr = csv_file_var.get()
    templateFileAddr = template_file_var.get()
    outputFolderAddr = output_folder_var.get()

    if not (csvFileAddr and templateFileAddr and outputFolderAddr):
        messagebox.showwarning("Missing Input", "Please select all required files and output folder.")
        return

    font_color = selected_color.get()  # Get the selected color (either 'white' or 'black')

    data = dataReadFromCsv(csvFileAddr)
    if not data:
        return

    progress_bar["value"] = 0
    max_val = len(data)
    progress_bar["maximum"] = max_val
    root.update_idletasks()

    for i, (name, id, folder) in enumerate(data):
        cerGenerat(name, id, folder, templateFileAddr, outputFolderAddr, font_color)
        progress_bar["value"] = i + 1
        progress_label.config(text=f"Progress: {i + 1}/{max_val}")
        root.update_idletasks()

    messagebox.showinfo("Success", "🎉 Certificates generated successfully!")

def showSampleOutput():
    try:
        name = "Rakesh Kundu"
        sampleTemplate = './template/sampleoutput.png'
        image = Image.open(sampleTemplate).convert("RGBA")
        drawingObj = ImageDraw.Draw(image)
        font_color = selected_color.get()  # Get selected font color for sample output
        color = (255, 255, 255) if font_color == 'white' else (0, 0, 0)

        font_path = './fonts/Photograph Signature.ttf'
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")

        font = ImageFont.truetype(font_path, 70)
        image_width = image.size[0]
        bbox = drawingObj.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]
        pos = ((image_width - text_width) // 2, 276)
        drawingObj.text(pos, name, fill=color, font=font)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            initialfile="sampleoutputCertificate.png",
            title="Save Sample Output As..."
        )
        if save_path:
            image.save(save_path)
            messagebox.showinfo("Saved", "Sample certificate saved successfully!")
    except Exception as e:
        messagebox.showerror("Sample Output Error", f"Couldn't generate sample output.\n\n{e}")

def cloSe():
    exit()

# ------------------ File Pickers ------------------ #
def browse_csv():
    file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file:
        csv_file_var.set(file)

def browse_template():
    file = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file:
        template_file_var.set(file)

def browse_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_folder_var.set(folder)

# ------------------ Hyperlink Functions ------------------ #
def open_docs():
    webbrowser.open_new("https://github.com/pin4ka/bulk_certificate_generator/tree/main")

def open_portfolio():
    webbrowser.open_new("https://trishul-a.github.io/portfolio")

# ------------------ GUI Setup ------------------ #
root = tk.Tk()
root.title("🎓 Certificate Generator")
root.geometry("550x460")
root.minsize(550, 460)
root.resizable(True, True)

csv_file_var = tk.StringVar()
template_file_var = tk.StringVar()
output_folder_var = tk.StringVar()

# Variable to store selected color for text
selected_color = tk.StringVar(value='white')  # Default to white

# ------------------ Style ------------------ #
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
    padding=6,
    font=("Segoe UI", 12),
    background="#4CAF50",
    foreground="white"
)

style.configure("TLabel",
    font=("Segoe UI", 10)
)

style.configure("Custom.Horizontal.TProgressbar",
    thickness=6,
    troughcolor="#f0f0f0",
    background="#00b894",
    bordercolor="#ffffff",
    lightcolor="#55efc4",
    darkcolor="#00cec9"
)

# ------------------ Navbar ------------------ #
navbar = tk.Frame(root, bg="#4CAF50", height=40)
navbar.pack(side="top", fill="x")

tk.Label(navbar, text="Created by Pinaka (Rakesh Kundu)  |  v1.0.0", bg="#4CAF50", fg="white", font=("Segoe UI", 12, "bold"))\
    .pack(side="left", padx=10)

ttk.Button(navbar, text="Sample Output", command=showSampleOutput).pack(side="right", padx=10, pady=5)

# ------------------ Content Frame ------------------ #
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True, padx=20, pady=10)

padding = {'padx': 10, 'pady': 8}

row = 0

tk.Label(content_frame, text="CSV File:").grid(row=row, column=0, sticky="e", **padding)
tk.Entry(content_frame, textvariable=csv_file_var, width=45).grid(row=row, column=1, **padding)
ttk.Button(content_frame, text="Browse", command=browse_csv).grid(row=row, column=2, **padding)

row += 1
tk.Label(content_frame, text="Template File:").grid(row=row, column=0, sticky="e", **padding)
tk.Entry(content_frame, textvariable=template_file_var, width=45).grid(row=row, column=1, **padding)
ttk.Button(content_frame, text="Browse", command=browse_template).grid(row=row, column=2, **padding)

row += 1
tk.Label(content_frame, text="Output Folder:").grid(row=row, column=0, sticky="e", **padding)
tk.Entry(content_frame, textvariable=output_folder_var, width=45).grid(row=row, column=1, **padding)
ttk.Button(content_frame, text="Browse", command=browse_output_folder).grid(row=row, column=2, **padding)

row += 1
# Radio buttons for font color selection
tk.Label(content_frame, text="Font Color:").grid(row=row, column=0, sticky="e", **padding)
radio_frame = tk.Frame(content_frame)
radio_frame.grid(row=row, column=1, columnspan=2, **padding)

ttk.Radiobutton(radio_frame, text="White", variable=selected_color, value="white").pack(side="left", padx=10)
ttk.Radiobutton(radio_frame, text="Black", variable=selected_color, value="black").pack(side="left", padx=10)

row += 1
ttk.Button(content_frame, text="Generate Certificates", command=generateCertificates).grid(
    row=row, column=0, columnspan=3, pady=20
)

row += 1
progress_bar = ttk.Progressbar(
    content_frame, orient="horizontal", length=480,
    mode="determinate", style="Custom.Horizontal.TProgressbar"
)
progress_bar.grid(row=row, column=0, columnspan=3, pady=10)
progress_label = tk.Label(content_frame, text="Progress: 0/0")
progress_label.grid(row=row + 1, column=0, columnspan=3)

# ------------------ Footer ------------------ #
footer = tk.Frame(root, bg="#4CAF50", height=40)
footer.pack(side="bottom", fill="x")

ttk.Button(footer, text="Docs", command=open_docs).pack(side="left", padx=10, pady=5)
ttk.Button(footer, text="Contact Pinaka", command=open_portfolio).pack(side="left", padx=10, pady=5)
ttk.Button(footer, text="Close", command=cloSe).pack(side="right", padx=10, pady=5)

root.mainloop()
