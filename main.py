import sys
import core


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        exit(1)
    with open(sys.argv[1], 'rb') as f:
        data = f.read()
        core.VM(data).run()


if __name__ == "__main__":
    main()

