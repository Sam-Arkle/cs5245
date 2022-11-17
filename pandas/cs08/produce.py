import pandas as pd
import hashlib

# arklesd cleans subcategory Lettuce, Head

items = [
    'Apples, Early Yellow Transparent', 'Apples, Gala', 'Apples, Gold Rush',
    'Apples, Red Rome Beauty', 'Apples, Spice', 'Basil, Fresh - Sweet Genovese (green)',
    'Beets, Without Greens', 'Collards', 'Garlic Scapes', 'Jerusalem Artichokes',
    'Lettuce, Head', 'Lettuce, Loose Leaf Green', 'Microgreens, Sunshine Mix',
    'Okra, Green', 'Peppers, Bell (Green)', 'Peppers, Jalapeno', 'Pumpkin, Seminole',
    'Rosemary, Fresh', 'Sweet Potatoes, Orange', 'Watermelon, Jubilee'
]


def myhash(user_name):
    m = hashlib.sha256()
    m.update(bytes(user_name, 'utf-8'))
    return int(m.hexdigest()[:16], 16)


user_name = 'arklesd'
item = items[myhash(user_name) % len(items)]
print(f'{user_name} cleans subcategory {item}')


def clean_lettuce(lettuce_row):
    unit = lettuce_row['Unit']
    if unit == 'Case':
        lettuce_row['Unit'] = 'Head'
        lettuce_row['Units Sold'] *= 28
    if unit == '1 head':
        lettuce_row['Unit'] = 'Head'
    return lettuce_row


def main():
    df = pd.read_csv('food.csv')
    df.loc[df['SubCategory'] == 'Lettuce, Head'] = df.loc[df['SubCategory'] == 'Lettuce, Head'].apply(clean_lettuce,
                                                                                                      axis=1)
    df.to_csv('cleaned_produce.csv', index=False)


if __name__ == '__main__':
    main()
