import sys

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided")
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()
