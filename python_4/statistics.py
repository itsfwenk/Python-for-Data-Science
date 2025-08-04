def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Take in *args a quantity of unknown number and
    calculates the Mean, Median, Quartile (25% and 75%),
    Standard Deviation and Variance according to the **kwargs
    """

    data = [arg for arg in args if isinstance(arg, (int, float))]
    if not data:
        for value in kwargs.items():
            print("ERROR")
        return

    data.sort()
    n = len(data)

    results = {}
    for key in kwargs.values():
        if key == 'mean':
            if n > 0:
                mean = sum(data) / n
                results['mean'] = mean
            else:
                results['mean'] = None

        elif key == 'median':
            if n % 2 == 1:
                median = float(data[n // 2])
            else:
                median = (data[n // 2 - 1] + data[n // 2]) / 2.0
            results['median'] = median

        elif key == 'quartile':
            # q1_index = int(n * 0.25)
            # q3_index = int(n * 0.75)

            if (n-1) * 0.25 % 1 == 0:
                q1 = float(data[int((n-1) * 0.25)])
            else:
                lower = data[int(0.25 * (n-1))]
                upper = data[int(0.25 * (n-1)) + 1]
                q1 = lower + (upper - lower) * (0.25 * (n-1) % 1)

            if (n-1) * 0.75 % 1 == 0:
                q3 = float(data[int((n-1)*0.75)])
            else:
                lower = data[int(0.75 * (n-1))]
                upper = data[int(0.75 * (n-1)) + 1]
                q3 = lower + (upper - lower) * (0.75 * (n-1) % 1)

            results['quartile'] = [q1, q3]

        elif key == 'std':
            if n > 1:
                mean = sum(data) / n
                variance = sum((x - mean) ** 2 for x in data) / n
                std_dev = variance ** 0.5
                results['std'] = std_dev
            else:
                results['std'] = None

        elif key == 'var':
            if n > 0:
                mean = sum(data) / n
                variance = sum((x - mean) ** 2 for x in data) / n
                results['var'] = variance
            else:
                results['var'] = None

        else:
            pass

    for key, value in results.items():
        print(f"  {key} : {value}")