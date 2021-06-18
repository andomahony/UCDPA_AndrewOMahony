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
check_for_nan= pd.isnull(WHR05_20)
#print(check_for_nan)

WHR05_20 = WHR05_20.dropna()
#print(WHR05_20)

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
#WHR_ri = WHR05_20.groupby("Country name")["Regional indicator"]
#WHR_ave_ri = pd.merge(WHR_ave,WHR_ri,on='Country name',how='outer')

WHR_T5 = pd.DataFrame(WHR_ave.sort_values(ascending=False).head(5))
WHR_T5["Regional indicator"] = WHR_T5.index.map(Country_dict)
WHR_B5 = pd.DataFrame(WHR_ave.sort_values(ascending=True).head(5))
WHR_B5["Regional indicator"] = WHR_B5.index.map(Country_dict)

#WHR_ave_ri = pd.concat([WHR_ave , WHR_ri], join="outer")
#print(WHR_ave.head())
#print(WHR_T5, WHR_B5)

T5_B5 = pd.concat([WHR_T5, WHR_B5], join="outer")
#T5_B5 = T5_B5["Ladder score"].astype(float)
#print(T5_B5)

WestE = T5_B5[T5_B5["Regional indicator"] == "Western Europe"]
WestE.reset_index(inplace=True)
#plt.show()

#SubSA = T5_B5[T5_B5["Regional indicator"] == "Sub-Saharan Africa"]
#SouthA = T5_B5[T5_B5["Regional indicator"] == "South Asia"]
#print(type(WestE))
#Merged_Reg = pd.concat([WestE, SubSA, SouthA])
#print(Merged_Reg.keys())

#print(Merged_Reg)

#WestE = pd.array(WestE)
print(WestE)

# creates a stacked bar plot
#Merged_Reg[0].plot(kind='bar', stacked=True)
#plt.title("Regional Happiness")
#plt.xlabel("Family Member")
#plt.ylabel("Pies Consumed")

#print(WHR_ave)
fig, ax = plt.subplots()

ax.bar(WestE[["Country name", "Regional indicator"]], WestE["Ladder score"])
ax.set_xlabel('Region')
ax.set_ylabel("Happiness Index")
plt.xticks(rotation=0)
plt.ylim(0, 8)
ax.set_title('Regional Happiness')
plt.show()


#print("Andy O'Mahony")

# Bringing in files to created DataFrame and also "Regional Dictionary".

WHR05_20 = pd.read_csv(r"C:\Users\anom\Desktop\.ipynb_checkpoints\Project\world-happiness-report.csv")
WHR21 = pd.read_csv(r"C:\Users\anom\Desktop\.ipynb_checkpoints\Project\world-happiness-report-2021.csv")
Country_dict = dict(zip(WHR21["Country name"], WHR21["Regional indicator"]))
WHR05_20["Regional indicator"] = WHR05_20["Country name"].map(Country_dict)

# Rename life ladder score
WHR05_20 = WHR05_20.rename(columns={'Life Ladder': 'Ladder score'})

# Dropping row with NAN
WHR05_20 = WHR05_20.dropna()
WHR05_20.reset_index(inplace=True)

WHR_Mean = WHR05_20.groupby("Country name")["Ladder score"].mean()
WHR_Mean = pd.DataFrame(WHR_Mean)
WHR_Mean.reset_index(inplace=True)
WHR_GDP = WHR05_20.groupby("Country name")["Log GDP per capita"].mean()
WHR_GDP = pd.DataFrame(WHR_GDP)
WHR_GDP.reset_index(inplace=True)
WHR_LE = WHR05_20.groupby("Country name")["Healthy life expectancy at birth"].mean()
WHR_LE = pd.DataFrame(WHR_LE)
WHR_LE.reset_index(inplace=True)
GDP_dict = dict(zip(WHR_GDP["Country name"], WHR_GDP["Log GDP per capita"]))
Life_E_dict = dict(zip(WHR_LE["Country name"], WHR_LE["Healthy life expectancy at birth"]))

# MERGING DATA IS NULLING VALUES>>> WHY????

#WHR_Mean_GDP = pd.concat([WHR_Mean, WHR_GDP], join="outer")
#print(T5_B5)
WHR_Mean["Regional indicator"] = WHR_Mean["Country name"].map(Country_dict)
WHR_Mean["Log GDP per capita"] = WHR_Mean["Country name"].map(GDP_dict)
WHR_Mean["Healthy life expectancy at birth"] = WHR_Mean["Country name"].map(Life_E_dict)
WHR_Mean = WHR_Mean.sort_values(["Log GDP per capita"], ascending=True)

#WHR_ri = WHR05_20.groupby("Country name")["Regional indicator"]
#WHR_ave_ri = pd.merge(WHR_ave,WHR_ri,on='Country name',how='outer')


print(WHR_Mean)
#print(WHR_T5, WHR_B5)

fig, ax = plt.subplots()
ax2=ax.twinx()
ax.scatter(WHR_Mean["Healthy life expectancy at birth"], WHR_Mean["Ladder score"], color="g")
ax2.scatter(WHR_Mean["Healthy life expectancy at birth"], WHR_Mean["Log GDP per capita"], color="r")
ax.set_xlabel('Life expectancy')
ax.set_ylabel("Happiness Index", color="g")
ax2.set_ylabel("Log GDP", color="r")
ax.tick_params(axis='x', which='major', length=6, pad=10,  labelsize=15, rotation=45)
z = np.polyfit(WHR_Mean["Healthy life expectancy at birth"], WHR_Mean["Ladder score"], 1)
p = np.poly1d(z)
ax.plot(WHR_Mean["Healthy life expectancy at birth"], p(WHR_Mean["Healthy life expectancy at birth"]), "b:")
plt.show()
#plt.legend()
ax.set_title("Mean Counties' Happiness")
plt.show()