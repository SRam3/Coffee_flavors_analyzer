import pandas as pd
import matplotlib.pyplot as plt


class Exploration:
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
        :return: None
        """
        self.data.drop("ID", axis=1, inplace=True)
        self.data.sort_values("Fecha", inplace=True)
        self.data.hist(bins=10, figsize=(20, 15))
        plt.show()
        plt.savefig("histogram.png")

    def get_description(self):
        """
        Get data description
        :return: None
        """
        print(self.data.describe())


class Coffee(Exploration):
    def __init__(self, directory: str):
        super().__init__(directory)

    def physical_atributes(self):
        """
        Get physical attributes of coffee
        :return: None
        """
        phys_atributes = self.data[["Almendra sana", "Broca", "Humedad", "Pasilla"]]
        print(phys_atributes.describe())

    def quantitative_sensorial_attributes(self):
        """
        Get quantitative sensorial attributes of coffee
        :return: None
        """
        quant_sensorial_atributes = self.data[
            ["Acidez", "Balance", "Cuerpo", "Dulzura", "Fragancia/Aroma", "Sabor", "Sabor Residual"]
        ]
        print(quant_sensorial_atributes.describe())

    def qualitative_sensorial_attributes(self):
        """
        Get qualitative sensorial attributes of coffee
        :return: None
        """
        self.data['Fragance'] = self.data['Descripcion'].str.extract(r'Fragancia: (.*?), ')
        self.data['Aroma'] = self.data['Descripcion'].str.extract(r'Aroma: (\w+.\w+)')
        self.data['Atributo'] = self.data['Descripcion'].str.extract(r'Defecto/ Atributo: (\w+.\w+.\w+)')
        qual_sensorial_atributes = self.data[["Fragance", "Aroma", "Atributo"]]
        qual_sensorial_atributes['Fragance'].fillna("N/A", inplace=True)
        # print(qual_sensorial_atributes['Atributo'].value_counts())
        # print(qual_sensorial_atributes['Fragance'].value_counts())
        print(qual_sensorial_atributes['Aroma'].value_counts())

