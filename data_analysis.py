import pandas as pd


def data_reader():
    try:
        df = pd.read_json('data.json')
    except ValueError:
        print('Incorrect file name')
    else:
        print(df)

data_reader()