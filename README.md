<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e3c72,100:2a5298&height=250&section=header&text=Smart%20File%20Organizer&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Python%20+%20Streamlit%20Based%20Automation%20Project&descAlignY=58&descSize=18" width="100%" />

# 📂 Smart File Organizer

A simple yet powerful **Smart File Organizer** built using **Python & Streamlit** to automatically organize messy folders into structured categories.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

# 🚀 Overview

> A Streamlit-powered file automation tool that helps organize files, detect duplicates, and maintain clean folder structures.

### ✅ Highlights

* Organizes files automatically by category
* Detects duplicate files using MD5 hashing
* Undo functionality for recovery
* Dry Run mode for previewing actions
* Beginner-friendly interface

---

# ✨ Features

* 📁 Automatic file organization
* 🖼️ Sort Images, PDFs, Videos, and Documents
* 🗑️ Duplicate file detection
* 🔄 Undo previous operations
* 🔍 Dry Run mode
* ⚡ Clean and interactive Streamlit UI

---

# 🛠️ Tech Stack

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Core programming language  |
| Streamlit  | User interface             |
| OS Module  | File and folder operations |
| Shutil     | File movement              |
| Hashlib    | Duplicate detection        |

---

# 📂 Project Structure

```text
Smart-File-Organizer/
│
├── app.py                # Main Streamlit application
├── file_organizer.py     # File organization logic
├── undo_log.txt          # Undo operation history
├── activity.log          # Activity tracking
└── README.md             # Documentation
```

---

# ⚙️ How It Works

1. Enter the folder path.
2. Select organization options.
3. Choose category type.
4. Click **Organize Files**.
5. Files are sorted into folders automatically.

---

# 📌 Example

### Before Organization

```text
Downloads/
├── image1.jpg
├── report.pdf
├── movie.mp4
├── notes.docx
```

### After Organization

```text
Downloads/
├── Images/
│   └── image1.jpg
├── PDFs/
│   └── report.pdf
├── Videos/
│   └── movie.mp4
├── WordDoc/
│   └── notes.docx
```

---

# ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/bhargavi-insights/file_organization.git
cd file_organization
```

### Install Dependencies

```bash
pip install streamlit
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

Open in browser:

```text
http://localhost:8501
```

---

# 🧠 Core Functionalities

### 🔍 Dry Run Mode

Preview actions before organizing files.

### 🗑️ Duplicate Detection

Uses MD5 hashing to detect identical files.

### 🔄 Undo Feature

Restore previous file locations instantly.

---

🖼️ Preview

<p align="center">
  <img width="1895" height="1024" alt="Screenshot 2026-04-23 191712" src="https://github.com/user-attachments/assets/004946bc-e187-4edc-923f-c04ce4eadd67" />
  <img width="1908" height="1035" alt="Screenshot 2026-04-10 162417" src="" />
  <img width="1912" height="1036" alt="Screenshot 2026-04-10 162445" src="" />
</p>

# 🔮 Future Enhancements

* Drag & Drop folder selection
* Progress tracking
* Custom categories
* Activity export
* Advanced dashboard UI

---

# 💼 Learning Outcomes

This project demonstrates:

* Python file handling
* Folder automation
* Duplicate detection logic
* Streamlit UI creation
* GitHub project publishing

---

# 👩‍💻 Author

**Bhargavi Tare**

GitHub: [https://github.com/bhargavi-insights](https://github.com/bhargavi-insights)

---


## ⭐ Support

If you like this project:

- ⭐ Star the repo
- 🍴 Fork it
- 🚀 Share it

---

