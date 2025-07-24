from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
import sys


def cut_square_img() -> np.array:
    """
    Loads the image "animal.jpeg", cuts a square from it and returns it.

    Args:
        None

    Returns:
        Array representing a square portion of "animal.jpeg".
    """

    try:
        img_array_original = ft_load("animal.jpeg")

        original_height, original_width, _ = img_array_original.shape

        crop_size = 400

        left = (original_width - crop_size) // 2
        top = (original_height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size

        img_cropped_rgb_array = img_array_original[top:bottom, left:right, :]

        grayscale_array = (
            img_cropped_rgb_array[:, :, 0] * 0.2989 +
            img_cropped_rgb_array[:, :, 1] * 0.5870 +
            img_cropped_rgb_array[:, :, 2] * 0.1140
        ).astype(np.uint8)

        # final_array = np.expand_dims(grayscale_array, axis=2)
        final_array = grayscale_array
        print(f"The shape of image is: {final_array.shape}")
        print(final_array)

        return final_array

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)


def transpose_array(arr: np.array) -> np.array:
    """
    Transposes a given 2D array.

    Args:
        arg1 (np.array) : Array to be tranposed.

    Return:
        Transposed array
    """
    # transposed_arr = np.moveaxis(arr, source = 1, destination=0)

    transposed_arr = np.zeros((arr.shape[0], arr.shape[1]), dtype=np.uint8)
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            transposed_arr[x][y] = arr[y][x]

    return transposed_arr


def main():
    """
    Loads the image "animal.jpeg", cut a square part from it
    and transpose it.
    Displays it, print the new shape
    and the data of the image after the transpose.

    Args:
        None

    Returns:
        None
    """
    sqr_arr = cut_square_img()
    tranposed_img_arr = transpose_array(sqr_arr)
    print(f"New shape after Transpose: {tranposed_img_arr.shape}")
    print(tranposed_img_arr)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(sqr_arr, cmap='gray')
    axes[0].set_title('Original Square Image')
    axes[1].imshow(tranposed_img_arr, cmap='gray')
    axes[1].set_title('Transposed Image')

    plt.show()


if __name__ == "__main__":
    main()
