from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
import matplotlib.pyplot as plt
import sys


def main():
    try:
        array = ft_load("landscape.jpg")
        inv_arr = ft_invert(array)
        red_arr = ft_red(array)
        green_arr = ft_green(array)
        blue_arr = ft_blue(array)
        grey_arr = ft_grey(array)
        print(ft_invert.__doc__)

        fig, axes = plt.subplots(3, 2, figsize=(10, 15))
        plt.subplots_adjust(hspace=0.5)

        axes[0][0].imshow(array)
        axes[0][0].set_title('Original')
        axes[0, 0].axis('off')

        axes[0][1].imshow(inv_arr)
        axes[0][1].set_title('Invert')
        axes[0, 1].axis('off')

        axes[1][0].imshow(red_arr)
        axes[1][0].set_title('Red')
        axes[1, 0].axis('off')

        axes[1][1].imshow(green_arr)
        axes[1][1].set_title('Green')
        axes[1, 1].axis('off')

        axes[2][0].imshow(blue_arr)
        axes[2][0].set_title('Blue')
        axes[2, 0].axis('off')

        axes[2][1].imshow(grey_arr, cmap='gray')
        axes[2][1].set_title('Grey')
        axes[2, 1].axis('off')

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
