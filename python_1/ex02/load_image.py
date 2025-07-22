import numpy as np
from PIL import Image
import os
import sys


def ft_load(path: str) -> np.array:
    """
    Loads an image, prints its format, and its pixels
    content in RGB format.

    Args:
        arg1 (str): Path to the image to be loaded.

    Returns:
        An array representing the loaded image pixels
        content in RGB format
    """
    # try:
    #     if not path.lower().endswith(("jpg", "jpeg")):
    #         raise AssertionError("image format must be JPG or JPEG")
    #     if not os.path.exists(path):
    #         raise AssertionError("file not found:", path)
    #     img = Image.open(path)
    #     #  size is given as a 2-tuple (width, height).
    #     print(
    #         f"The shape of Image is: {img.height}, "
    #         f"{img.width}, {img.layers}"
    #     )
    #     print(np.array(img))
    #     return np.array(img)
    # except AssertionError as e:
    #     print(f"AssertionError: {e}")
    #     sys.exit(1)

    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Error: File '{path}' not found.")
        
        if not os.path.isfile(path):
            raise ValueError(f"Error: '{path}' is not a valid file.")
        
        with Image.open(path) as img:
            img_format = img.format
            
            if img_format not in ['JPEG', 'JPG']:
                print(f"Warning: Image format is {img_format}, but function is designed for JPG/JPEG")
            
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            img_array = np.array(img)
            
            print(f"The shape of image is: {img_array.shape}")
            
            return img_array
            
    except FileNotFoundError as e:
        print(str(e))
        return np.array([])
    
    except ValueError as e:
        print(str(e))
        return np.array([])
    
    except Exception as e:
        print(f"Error loading image: {str(e)}")
        return np.array([])
