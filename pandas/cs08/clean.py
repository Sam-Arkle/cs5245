import pandas as pd
import re
from city_name_map import city_name_map


def clean_city(city):
    if isinstance(city, str):
        city = city.strip()
        city = re.sub('\s\s', ' ', city)
        city = city.title().split(',')[0]
        if city.endswith('Nc'):
            city = city[:-3]
        if city in city_name_map:
            city = city_name_map[city]

    return city


def clean_state(state):
    if isinstance(state, str):
        if state == 'No':
            state = 'NC'
        state = state.upper()
    return state


def clean_zip_code(zip):
    if isinstance(zip, str):
        zip = re.sub('\D', '', zip)
        if len(zip) > 5:
            zip = zip[:5]
        if len(zip) < 5:
            zip = float('nan')
    return zip


# df_person = pd.read_csv('basic_person.csv', index_col='acct_id_new')
# pd.set_option('display.max_rows', 500)
# df_person['city'] = df_person['city'].apply(clean_city)
# # c = df_person['city'].value_counts().sort_index()
# df_person['state'] = df_person['state'].apply(clean_state)
# # states = df_person['state'].value_counts().sort_index()
# df_person['zip'] = df_person['zip'].apply(clean_zip_code)
# # zips = df_person['zip'].value_counts().sort_index()
# # print(zips)
# df_person.to_csv('cleaned.csv', index=False)

# def fix_daft(row):
#     row['zip'] = '28043'
#     return row

def main():
    # Load and process the 'basic_person.csv' file.
    # Save the file 'cleaned.csv' without the implicit index
    df_person = pd.read_csv('basic_person.csv', index_col='acct_id_new')
    pd.set_option('display.max_rows', 500)
    # df_person.loc[df_person['city'] == 'Forest City, NC 28043'] = df_person.loc[df_person['city'] == 'Forest City, NC 28043'].apply(fix_daft, axis=1)
    df_person['city'] = df_person['city'].apply(clean_city)
    df_person['state'] = df_person['state'].apply(clean_state)
    df_person['zip'] = df_person['zip'].apply(clean_zip_code)
    df_person.to_csv('cleaned.csv')


if __name__ == '__main__':
    main()
