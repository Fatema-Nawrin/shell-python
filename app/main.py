import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    input()
    cmd = input()

    sys.stdout.write(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
