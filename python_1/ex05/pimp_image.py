import numpy as np
import sys


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of an RGB image.

    Args:
        arg1 (array): The image to invert.

    Returns:
        An array representing the image with its colors inverted.
    """
    try:
        if not isinstance(array, np.ndarray) \
                or array.ndim != 3 or array.shape[2] != 3:
            raise AssertionError("Argument should be an array of an RGB image")

        inverted_array = 255 - array
        return inverted_array

    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        return None


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to an RGB image,
    making only the red channel visible.

    Args:
        arg1 (array): The image to filter.

    Returns:
        An array representing the image with only the red channel visible.
    """
    try:
        if not isinstance(array, np.ndarray) \
                or array.ndim != 3 or array.shape[2] != 3:
            raise AssertionError("Argument should be an array of an RGB image")

        red_filter_mask = np.array([1, 0, 0], dtype=array.dtype)
        red_array = array * red_filter_mask
        return red_array

    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        return None


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to an RGB image,
    making only the green channel visible.

    Args:
        arg1 (array): The image to filter.

    Returns:
        An array representing the image with only the green channel visible.
    """

    try:
        if not isinstance(array, np.ndarray) \
                or array.ndim != 3 or array.shape[2] != 3:
            raise AssertionError("Argument should be an array of an RGB image")

        green_array = array.copy()

        green_array[:, :, 0] = green_array[:, :, 0] - green_array[:, :, 0]
        green_array[:, :, 2] = green_array[:, :, 2] - green_array[:, :, 2]
        return green_array

    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        return None


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to an RGB image,
    making only the blue channel visible.

    Args:
        arg1 (array): The image to filter.

    Returns:
        An array representing the image with only the blue channel visible.
    """

    try:
        if not isinstance(array, np.ndarray) \
                or array.ndim != 3 or array.shape[2] != 3:
            raise AssertionError("Argument should be an array of an RGB image")

        blue_array = array.copy()

        blue_array[:, :, 0] = 0
        blue_array[:, :, 1] = 0
        return blue_array

    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        return None


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts an RGB image to grayscale.

    Args:
        arg1 (array): The image to convert.

    Returns:
        An array representing the image in greyscale.
    """

    try:
        if not isinstance(array, np.ndarray) \
                or array.ndim != 3 or array.shape[2] != 3:
            raise AssertionError("Argument should be an array of an RGB image")

        grayscale_array = array[:, :, 1]
        return grayscale_array.astype(np.uint8)

    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        return None
