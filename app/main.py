import sys


def main():
    while True:
        sys.stdout.write("$ ")
        commands = ["echo", "exit", "type"]
        command = input().strip()
        if command == "exit 0":
            break
        elif command.startswith("echo "):
            print(command[5:])
        elif command.startswith("type "):
            name = command.split()[1]
            if name in commands:
                print(f"{name} is a shell builtin")
            else:
                print(f"{name}: command not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
