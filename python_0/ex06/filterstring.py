import sys


def main():
    """
    Outputs a list of words from the input string that have a
    length greater than the input integer.

    Args:
        arg1 (str): a string
        arg2 (int): an integer

    Return:
        None
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        S: str = sys.argv[1]
        try:
            N: int = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        # if not isinstance(S, str):
        #     raise AssertionError("the arguments are bad")

        words = S.split()
        filtered_words = [
            word for word in words
            if (lambda w, threshold: len(w) > threshold)(word, N)
        ]
        print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    # print(main.__doc__)
