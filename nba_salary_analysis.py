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

# Explore the datasets further
print("\nShape of the statistics dataset:", stats_data.shape)
print("Shape of the salaries dataset:", salaries_data.shape)

print("\nInformation about the statistics dataset:")
print(stats_data.info())
print("\nInformation about the salaries dataset:")
print(salaries_data.info())

print("\nSummary statistics for the statistics dataset:")
print(stats_data.describe())
print("\nSummary statistics for the salaries dataset:")
print(salaries_data.describe())

print("\nColumn names for the statistics dataset:")
print(stats_data.columns)
print("\nColumn names for the salaries dataset:")
print(salaries_data.columns)

print("\nSample data from the statistics dataset:")
print(stats_data.head())
print("\nSample data from the salaries dataset:")
print(salaries_data.head())
