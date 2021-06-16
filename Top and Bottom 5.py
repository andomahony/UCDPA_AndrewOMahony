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


# Mean Score over year and splitting top and bottom 5
WHR_ave = WHR05_20.groupby("Country name")["Ladder score"].mean()
WHR_T5 = pd.DataFrame(WHR_ave.sort_values(ascending=False).head(5))
WHR_T5["Regional indicator"] = WHR_T5.index.map(Country_dict)
WHR_B5 = pd.DataFrame(WHR_ave.sort_values(ascending=True).head(5))
WHR_B5["Regional indicator"] = WHR_B5.index.map(Country_dict)

# Joining Top and Bottom 5 to create 1 DF.
T5_B5 = pd.concat([WHR_T5, WHR_B5], join="outer")
fig, ax = plt.subplots()

ax.bar(T5_B5["Regional indicator"], T5_B5["Ladder score"])
ax.set_xlabel('Region')
ax.set_ylabel("Happiness Index")
plt.xticks(rotation=0)
plt.ylim(0, 8)
ax.set_title('Regional Happiness')
plt.show()
