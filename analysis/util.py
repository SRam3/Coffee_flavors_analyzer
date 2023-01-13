import pandas as pd
import matplotlib.pyplot as plt

class Coffee:
    """
    Coffee class
    """
    def __init__(self, directory: str):
        """
        Load data from directory
        :param directory: directory path
        """
        self.data = pd.read_json(directory)

    def explore_data(self):
        """
        Explore data
        :return: None
        """
        print("Data shape: ", self.data.shape)
        print("Data columns: ", self.data.columns)
        print("Data types: ", self.data.dtypes)
        print("Data head: ", self.data.head())

    def get_histogram(self):
        """
        Get histogram of the values distribution
        :param data: pandas dataframe
        :param column: column name
        :return: None
        """
        self.data.drop('ID', axis=1, inplace=True)
        self.data.sort_values('Fecha', inplace=True)
        self.data.hist(bins=10, figsize=(20, 15))
        plt.show()
        plt.savefig('histogram.png')

    def get_correlation(self):
        """
        Get correlation matrix
        :param data: pandas dataframe
        :return: None
        """
        corr_matrix = self.data.corr()
        corr_matrix.to_csv('correlation.csv')
