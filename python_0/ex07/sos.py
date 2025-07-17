import sys


def main():
    """
    Takes a string as an argument and encodes it into
    Morse Code.

    Args:
        arg1 (str) : a string

    Return:
        None
    """

    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        input_string = sys.argv[1]

        # if not isinstance(input_string, str):
        #     raise AssertionError("the arguments are bad")
        for char in input_string:
            if not (char.isalnum() or char.isspace()):
                raise AssertionError("the arguments are bad")

        morse_code_parts = []

        for char in input_string:
            upper_char = char.upper()
            morse_code_parts.append(MORSE_CODE_DICT[upper_char])

        print(" ".join(morse_code_parts))

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
