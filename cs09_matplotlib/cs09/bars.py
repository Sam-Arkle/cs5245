import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler


def clean_month(month_value):
    month_value = month_value[3:]
    return month_value


def main():
    # desired_category_start = 'Basil'
    desired_category_start = input('Keep subcategories that start with: ')

    df = pd.read_csv('food_cleaned.csv')
    desired_rows = df.loc[df['SubCategory'].str.startswith(desired_category_start)]
    desired_rows = desired_rows.loc[desired_rows['Month Sold'].str.startswith('19')]
    desired_rows['Month Sold'] = desired_rows['Month Sold'].apply(clean_month)
    summed_values = desired_rows.groupby(['SubCategory', 'Month Sold'], as_index=False).sum(numeric_only=True)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    pd.Categorical(summed_values, categories=months, ordered=True)
    categories_array = summed_values['SubCategory'].unique()
    dataframe_dict = {}
    for category in categories_array:
        dataframe_dict[category] = summed_values.loc[summed_values['SubCategory'] == category].sort_values('Month Sold',
                                                                                                           key=lambda
                                                                                                               x: pd.Categorical(
                                                                                                               x,
                                                                                                               categories=months,
                                                                                                               ordered=True))
    counter = 0
    fig, axes = plt.subplots(nrows=len(dataframe_dict), ncols=1, gridspec_kw={'hspace': 0})
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    axes_dict = {}

    for element in dataframe_dict:
        monthly_value = []
        month_to_int = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
                        'Oct': 10,
                        'Nov': 11, 'Dec': 12}
        rows, columns = dataframe_dict[element].shape
        df = dataframe_dict[element].groupby('Month Sold', as_index=False).first()
        for month in months:
            if month in df['Month Sold'].unique():
                weighted_amount = float(df.loc[df['Month Sold'] == month]['Units Sold']) * month_to_int[month]
                monthly_value.append(weighted_amount)
            else:
                df.loc[len(df.index)] = [month, float('nan'), float('nan')]
        df = df.sort_values('Month Sold',
                            key=lambda
                                x: pd.Categorical(
                                x,
                                categories=months,
                                ordered=True))
        # Normalization parameters
        monthly_total = df['Units Sold'].sum()
        normalize_min = 0.1
        normalize_max = 1
        mms = MinMaxScaler()
        df['Units Sold'] = preprocessing.minmax_scale(df['Units Sold'],
                                                      feature_range=(normalize_min, normalize_max))
        df.plot.bar(ax=axes[counter], legend=None, rot=0)
        expected_month_purchase = float((sum(monthly_value) / monthly_total))
        axes[counter].set_ylabel(f'{element} ({expected_month_purchase:.2f})', rotation=0)
        axes[counter].set_yticklabels([])
        axes_dict[axes[counter]] = expected_month_purchase

        counter += 1
    plt.xticks(array, months)
    plt.show()


if __name__ == '__main__':
    main()
