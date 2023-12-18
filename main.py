import subprocess

def main():
    while True:
        command = input("$ ")
        if command == "quit":
            break
        else:
            print(command)


if __name__ == '__main__':
    main()

