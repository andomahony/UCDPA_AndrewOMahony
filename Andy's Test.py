import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

ds = pd.read_csv(r"C:\Users\anom\Desktop\.ipynb_checkpoints\world-happiness-report.csv")

#print(ds.head())

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

print(ds.groupby("Country name")["Healthy life expectancy at birth"].mean())
