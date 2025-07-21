def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Takes two lists of integer or float and calculates the BMI.
    Both lists must be the same length.

    Args:
        arg1 (list): List of heights as integers or floats.
        arg2 (list): List of weights as integers or floats.

    Returns:
        List of calculated BMIs.
    """
    try:
        if len(height) != len(weight):
            raise AssertionError("arguments are not the same size.")

        bmi_values = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) \
                    or not isinstance(w, (int, float)):
                raise AssertionError("lists must contain int or float only.")
            if h <= 0 or w <= 0:
                raise AssertionError("lists values must be positive.")
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
    except AssertionError as e:
        print(f"AssertionError: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Takes a list of integers or floats and an integer representing
    the limit.
    Returns a list of booleans (True if above the limit).

    Args:
        arg1 (list): List of integers or floats.
        arg2 (int): Integer representing the limit.

    Returns:
        List of booleans.
    """
    try:
        if type(limit) is not int:
            raise AssertionError("limit must be an int.")
        above_limit = []
        for x in bmi:
            if not isinstance(x, (int, float)):
                raise AssertionError("list must contain int or float only.")
            if x > limit:
                above_limit.append(True)
            else:
                above_limit.append(False)
        return above_limit
    except AssertionError as e:
        print(f"AssertionError: {e}")

# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
