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

#From Top and Bottom 5 graph, we know that Denmark has the highest mean over time and Burundi has the lowest.
#I want to see how they trend over time.

WHR_DK = WHR05_20[WHR05_20['Country name'] == "Denmark"]
WHR_BRU = WHR05_20[WHR05_20['Country name'] == "Burundi"]
#print(WHR_DK, WHR_BRU)

#WHD_TB = pd.concat([WHR_DK , WHR_BRU], join="outer")
#print(WHD_TB)
#print(WHR05_20)

fig, ax = plt.subplots()
ax.plot(WHR_DK["year"], WHR_DK["Ladder score"], color="g", linestyle = "--", marker="o", label="Denmark")
ax.plot(WHR_BRU["year"], WHR_BRU["Ladder score"], color="r", linestyle = "--", marker=".", label="Burundi")
#ax.annotate(">1 degree", xy=(2014, 3)), arrowprops={"arrowstyle":"->", "color":"gray"}
ax.set_xlabel('Year')
ax.set_ylabel("Happiness Index")
ax.set_title("Top and bottom counties' happiness over time")
plt.legend()
plt.ylim(2, 10)
plt.show()



