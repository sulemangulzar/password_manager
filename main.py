import random
import string


# Suggest a strong password
def suggest_pass():
    user_length_input = input("Enter Length Of Password: ")
    try:
        pass_length = int(user_length_input)
    except ValueError:
        print("❌ Please enter a valid number.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(pass_length))
    print("Suggested password:", password)
    return password


# Check if created password is valid
def create_pass(user_password):
    messages = []

    if len(user_password) < 8:
        messages.append("❌ Must be at least 8 characters long.")
    if not any(char in string.ascii_lowercase for char in user_password):
        messages.append("❌ Must include at least one lowercase letter (a-z).")
    if not any(char in string.ascii_uppercase for char in user_password):
        messages.append("❌ Must include at least one uppercase letter (A-Z).")
    if not any(char in string.digits for char in user_password):
        messages.append("❌ Must include at least one digit (0-9).")
    if not any(char in string.punctuation for char in user_password):
        messages.append(
            "❌ Must include at least one special character (!@#$%^&* etc)."
        )

    if not messages:
        return True, ["✅ Password is strong!"]
    else:
        return False, messages


# Save password to file
def save_password(password):
    app_name = input("Enter App Name: ")
    updated = False

    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    new_lines = []
    app_found = False

    for line in lines:
        if line.lower().startswith(app_name.lower() + ":"):
            app_found = True
            print("⚠️ This app already exists in your saved passwords.")
            choice = input("1 - Replace Password \n2 - Rename \n3 - Exit: ")

            if choice == "1":
                new_lines.append(f"{app_name}: {password}\n")
                updated = True
            elif choice == "2":
                rename_save_app = input("Rename The App: ")
                # Check if renamed app already exists
                if any(
                    l.lower().startswith(rename_save_app.lower() + ":") for l in lines
                ):
                    print("❌ That renamed app already exists.")
                    new_lines.append(line)  # Keep the original line
                else:
                    new_lines.append(line)  # Keep the original line too
                    new_lines.append(f"{rename_save_app}: {password}\n")
                    updated = True
            else:
                new_lines.append(line)  # Keep the original line
                print("❌ Operation cancelled.")
            break  # Exit loop after handling the match
        else:
            new_lines.append(line)

    # If app wasn't found at all, just append it
    if not app_found:
        new_lines.append(f"{app_name}: {password}\n")
        print("✅ Password saved.")
    elif updated:
        print("✅ Password updated.")

    with open("passwords.txt", "w") as f:
        f.writelines(new_lines)


def delete_password():
    del_pass_input = input(
        "Enter the name of the app you want to delete the password for: "
    )

    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("❌ No saved passwords found.")
        return

    found = False
    new_lines = []

    for line in lines:
        if line.lower().startswith(del_pass_input.lower() + ":"):
            print(f"⚠️ Found: {line.strip()}")
            confirm = input("1 - Confirm Delete\n2 - Exit: ")
            if confirm == "1":
                print("✅ Password deleted.")
                found = True
                continue
        new_lines.append(line)

    if not found:
        print("❌ App not found.")

    with open("passwords.txt", "w") as f:
        f.writelines(new_lines)


def view_password():
    view_pass_input = input(
        "Enter the name of the app you want to view the password for: "
    )

    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("❌ No saved passwords found.")
        return

    found = False
    for line in lines:
        if line.lower().startswith(view_pass_input.lower() + ":"):
            print(f"🔐 Found: {line.strip()}")
            found = True
            break

    if not found:
        print("❌ App not found.")


# --- Main program ---
create_or_suggest_or_del = int(
    input(
        "Enter \n 1 - Suggest Password \n 2 - Create Password \n 3 - Delete Password \n 4 - View Password: "
    )
)

if create_or_suggest_or_del == 1:
    suggested_password = suggest_pass()
    if suggested_password:
        save_or_not = input("1 - Save Password \n2 - No: ")
        if save_or_not == "1":
            save_password(suggested_password)

elif create_or_suggest_or_del == 2:
    user_password = input("Enter your password: ")
    valid, messages = create_pass(user_password)
    for msg in messages:
        print(msg)
    if valid:
        save_or_not = input("1 - Save Password \n2 - No: ")
        if save_or_not == "1":
            save_password(user_password)

elif create_or_suggest_or_del == 3:
    delete_password()

elif create_or_suggest_or_del == 4:
    view_password()
else:
    print("❌ Invalid choice.")
