import sys


def main():
    """
    Takes a single string argument and displays the sums of its upper-case
    characters, lower-case characters, punctuation characters, digits and
    spaces.

    Args:
        arg1 (str, optional): The first argument, a string.

    Returns:
        None
    """
    strToCount = ""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 1:
            try:
                strToCount = input("What is the text to count?\n")
                strToCount += '\n'
            except EOFError:
                pass
        elif len(sys.argv) == 2:
            strToCount = str(sys.argv[1])

        print(f"This text contains {len(strToCount)} characters:")
        n = sum(1 for char in strToCount if char.isupper())
        print(f"{n} upper letters")
        n = sum(1 for char in strToCount if char.islower())
        print(f"{n} lower letters")
        punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        n = sum(1 for char in strToCount if char in punctuations)
        print(f"{n} punctuation marks")
        n = sum(1 for char in strToCount if char.isspace())
        print(f"{n} spaces")
        n = sum(1 for char in strToCount if char.isdigit())
        print(f"{n} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
