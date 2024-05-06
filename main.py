import pandas as pd


def clear_dataset(data_frame):
    print(data_frame.head())

    # Check duplicated rows
    duplicates = data_frame[data_frame.duplicated(keep=False)]
    print("Duplicates:", duplicates)
    # df.drop_duplicates(inplace=True)

    # Check rows with missing data
    missing_values = data_frame[data_frame.isnull().any(axis=1)]
    print("Missing values:", missing_values)
    # df.dropna(inplace=True)

    # Remove unused column
    print("Columns:", data_frame.columns)
    data_frame.drop(columns=['Unnamed: 0'], inplace=True)
    print("Columns:", data_frame.columns)
    print(data_frame.head())

    # Check different value types
    print(data_frame.dtypes)
    object_cols = data_frame.select_dtypes(include='object').columns
    for col in object_cols:
        print(f"Column '{col}' has values:", data_frame[col].unique())


def numeric_stats(data_frame):
    numeric_cols = data_frame.select_dtypes(include='number').columns.tolist()
    print("Numeric columns:", numeric_cols)

    # Рассчитываем среднее значение, медиану и моду для численных переменных
    mean_values = data_frame[numeric_cols].mean()
    median_values = data_frame[numeric_cols].median()
    mode_values = data_frame[numeric_cols].mode().dropna()

    print("Среднее значение:", mean_values, sep="\n")
    print("Медиана:", median_values, sep="\n")
    print("Мода:", mode_values, sep="\n")
    print("""
Среднее значение говорит о том, где находится центр распределения данных.
Медиана делит распределение на две равные части, и она менее чувствительна к выбросам, чем среднее значение.
Мода представляет наиболее часто встречающееся значение в данных.
Данные находятся в разных диапазонах - возможно их нужно будет нормализовать
Длина и ширина алмазов в среднем равны
По сравнению со средней ценой 3932 в выборке самая популярная цена алмаза 605
""")


df = pd.read_csv('diamonds.csv')
clear_dataset(df)
numeric_stats(df)

