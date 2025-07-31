# 🔐 Password Manager (Python)

This is a simple command-line Password Manager written in Python. It allows you to:

- Suggest strong passwords
- Create your own passwords with validation
- Save passwords securely (locally)
- View saved passwords
- Update or delete saved passwords

## 📁 Features

- ✅ Password strength checker
- 🔐 Random password generator (with special characters, digits, etc.)
- 💾 Save passwords with app names
- ✏️ Update or rename existing app password entries
- 👁️ View saved passwords
- 🗑️ Delete passwords by app name

## 🧠 How It Works

- The user is prompted to choose between creating a password manually or generating one.
- Manual passwords are validated to ensure they meet strength requirements:
  - At least 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number
  - At least one special character
- Passwords are saved to a local file named `passwords.txt` along with the app name.
- When saving, it checks if the app name already exists and gives options to update or rename.
- Passwords can be viewed or deleted by providing the app name.

## 🛠 Requirements

- Python 3.x

No external libraries are needed — it only uses Python’s standard library (`random`, `string`).

## 🚀 Getting Started

1. Clone this repository or copy the script file.
2. Run the Python file:

```bash
python password_manager.py
