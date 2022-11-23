# Sam Arkle
# Resources used: https://cs.appstate.edu/~rmp/cs5245/pythondatasciencehandbook.pdf
# Additional features: Computed expected month of sale. Used the names of months on x-axis.
# Applied a style to the chart

import pandas as pd
import matplotlib.pyplot as plt

def main():
    # desired_category = "Apples, Gold Rush"
    desired_category = input('Enter SubCategory: ')
    df = pd.read_csv('food_cleaned.csv')
    desired_rows = df.loc[df['SubCategory'] == desired_category]
    desired_rows['Month Sold'] = desired_rows['Month Sold'].map(lambda x: x.lstrip('19-'))
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    desired_rows = desired_rows[desired_rows['Month Sold'].isin(months)]
    unit = desired_rows['Unit'].iat[0]
    summed_values = desired_rows.groupby('Month Sold', as_index=False).agg(['sum'])[["Units Sold"]]
    month_list = summed_values.index.to_list()
    monthly_value = []
    month_to_int = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
                    'Nov': 11, 'Dec': 12}
    for month in month_list:
        weighted_amount = summed_values.loc[month]['Units Sold'] * month_to_int[month]
        monthly_value.append(weighted_amount)
    pd.Categorical(summed_values, categories=months, ordered=True)
    summed_values = summed_values.sort_values('Month Sold',
                                              key=lambda x: pd.Categorical(x, categories=months, ordered=True))
    plt.style.use('classic')
    summed_values.plot.bar()
    monthly_average = summed_values['Units Sold'].sum()
    expected_month_purchase = float(sum(monthly_value) / monthly_average)

    plt.xlabel(f'Month (Average {expected_month_purchase:.2f})')
    plt.xticks(rotation=30, horizontalalignment="center")
    plt.ylabel('Units Sold')
    plt.title(f'{unit}, {desired_category}')
    plt.legend('')
    plt.show()


if __name__ == '__main__':
    main()

