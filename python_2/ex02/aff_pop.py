import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import sys
from load_csv import load
import numpy as np



def convert_population(pop_str):
    """
    Convert the population string to a float value.

    Args:
        pop_str (str): Population string.

    Returns:
        float: Numeric population value.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        try:
            return float(pop_str)
        except ValueError:
            print(f"Warning: Could not convert '{pop_str}'. Returning NaN.")
            return np.nan

def main():
    """
    Program that calls the load function from load_csv, loads the file
    population_total.csv, and displays the population of France versus
    the population of Belgium.

    Args: None

    Returns : None
    """

    df = load("population_total.csv")
    # france_data = df[df['country'] == 'France']
    france_data = df.loc[df['country'] == 'France']
    years_df_slice = france_data.loc[:, '1800':'2050']
    years = years_df_slice.columns.astype(int)
    pop_france = france_data.loc[:, '1800':'2050'].values.flatten()
    pop_france_float = np.array([convert_population(x) for x in pop_france])

    belgium_data = df.loc[df['country'] == 'Belgium']
    pop_belgium = belgium_data.loc[:, '1800':'2050'].values.flatten()
    pop_belgium_float = np.array([convert_population(x) for x in pop_belgium])

    df_to_plt = pd.DataFrame({
        'Year' : years,
        'France population' : pop_france_float,
        'Belgium population' : pop_belgium_float
    })

    sns.lineplot(x='Year', y='France population', data=df_to_plt, label='France', color='green')
    sns.lineplot(x='Year', y='Belgium population', data=df_to_plt, label='Belgium')

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(40))
    # plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
    desired_yticks = [20_000_000.0, 40_000_000.0, 60_000_000.0]
    plt.gca().set_yticks(desired_yticks)
    formatter = ticker.FuncFormatter(lambda x, p: f'{x/1_000_000:.0f}M')
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()