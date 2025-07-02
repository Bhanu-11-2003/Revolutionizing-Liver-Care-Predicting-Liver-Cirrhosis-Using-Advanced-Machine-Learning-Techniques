# Milestone 2: Data Collection & Preparation
import pandas as pd
df = pd.read_csv('liver_dataset.csv')
df.dropna(inplace=True)
df.to_csv('cleaned_liver_data.csv', index=False)
