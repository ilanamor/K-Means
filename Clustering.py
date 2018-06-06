from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Clustering:

    kmeans = pd.DataFrame({})
    df = pd.DataFrame({})
    n_clusters = 0
    n_init = 0

    def __init__(self,data,n_clusters, n_init):
        self.df = data
        self.n_clusters = n_clusters
        self.n_init = n_init


    def calcKmeans(self):
        self.kmeans = KMeans(n_clusters=self.n_clusters, n_init=self.n_init).fit(self.df)
        self.df["cluster"]= self.kmeans.labels_
        self.df.reset_index(level=0, inplace=True)
        return self.df

    def drawScatter(self):
        cm = plt.cm.get_cmap('RdYlBu')
        x = self.df["Generosity"]
        y = self.df["Social support"]
        z = self.df["cluster"]
        sc = plt.scatter(x, y, c=z)
        plt.colorbar(sc)
        plt.show()