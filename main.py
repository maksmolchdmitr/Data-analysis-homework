import pandas as pd


def clear_dataset(df):
    print(df.head())

    # Check duplicated rows
    duplicates = df[df.duplicated(keep=False)]
    print("Duplicates:", duplicates)
    # df.drop_duplicates(inplace=True)

    # Check rows with missing data
    missing_values = df[df.isnull().any(axis=1)]
    print("Missing values:", missing_values)
    # df.dropna(inplace=True)

    # Remove unused column
    print("Columns:", df.columns)
    df.drop(columns=['Unnamed: 0'], inplace=True)
    print("Columns:", df.columns)
    print(df.head())

    # Check different value types
    print(df.dtypes)
    object_cols = df.select_dtypes(include='object').columns
    for col in object_cols:
        print(f"Column '{col}' has values:", df[col].unique())


df = pd.read_csv('diamonds.csv')
clear_dataset(df)
