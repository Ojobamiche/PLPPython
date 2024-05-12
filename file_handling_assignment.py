with open("my_file.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("42\n")
    file.write("Hello, World!\n")

    with open("my_file.txt", "a") as file:
        file.write("This is line 4\n")
        file.write("Another line added\n")
        file.write("Last line appended\n")

try:
    with open("my_missing_file.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Error handling completed.")