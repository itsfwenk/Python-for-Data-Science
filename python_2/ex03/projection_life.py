import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
from load_csv import load
import numpy as np
import sys


def convert_income(income_str):
    """
    Convert the income string to a float value.

    Args:
        income_str (str): Income string.

    Returns:
        float: Numeric income value.
    """
    if type(income_str) is int:
        return float(income_str)
    elif income_str.endswith("M"):
        return float(income_str[:-1]) * 1e6
    elif income_str.endswith("k"):
        return float(income_str[:-1]) * 1e3
    else:
        try:
            return float(income_str)
        except ValueError:
            print(f"Warning: Could not convert '{income_str}'. Returning NaN.")
            return np.nan


def main():
    """
    Program that calls the load function from load_csv, loads the file
    income_per_person_gdppercapita_ppp_inflation_adjusted.csv" and
    life_expectancy_years.csv, and displays  the projection of life
    expectancy in relation to the gross national product of
    the year 1900 for each country.

    Args: None

    Returns : None
    """

    income_file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    df_income = load(income_file)
    if df_income is None:
        sys.exit(1)

    df_life_exp = load("life_expectancy_years.csv")
    if df_life_exp is None:
        sys.exit(1)

    income_1900_str = df_income['1900']
    income_1900 = np.array([convert_income(x) for x in income_1900_str])
    life_exp_1900 = df_life_exp['1900']

    df_to_plt = pd.DataFrame({
        '1900 income': income_1900,
        '1900 life expectancy': life_exp_1900
    })

    sns.scatterplot(data=df_to_plt, x="1900 income", y="1900 life expectancy")

    plt.xscale("log")
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(5))
    # plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
    desired_xticks = [300.0, 1000.0, 10_000.0]
    plt.gca().set_xticks(desired_xticks)
    formatter = ticker.FuncFormatter(
        lambda x, p: f'{int(x)}'if x < 1000 else f'{x/1_000:.0f}k'
        )
    plt.gca().xaxis.set_major_formatter(formatter)

    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
