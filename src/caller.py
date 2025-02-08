import sys


def main(arg1):
    """
    This is the main function that takes two arguments.
    """
    print(f"Argument 1: {arg1}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide two arguments.")
