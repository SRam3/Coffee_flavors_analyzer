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

    def Puntaje_Catador(self):
        """
        Plot the puntaje catador as a function of the date in points
        """
        puntaje_catador = self.data[["Fecha", "Puntaje Catador"]].sort_values("Fecha")
        puntaje_catador["Fecha"] = pd.to_datetime(puntaje_catador["Fecha"])
        puntaje_catador = puntaje_catador.groupby(puntaje_catador["Fecha"].dt.year)["Puntaje Catador"].mean()
        plt.figure(figsize=(10, 8))
        plt.plot(puntaje_catador.index, puntaje_catador.values, marker="o")
        plt.gca().yaxis.set_major_formatter("{:.2f}".format)
        plt.xlabel("Año", size=18)
        plt.ylabel("Puntaje Catador promedio", size=18)
        plt.xticks(puntaje_catador.index, rotation=30, ha="right", size=15)
        plt.yticks(size=15)
        # plt.title("Puntaje Catador ", fontsize=18)
        plt.savefig("puntaje_catador.jpg")




        # puntaje_catador["Fecha"] = pd.to_datetime(puntaje_catador["Fecha"])
        # puntaje_catador = puntaje_catador["Fecha"].dt.strftime("%Y-%m-%d")
        # puntaje_catador = puntaje_catador.groupby("Fecha").mean()
        # plt.plot(puntaje_catador["Fecha"], puntaje_catador["Puntaje Catador"], marker="o")
        # plt.xlabel("Fecha", size=15)
        # plt.ylabel("Puntaje Catador", size=15)
        # plt.xticks(rotation=30, ha="right", size=10)
        # plt.yticks(size=10)
        # plt.title("Puntaje Catador", fontsize=15)
        # plt.savefig("puntaje_catador.jpg")


        # puntaje_catador["Fecha"] = puntaje_catador["Fecha"].dt.strftime("%Y-%m-%d")
        # puntaje_catador["Fecha"] = pd.to_datetime(puntaje_catador["Fecha"])
        # puntaje_catador = puntaje_catador.groupby("Fecha").mean()
        # puntaje_catador.plot()
        # plt.savefig("puntaje_catador.jpg")
