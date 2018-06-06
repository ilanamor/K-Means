from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py

class Clustering:

    kmeans = pd.DataFrame({})
    df = pd.DataFrame({})
    n_clusters = 0
    n_init = 0
    scatter = None

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
        sc = plt.scatter(x=self.df["Social support"], y=self.df["Generosity"], c=self.df["cluster"])
        plt.title("K-Meams Clustering")
        plt.ylabel("Generosity")
        plt.xlabel("Social support")
        plt.colorbar(sc)
        self.scatter=plt
        #plt.show()
        #plt.savefig("D:\documents\users\ilanamor\Documents\\tmp.png")
        self.scatter.show()


    def horoplethMap(self):
        #username: ilanamor
        # PuJAQXTCGxrq3pgAHvqo

        data = [dict(
            type='choropleth',
            locations=self.df['CODE'],
            z=self.df['GDP (BILLIONS)'],
            text=self.df['COUNTRY'],
            colorscale=[[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"], \
                        [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]],
            autocolorscale=False,
            reversescale=True,
            marker=dict(
                line=dict(
                    color='rgb(180,180,180)',
                    width=0.5
                )),
            colorbar=dict(
                autotick=False,
                tickprefix='$',
                title='GDP<br>Billions US$'),
        )]

        layout = dict(
            title='2014 Global GDP<br>Source:\
                    <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
                    CIA World Factbook</a>',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection=dict(
                    type='Mercator'
                )
            )
        )

        fig = dict(data=data, layout=layout)
        py.iplot(fig, validate=False, filename='d3-world-map')

