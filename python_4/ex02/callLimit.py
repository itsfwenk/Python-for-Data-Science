def callLimit(limit: int):
    """
    A decorator factory that creates a decorator to limit the number
    of times a function can be called.

    Args:
        limit (int): The maximum number of calls allowed
        for the decorated function.

    Returns:
        Callable: The decorator function, 'callLimiter'.
    """
    count = 0

    def callLimiter(function):
        """
        The actual decorator that wraps the target function.

        Args:
            function (Callable): The function to be decorated.

        Returns:
            Callable: The new wrapper function, 'limit_function'.
        """
        def limit_function(*args: any, **kwds: any):
            """
            The wrapper function that enforces the call limit.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: '{function}' call too many times")
                return None
        return limit_function
    return callLimiter