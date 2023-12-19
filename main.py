import subprocess
import os

def main():
    while True:
        current_directory = os.getcwd()
        command = input("/" + current_directory.split("/")[-1] + " $ ")
        if command == "quit":
            break
        if command == "pwd":
            print(current_directory)
        else:
            print(command)


if __name__ == '__main__':
    main()

