import os


def shell_loop():
    while True:
        current_directory = os.getcwd()
        command = input("/" + current_directory.split("/")[-1] + " $ ")
        if command == "quit" or command == "exit":
            break
        elif command == "pwd":
            print(current_directory)
        else:
            print(command)