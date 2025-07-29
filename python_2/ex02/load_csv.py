import pandas as pd
import os



def load(path: str) -> pd.DataFrame :
    """
    Takes a path as argument, writes the dimensions of the data set
    and returns it.

    Args:
        arg1 (str): The path of the data set to load.

    Returns:
        A pandas dataframe of the data set.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Error: File '{path}' not found.")
        if not os.path.isfile(path):
            raise ValueError(f"Error: '{path}' is not a valid file.")
        if not path.lower().endswith(".csv"):
            raise AssertionError("file must be .csv.")

        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except FileNotFoundError as e:
        print(str(e))
        return None