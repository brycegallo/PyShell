import os


def shell_loop():
    while True:
        current_directory = os.getcwd()
        command = input("/" + current_directory.split("/")[-1] + " $ ")
        if command == "quit" or command == "exit":
            break
        elif command == "pwd":
            print(current_directory)
        elif command == "ls":
            ls_process(current_directory)
        elif command == "helpme":
            helpme()
        else:
            print(command)


def ls_process(current_directory):
    ls_list = os.listdir(current_directory)
    ls_output = ""
    for item in ls_list:
        ls_output += (item + " ")
    print(ls_output)


def helpme():
    print("available commands currently include: 'ls', 'pwd', 'quit', 'exit'")
