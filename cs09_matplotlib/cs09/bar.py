import pandas as pd
import matplotlib.pyplot as plt

# def count_produce(row):
#     # Make a dictionary with month as key and units sold as value? Issue is month repetitions will overwrite.
#     # Could do a check on whether the key is already in the dicitonary, if not then new. If so then add the values?
#     # We are accessing one row at a time. Not going to work. Could do a for loop in main, which grabs the number
#     # of items which fall in the subcategory. Then build a dict.
#     month = row['Month Sold']
#
#     return pass


# TODO: Change from set to user input
desired_category = "Lettuce, Head"
df = pd.read_csv('food_cleaned.csv')
# aggregate_sales = {}
# aggregate_sales = df.loc[df['SubCategory'] == 'Lettuce, Head'].apply(count_produce,
#                                                                      axis=1)
desired_rows = df.loc[df['SubCategory'] == desired_category]
# for row in range(len(desired_rows)):
#     month = row[]
summed_values = desired_rows.groupby('Month Sold', as_index=False).agg(['sum'])[["Units Sold"]]
month_list = summed_values.index.to_list()
month_list = [x for x in month_list if not x.startswith('18')]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df['months'] = pd.Categorical(df['months'], categories=months, ordered=True)
df.sort_values(...)  # same as you have now; can use inplace=True
# ordered_month_dict = {'19-Jan':'', '19:Feb':'','19:Mar':'','19:Apr':'','19:May':'','19:Jun':'','19:Jul':'','19:Aug':'','19:Feb':'','19:Feb':'',}
# summed_values.plot.bar()
# TODO: Get this bar chart looking nifty. Still need names, and a key value. What is none none?
# TODO: Get the months in order and get rid of incorrect years
