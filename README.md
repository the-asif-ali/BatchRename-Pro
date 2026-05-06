# 📂✨ BatchRename Pro

A simple yet powerful Python script to rename multiple files in a folder with ease. Whether you're organizing images, documents, or any other files, **BatchRename Pro** helps you do it in seconds ⚡

---

## 🚀 Features

* 🔍 Select any folder on your system
* 🧩 Filter files by extension (e.g., `.jpg`, `.png`, `.txt`)
* ✏️ Rename files with a custom base name
* 🔢 Automatic numbering for clean organization
* ⚡ Fast and lightweight — no external libraries required

---

## 🛠️ How It Works

1. You provide the folder path 📁
2. Specify the file extension you want to rename 🔎
3. Enter a new base name ✏️
4. The script renames all matching files in sequence:

```
example_1.jpg
example_2.jpg
example_3.jpg
...
```

---

## 💻 Usage

### ▶️ Run the Script

```bash
python your_script_name.py
```

### 🧾 Input Prompts

* **Enter Folder Path :** Path to your target directory
* **Enter File Extension :** File type (e.g., `.jpg`)
* **Enter the new name :** Desired base name

---

## 📌 Example

**Input:**

```
Folder: C:/Images
Extension: .png
New Name: holiday
```

**Output:**

```
holiday_1.png
holiday_2.png
holiday_3.png
...
```

---

## ⚠️ Important Notes

* 🚨 Make sure the folder path is correct
* 🔁 Existing files with the same name may be overwritten
* 📂 Currently renames *all files in the folder*, not just filtered ones (can be improved)

---

## 🔧 Possible Improvements

* ✅ Rename only filtered files (fix loop logic)
* 🔄 Add preview mode before renaming
* 📊 Add sorting options (by date, size, etc.)
* 🖥️ Build a GUI for easier interaction

---

## 👨‍💻 Author

**Asif Ali** ✨

---

## 🤝 Contributing

Feel free to improve this script and make it even more powerful! 💡
Pull requests and ideas are always welcome.

---

## 📜 License

This project is open-source and free to use 🎉

---

## ❤️ Made With Python

Keep coding and keep building! 🚀
