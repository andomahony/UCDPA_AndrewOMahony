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

# Sorting and defining Regional Mean
WHR_Reg_Mean = WHR05_20.groupby("Regional indicator")["Ladder score"].mean()
WHR_Reg_Mean = pd.DataFrame(WHR_Reg_Mean)
WHR_Reg_Mean.reset_index(inplace=True)

# Defining values for displaying
def pie_values(mean_values):
    display_values  = np.round(mean_values/100.*WHR_Reg_Mean["Ladder score"].sum(), 2)
    return display_values

# Plotting pie chart to display mean by region
plt.pie(WHR_Reg_Mean["Ladder score"], labels=WHR_Reg_Mean["Regional indicator"], startangle=90, autopct=pie_values, explode =(0,0,0,0,0,0.2,0,0,0,0.1), shadow= True, textprops={'fontsize': 12})
plt.title(r"Happiness by regional area")
plt.show()

# Sorting and defining Country Mean from the top Region of North America and ANZ
WHR_US_ANZ = WHR05_20.groupby("Country name")["Ladder score"].mean()
WHR_US_ANZ = pd.DataFrame(WHR_US_ANZ)
WHR_US_ANZ.reset_index(inplace=True)
WHR_US_ANZ["Regional indicator"] = WHR_US_ANZ["Country name"].map(Country_dict)
WHR_US_ANZ = WHR_US_ANZ[WHR_US_ANZ["Regional indicator"] == "North America and ANZ"]

# Defining absolute values for Country from Top Regional area
def pie_values_cn(mean_values_cn):
    display_values_cn  = np.round(mean_values_cn/100.*WHR_US_ANZ["Ladder score"].sum(), 2)
    return display_values_cn

# Plotting pie chart to display mean by region
plt.pie(WHR_US_ANZ["Ladder score"], labels=WHR_US_ANZ["Country name"], startangle=90, autopct=pie_values_cn, explode =(0,0.1,0,0), shadow= True)
plt.title("Happiness by county from top region")
plt.show()

