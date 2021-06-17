import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 100)

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
