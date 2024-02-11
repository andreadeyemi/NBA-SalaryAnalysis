import pandas as pd

# Load the dataset
dataset_path = "nba_2022-23_all_stats_with_salary.csv"
data = pd.read_csv(dataset_path)

# Display the first few rows of the dataset
print(data.head())
