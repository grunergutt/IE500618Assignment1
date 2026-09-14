import os
import pandas as pd
import matplotlib as plt

BASE_DIR = os.path.join(os.getcwd())
PATH_DATA = os.path.join(BASE_DIR, "data")
PATH_AMESHOUSING = os.path.join(PATH_DATA, "AmesHousing.csv")

df = pd.read_csv(PATH_AMESHOUSING)
print(df.head())