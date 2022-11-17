# flat_file.py
import pandas as pd


def main():
    # Load and process the files.
    # Save the file 'joined.csv' without the implicit index
    df_person = pd.read_csv('basic_person.csv')
    df_student = pd.read_csv('person_detail_f.csv')
    df_map = pd.read_csv('student_detail_v.csv')
    df_person = df_person.groupby('acct_id_new').max()
    df_student = df_student.groupby('person_detail_id_new').max()
    df_map = df_map.groupby('student_id_new', as_index=False).max()

    df_joined = df_map.merge(df_student, left_on='person_detail_id_new', right_on='person_detail_id_new')
    # df_joined = df_joined.groupby('acct_id_new', as_index=False).max()
    df_joined = df_joined.merge(df_person, left_on='acct_id_new', right_on='acct_id_new')
    # df_joined = df_joined.reset_index()
    # df_joined = df_joined.rename(columns={'index': 'student_id_new'})
    df_joined.to_csv('joined.csv', index=False)


if __name__ == '__main__':
    main()
