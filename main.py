import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def numeric_stats(df):
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    print("Numeric columns:", numeric_cols)

    # Рассчитываем среднее значение, медиану и моду для численных переменных
    mean_values = df[numeric_cols].mean()
    median_values = df[numeric_cols].median()
    mode_values = df[numeric_cols].mode().dropna()

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


def draw_hist(df, col):
    plt.hist(df[col], bins=50)
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.show()
    plt.close()


def draw_box_plots(df):
    sns.boxplot(x='price', y='cut', data=df)
    plt.show()
    plt.close()

    sns.boxplot(x='price', y='color', data=df)
    plt.show()
    plt.close()


def draw_scatter_plots(df):
    sns.scatterplot(x='carat', y='price', data=df)
    plt.show()
    plt.close()


def data_visualization(df):
    for col in ['carat', 'depth', 'price']:
        draw_hist(df, col)
    draw_box_plots(df)
    draw_scatter_plots(df)


data_frame = pd.read_csv('diamonds.csv')
clear_dataset(data_frame)
numeric_stats(data_frame)
data_visualization(data_frame)
