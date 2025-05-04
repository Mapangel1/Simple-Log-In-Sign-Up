import json
import os
file_name = "USER&PASSLOGS.json"
caccolacc = input("Type 1 to Create an account. Type 2 login to your account. Press Enter to continue: ")
if caccolacc == "1":
    username = input("Create a username: ")
    password = input("Create a password: ")
    with open(file_name, "r") as file:
        data = json.load(file)
    if username in data:
        print("Username already exists. Please choose a different username.")
    else:
        data[username] = password
        with open(file_name, "w") as file:
            json.dump(data, file)
        print("Account created successfully!")
        input("Press Enter to continue...")
elif caccolacc == "2":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open(file_name, "r") as file:
        data = json.load(file)
    if username in data and data[username] == password:
        print("Login successful!")
        input("Press Enter to continue...")
    else:
        print("Invalid username or password.")
        input("Press Enter to continue...")

