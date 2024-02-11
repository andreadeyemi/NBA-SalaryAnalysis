import pandas as pd

# Load the datasets
stats_dataset_path = "nba_2022-23_all_stats_with_salary.csv"
salaries_dataset_path = "nba_salaries.csv"

stats_data = pd.read_csv(stats_dataset_path)
salaries_data = pd.read_csv(salaries_dataset_path)

# Display the first few rows of each dataset
print("Statistics Dataset:")
print(stats_data.head())
print("\nSalaries Dataset:")
print(salaries_data.head())
