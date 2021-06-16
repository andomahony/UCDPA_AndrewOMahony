import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 100)

WHR05_20 = pd.read_csv(r"C:\Users\anom\Desktop\.ipynb_checkpoints\Project\world-happiness-report.csv")
WHR21 = pd.read_csv(r"C:\Users\anom\Desktop\.ipynb_checkpoints\Project\world-happiness-report-2021.csv")

#print(WHR21["Regional indicator"])

Country_dict = dict(zip(WHR21["Country name"], WHR21["Regional indicator"]))
#print(Country_dict)

WHR05_20["Regional indicator"] = WHR05_20["Country name"].map(Country_dict)
#print(WHR05_20.tail())

WHR05_20 = WHR05_20.rename(columns={'Life Ladder': 'Ladder score'})
#WHR05_20 = WHR05_20.astype(str)
#WHR19 = WHR05_20[WHR05_20["year"] == 2019]
#WHR_tens = WHR05_20[WHR05_20["year"] == 2017]
#print(WHR_tens.head())


#print(WHR05_20.head())
#fig, ax = plt.subplots()

#ax.scatter(WHR19["Country name"], WHR19["Ladder score"])
#ax.set_ylabel('Happiness')
#plt.xlim(0, 150)
#ax.set_title('Regional Happiness')
#plt.show()

#print(type(WHR05_20["Ladder score"]))

#print(WHR19)

#print(ds.loc[ds['Country name']== "United States"])

#print(ds.keys())

#print(ds.loc(ds["year"]== "2020", ds.sort_values(by=["Healthy life expectancy at birth"],ascending=False))

#print(ds.info())

#ds_US = ds[ds['Country name'] == 'United States']
#print(ds_US)

#ds_2020 = ds[ds['year'] == 2020]
#print(ds_2020[ds_2020["Healthy life expectancy at birth"] > 70])
#print("Mean life ex. 2020: ", (ds_2020["Healthy life expectancy at birth"].mean()))
#print("Min life ex. 2020: ", (ds_2020["Healthy life expectancy at birth"].min()))
#print("Max life ex. 2020: ", (ds_2020["Healthy life expectancy at birth"].max()))
#print("Median life ex. 2020: ", (ds_2020["Healthy life expectancy at birth"].median()))

WHR_ave = WHR05_20.groupby("Country name")["Ladder score"].mean()
WHR_T5 = pd.DataFrame(WHR_ave.sort_values(ascending=False).head(5))
#WHR_T5["Regional indicator"] = WHR_T5.map(Country_dict)
WHR_B5 = pd.DataFrame(WHR_ave.sort_values(ascending=True).head(5))
#WHR_B5["Regional indicator"] = WHR_B5.map(Country_dict)

T5_B5 = pd.concat([WHR_T5, WHR_B5], join="outer")
T5_B5 = T5_B5["Ladder score"].astype(str)
T5_B5 = "{:.2f}".format(["Ladder score"])
#print(T5_B5)

#print(WHR_ave)
#fig, ax = plt.subplots()

#ax.barh(T5_B5.index, T5_B5)
#ax.set_xlabel('Happiness')
#plt.xticks(rotation=80)
#plt.ylim(3, 8)
#ax.set_title('Regional Happiness')
#plt.show()


