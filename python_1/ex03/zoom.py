from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os


def main():
    """
    Loads the image "animal.jpeg".
    Prints the following informations :
        • The size in pixel on both X and Y axis
        • The number of channel
        • The pixel content of the image.
    Displays the zoomed in image with the scale
    on the x and y axis on the image.

    Args:
        None

    Returns:
        None
    """

    try:
        img_array_original = ft_load("animal.jpeg")
        print(img_array_original)

        original_height, original_width, _ = img_array_original.shape

        crop_size = 400

        left = (original_width - crop_size) // 2
        top = (original_height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size

        img_cropped_rgb_array = img_array_original[top:bottom, left:right, :]

        # Grayscale conversion formula: Y = 0.2989*R + 0.5870*G + 0.1140*B
        grayscale_array = (
            img_cropped_rgb_array[:, :, 0] * 0.2989 +
            img_cropped_rgb_array[:, :, 1] * 0.5870 +
            img_cropped_rgb_array[:, :, 2] * 0.1140
        ).astype(np.uint8)

        final_array_shape = grayscale_array.shape

        print(f"New shape after zooming: {final_array_shape}")
        print(grayscale_array)

        plt.imshow(grayscale_array, cmap='gray')
        plt.xlabel("X-axis (pixels)")
        plt.ylabel("Y-axis (pixels)")
        plt.colorbar(label="Pixel Intensity")
        plt.show()

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

####################################################################################
        # img_array_original = ft_load("animal.jpeg")
        # print(img_array_original)

        # img_pil_original = Image.fromarray(img_array_original)

        # original_height, original_width, _ = img_array_original.shape

        # left = (original_width - 400) // 2
        # upper = (original_height - 400) // 2
        # right = left + 400
        # lower = upper + 400

        # img_cropped_pil = img_pil_original.crop((left, upper, right, lower))

        # img_cropped_grayscale_pil = img_cropped_pil.convert('L')

        # final_array = np.array(img_cropped_grayscale_pil)

        # print(f"New shape after zooming: {final_array.shape}")
        # print(final_array)

        # plt.imshow(final_array, cmap='gray')
        # plt.xlabel("X-axis (pixels)")
        # plt.ylabel("Y-axis (pixels)")
        # plt.colorbar(label="Pixel Intensity") # Add a color bar for intensity
        # plt.show()
##########################################################################################
        # Just shrinks the image #########################################################
        # img_array = np.array(ft_load("animal.jpeg"))
        # print(img_array)

        # img_pil = Image.fromarray(img_array)
        # img_resized = img_pil.resize((400, 400)).convert('L')
        # final_array = np.array(img_resized)
        # print(f"New shape after slicing: {final_array.shape}")
        # print(final_array)
        # Image.fromarray(final_array).show()
        # final_array.show()

    # except Exception as e:
    #     print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()