# Python File Automation

## 📌 Project Overview
This project automates the organization of files inside a folder using Python.  
It scans files, detects their extensions, and automatically moves them into
organized folders (PDFs, Images, Text).

The goal of this project is to practice **Python automation** and reduce
manual file management tasks.

---

## ⚙️ What the Script Does
- Scans a source folder (`downloads`)
- Detects file extensions
- Creates folders automatically if they don’t exist
- Moves files to the correct folder based on type

---

## 🧠 Example
Before running the script:
downloads/
├── report.pdf
├── image.png
├── notes.txt

After running the script:
downloads/
├── PDFs/
│ └── report.pdf
├── IMAGES/
│ └── image.png
├── Text/
│ └── notes.txt


---

## 🛠️ Tools & Technologies
- Python
- os module
- shutil module

---

## 🚀 How to Run the Project
1. Clone the repository
2. Create a folder named `downloads`
3. Add sample files (pdf, images, txt)
4. Run:
```bash
python main.py


