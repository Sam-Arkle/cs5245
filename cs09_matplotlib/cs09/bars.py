import pandas as pd
import matplotlib.pyplot as plt

def clean_month(month_value):
    month_value = month_value[3:]
    return month_value

# TODO: Make it a user input thing:

desired_category_start = 'Apple'
df = pd.read_csv('food_cleaned.csv')
desired_rows = df.loc[df['SubCategory'].str.startswith(desired_category_start)]
desired_rows = desired_rows.loc[desired_rows['Month Sold'].str.startswith('19')]
desired_rows['Month Sold'] = desired_rows['Month Sold'].apply(clean_month)
# summed_values = desired_rows.groupby(['SubCategory', 'Month Sold'], as_index=False).agg(['sum'])[["Units Sold"]]
summed_values = desired_rows.groupby(['SubCategory', 'Month Sold'], as_index=False).sum(numeric_only=True)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
pd.Categorical(summed_values, categories=months, ordered=True)
# summed_values = summed_values.sort_values('Month Sold',
#                                               key=lambda x: pd.Categorical(x, categories=months, ordered=True))
categories_array = summed_values['SubCategory'].unique()
dataframe_dict = {}
for category in categories_array:
    dataframe_dict[category] = summed_values.loc[summed_values['SubCategory'] == category].sort_values('Month Sold',
                                              key=lambda x: pd.Categorical(x, categories=months, ordered=True))
counter = 0
fig, axes = plt.subplots(nrows=dataframe_dict.__len__(), ncols=1, sharey=True)
for element in dataframe_dict:
    rows, columns = dataframe_dict[element].shape
    # plt.subplot(rows, columns, counter)
    dataframe_dict[element].plot.bar(ax=axes[counter])
    counter += 1
plt.show()
