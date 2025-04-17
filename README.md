
# 🧾 Certificate Generator GUI App

A modern and intuitive GUI application to **automatically generate personalized certificates** from a CSV file and a certificate template image.

This app is perfect for:
- 🏫 Schools and colleges
- 🏆 Event organizers
- 🧑‍🏫 Trainers and educators
- 🧑‍💻 Hackathon or coding event teams

Built using Python and `customtkinter`, it provides a sleek UI with real-time progress updates and customizable input/output options.

---

## 🚀 Features

- 📄 Input via CSV (name list)
- 🖼️ Custom PNG template support
- 💾 Select output folder for generated certificates
- 🌗 Light and dark theme friendly
- 📈 Real-time progress bar
- 👁️ Sample output preview
- 🛠️ Easy to use interface
- ✅ Built with `customtkinter`, `PIL`, and `pandas`

---

## 🖼️ App Screenshots

| Initial Screen (Before Generation) | Final Screen (After Generation) |
|-----------------------------------|----------------------------------|
| ![UI Input](assets/ui_input.png)  | ![UI Output](assets/ui_output.png) |

> 📝 Rename and place your images:
> - `Screenshot from 2025-04-17 17-05-58.png` → `assets/ui_input.png`
> - `Screenshot from 2025-04-17 17-05-26.png` → `assets/ui_output.png`

---

## 📁 Project Structure

```
CertificateGenerator/
│
├── assets/
│   ├── ui_input.png            # Input screen screenshot
│   └── ui_output.png           # Output screen screenshot
│
├── templates/
│   └── sample.png              # Sample certificate template
│
├── sample.csv                  # Sample CSV with names
├── main.py                     # Main Python GUI script
├── requirements.txt            # Dependencies
└── README.md                   # You're reading it!
```

---

## 🧰 Installation

### 🔗 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/certificate-generator.git
cd certificate-generator
```

### 📦 Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

> ✅ Tested with **Python 3.9+**

---

## 📋 How to Use

### Step 1: Prepare Your CSV File

Your CSV must have the following structure:

```csv
Name
Rakesh Kundu
Tina Sharma
Alex Roy
```

> Make sure the column header is `Name` (case-sensitive).

---

### Step 2: Choose a Template Image

Use a **.png** image as the certificate template. The app will place the name text at a predefined location on the image.

---

### Step 3: Run the App

```bash
python main.py
```

### Step 4: In the App GUI

1. Click **Browse** next to **CSV File** → select your `.csv` file.
2. Click **Browse** next to **Template File** → select your `.png` certificate template.
3. Click **Browse** next to **Output Folder** → choose the folder where you want to save the certificates.
4. Click **Generate Certificates** → Watch the progress bar fill up!
5. Optionally, click **Sample Output** to preview a sample certificate.

---

## 📤 Output

Each certificate will be saved in the selected output folder with the recipient's name in the filename, for example:

```
Certificates/
├── Rakesh Kundu.png
├── Tina Sharma.png
└── Alex Roy.png
```

---

## 📚 Documentation & Help

- 📘 **Docs**: This README serves as the complete guide.
- 🌐 **Connect**: [GitHub - Rakesh Kundu (Pinaka)](https://github.com/rax-2)

---

## 👨‍💻 About the Creator

**Developed by:** Rakesh Kundu  
🎓 ECE Student @ Abacus Institute of Engineering and Management  
💡 Founder of YantraYodha Hardware & Coding Club

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 📌 Version

**v1.0.0** – Initial release with all core features.
