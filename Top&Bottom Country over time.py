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

print(WHR05_20)


