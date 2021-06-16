import pandas as pd
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
GDP_dict = dict(zip(WHR_GDP["Country name"], WHR_GDP["Log GDP per capita"]))

# MERGING DATA IS NULLING VALUES>>> WHY????

#WHR_Mean_GDP = pd.concat([WHR_Mean, WHR_GDP], join="outer")
#print(T5_B5)
WHR_Mean["Regional indicator"] = WHR_Mean["Country name"].map(Country_dict)
WHR_Mean["Log GDP per capita"] = WHR_Mean["Country name"].map(GDP_dict)
#WHR_Mean_GDP = WHR_Mean_GDP.sort_values(["Log GDP per capita"], ascending=True)

#WHR_ri = WHR05_20.groupby("Country name")["Regional indicator"]
#WHR_ave_ri = pd.merge(WHR_ave,WHR_ri,on='Country name',how='outer')

print(WHR_GDP)
print(WHR_Mean)
#print(WHR_T5, WHR_B5)

fig, ax = plt.subplots()
ax.scatter(WHR_Mean["Country name"], WHR_Mean["Ladder score"])
ax.scatter(WHR_GDP["Country name"], WHR_GDP["Log GDP per capita"])
ax.set_xlabel('Country')
ax.set_ylabel("Happiness Index")
plt.xticks(rotation=85)
plt.ylim(0, 10)
#plt.legend()
ax.set_title("Mean Counties' Happiness")
plt.show()
