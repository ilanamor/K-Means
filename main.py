from CleanData import *
from Clustering import *
import pandas as pd

df = pd.read_excel("data.xlsx")
dataCleaner = CleanData(df).Clean()
clustering = Clustering(dataCleaner,3,5)
table=clustering.calcKmeans()
clustering.drawScatter()
print "xxxx"