# 🔍 String Finder Script

A simple Python script that **searches for a specific string inside all files** in a given directory (including subdirectories).

✅ It will scan every file in the folder  
✅ It will check if the file contains the target string  
✅ If the string is found, it will print the file path

---

## 📄 Example use case:

Let's say you have a folder full of text files, and you want to know **which file contains a specific keyword or phrase.**  
This script will automatically search all files and tell you where it was found.

---

## 🚀 How it works:

1. You specify:
   - The directory path (in `DIRECTORY`)
   - The string to search for (in `FIND_STRING`)
2. The script goes through every file
3. If the string is found → it prints the file name

---

## 📝 Configuration:

Edit these two variables inside the script:

```python
DIRECTORY = r"C:\path\to\your\folder"
FIND_STRING = "your_search_string"
