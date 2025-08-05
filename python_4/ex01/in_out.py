def square(x: int | float) -> int | float:
    """
    Calculates the square of argument.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Calculates the exponentiation of argument by itself
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Takes as argument a number and a function,
    it returns an object that when called returns
    the result of the arguments calculation.
    """
    count = 0
    def inner() -> float:
        """
        Inner function to perform the calculation
        """
        nonlocal count
        count += 1
        nonlocal x
        result = function(x)
        x = result
        # print(f"count = {count}")
        return result
    return inner
