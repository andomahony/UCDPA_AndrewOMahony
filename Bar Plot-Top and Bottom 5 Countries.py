import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 100)
pd.set_option("display.width", 100)

# Bringing in files to created DataFrame and also "Regional Dictionary".

WHR05_20 = pd.read_csv(r"C:\Users\anom\Desktop\.ipynb_checkpoints\Project\world-happiness-report.csv")
WHR21 = pd.read_csv(r"C:\Users\anom\Desktop\.ipynb_checkpoints\Project\world-happiness-report-2021.csv")
Country_dict = dict(zip(WHR21["Country name"], WHR21["Regional indicator"]))
WHR05_20["Regional indicator"] = WHR05_20["Country name"].map(Country_dict)

# Rename life ladder score.
WHR05_20 = WHR05_20.rename(columns={'Life Ladder': 'Ladder score'})

# Dropping row with NAN.
WHR05_20 = WHR05_20.dropna()

# Mean Score over years (2005 - 2020) and splitting top and bottom 5.
WHR_ave = WHR05_20.groupby("Country name")["Ladder score"].mean()
WHR_T5 = pd.DataFrame(WHR_ave.sort_values(ascending=False).head(5))
WHR_T5["Regional indicator"] = WHR_T5.index.map(Country_dict)
WHR_T5.reset_index(inplace=True)
WHR_B5 = pd.DataFrame(WHR_ave.sort_values(ascending=False).tail(5))
WHR_B5["Regional indicator"] = WHR_B5.index.map(Country_dict)
WHR_B5.reset_index(inplace=True)

# Plotting the chart.
fig, ax = plt.subplots()
ax.bar(WHR_T5["Country name"], WHR_T5["Ladder score"], label=WHR_T5["Regional indicator"].unique())
ax.bar(WHR_B5["Country name"], WHR_B5["Ladder score"], label=WHR_B5["Regional indicator"].unique())
ax.set_xlabel("Country", fontsize=20)
ax.set_ylabel("Happiness Index", fontsize=20)
plt.xticks(rotation=0)
plt.ylim(0, 10)
plt.legend()
ax.set_title("Mean top and bottom 5 counties' happiness")
plt.show()

