import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
        plt.savefig("histogram.jpg")

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
            [
                "Acidez",
                "Balance",
                "Cuerpo",
                "Dulzura",
                "Fragancia/Aroma",
                "Sabor",
                "Sabor Residual",
            ]
        ]
        print(quant_sensorial_atributes.describe())

    def qualitative_sensorial_attributes(self):
        """
        Get qualitative sensorial attributes of coffee
        :return: None
        """
        self.data["Fragrance"] = self.data["Descripcion"].str.extract(
            r"Fragancia: (.*?), "
        )
        self.data["Aroma"] = self.data["Descripcion"].str.extract(r"Aroma: (\w+.\w+)")
        self.data["Flavor"] = self.data["Descripcion"].str.extract(
            r"Defecto/ Atributo: (\w+.\w+.\w+)"
        )
        qual_sensorial_atributes = self.data[["Fragrance", "Aroma", "Flavor"]]
        qual_sensorial_atributes["Fragrance"].fillna("N/A", inplace=True)
        # print(qual_sensorial_atributes['Atributo'].value_counts())
        # print(qual_sensorial_atributes['Fragance'].value_counts())
        return qual_sensorial_atributes["Fragrance"]
        # return qual_sensorial_atributes["Flavor"]

    def flavors_distribution(self):
        """
        Get flavors distribution
        :return: None
        """
        flavors = self.qualitative_sensorial_attributes()
        flavors = flavors.value_counts()
        flavors.plot(kind="bar")
        plt.grid()
        plt.xticks(rotation=30, ha="right", size=6)
        plt.xlabel("Fragancia", size=10)
        plt.ylabel("Frecuencia", size=10)
        plt.title("Espectro de fragancias", fontsize=10)
        # plt.savefig("flavors.jpg") 
        plt.savefig("fragancias.jpg")

    def flavors_correlation(self):
        """
        Get flavors correlation from qualitative sensorial attributes of coffee as heatmap using seaborn
        :return: None
        """
        flavors = self.qualitative_sensorial_attributes()
        flavors = pd.get_dummies(flavors)
        flavors_corr = flavors.corr()
        plt.figure(figsize=(15,15))
        sns.heatmap(flavors_corr, annot=True)
        plt.savefig("flavors_corr.jpg")

    def acidity(self):
        """
        Get acidity of coffee
        :return: None
        """
        acidity = self.data["Acidez"]
        plt.figure(figsize=(15, 15))
        plt.xlabel("Puntaje catador", size=25)
        plt.xticks(size=20)
        plt.ylabel("Frecuencia", size=25)
        plt.yticks(size=20)
        acidity.plot(kind="hist", bins=10, figsize=(20, 15))
        plt.savefig("acidity.jpg")