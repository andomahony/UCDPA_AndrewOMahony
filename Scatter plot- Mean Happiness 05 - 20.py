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

WHR_Mean = WHR05_20.groupby("Country name")["Ladder score"].mean()
WHR_Mean = pd.DataFrame(WHR_Mean)
WHR_Mean.reset_index(inplace=True)
WHR_GDP = WHR05_20.groupby("Country name")["Log GDP per capita"].mean()
WHR_GDP = pd.DataFrame(WHR_GDP)
WHR_GDP.reset_index(inplace=True)
WHR_LE = WHR05_20.groupby("Country name")["Healthy life expectancy at birth"].mean()
WHR_LE = pd.DataFrame(WHR_LE)
WHR_LE.reset_index(inplace=True)
# Creating dictionaries to merge data
GDP_dict = dict(zip(WHR_GDP["Country name"], WHR_GDP["Log GDP per capita"]))
Life_E_dict = dict(zip(WHR_LE["Country name"], WHR_LE["Healthy life expectancy at birth"]))

# Creating new columns in the 1 WHR_Mean DataFrame.
WHR_Mean["Regional indicator"] = WHR_Mean["Country name"].map(Country_dict)
WHR_Mean["Log GDP per capita"] = WHR_Mean["Country name"].map(GDP_dict)
WHR_Mean["Healthy life expectancy at birth"] = WHR_Mean["Country name"].map(Life_E_dict)
WHR_Mean = WHR_Mean.sort_values(["Log GDP per capita"], ascending=True)

#Plotting the Scatter plot of Does Happiness increase with higher Life Expectancy and Higher Log GDP
fig, ax = plt.subplots()
ax2=ax.twinx()
ax.scatter(WHR_Mean["Healthy life expectancy at birth"], WHR_Mean["Ladder score"], color="g")
ax2.scatter(WHR_Mean["Healthy life expectancy at birth"], WHR_Mean["Log GDP per capita"], color="r")
ax.set_xlabel('Life expectancy')
ax.set_ylabel("Happiness Index", color="g", fontsize=20)
ax2.set_ylabel("Log GDP per capita", color="r", fontsize=20)
ax.tick_params(axis='x', which='major', length=6, pad=10,  labelsize=15, rotation=0)
z = np.polyfit(WHR_Mean["Healthy life expectancy at birth"], WHR_Mean["Ladder score"], 1)
p = np.poly1d(z)
ax.plot(WHR_Mean["Healthy life expectancy at birth"], p(WHR_Mean["Healthy life expectancy at birth"]), "b:")
plt.title("Life expectancy against happiness & log GDP")
plt.show()

