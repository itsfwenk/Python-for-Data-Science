import numpy as np
import sys


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based
    on the provided start and end arguments.

    Args:
        arg1 (list): A 2D array.
        arg2 (int): Indicates the start of the truncation.
        arg3 (int): Indicates the end of the truncation.

    Returns:
        Desired truncated list.
    """
    try:
        if not isinstance(family, list):
            raise AssertionError("first argument must be a list.")
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("start and end must be integers.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("lists must all be the same size.")
        
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end].shape}")
        return np.array(family)[start:end].tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)