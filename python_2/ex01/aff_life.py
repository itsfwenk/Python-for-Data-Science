import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import sys
from load_csv import load



def main():
    """
    Program that calls the load function from load_csv, loads the file
    life_expectancy_years.csv, and displays the information of France.

    Args: None

    Returns : None
    """

    df = load("life_expectancy_years.csv")
    # france_data = df[df['country'] == 'France']
    france_data = df.loc[df['country'] == 'France']
    years = france_data.columns[1:].astype(int)
    life_expectancy = france_data.values[0][1:]

    # life_expectancy = france_data.loc[:, '1800':].values.flatten()

    # Integer-location based indexing
    # life_expectancy = france_data.iloc[0, 1:].values

    df_to_plt = pd.DataFrame({
        'Year' : years,
        'Life expectancy' : life_expectancy
    })

    sns.lineplot(x='Year', y='Life expectancy', data=df_to_plt)
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(40))
    plt.title('France Life expectancy Projections')
    # plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()