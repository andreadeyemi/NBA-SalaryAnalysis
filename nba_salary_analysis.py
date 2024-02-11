import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
stats_dataset_path = "nba_2022-23_all_stats_with_salary.csv"
salaries_dataset_path = "nba_salaries.csv"

stats_data = pd.read_csv(stats_dataset_path)
salaries_data = pd.read_csv(salaries_dataset_path)

# Display the first few rows of each dataset before cleaning
print("\nData before cleaning:")
print("\nStatistics Dataset:")
print(stats_data.head())
print("\nSalaries Dataset:")
print(salaries_data.head())

# Handle missing values
print("\nHandling missing values...")
print("\nNumber of missing values in the statistics dataset before handling:")
print(stats_data.isnull().sum())
stats_data.fillna(0, inplace=True)  # Fill missing values with 0
print("\nNumber of missing values in the statistics dataset after handling:")
print(stats_data.isnull().sum())

# Remove duplicates
print("\nRemoving duplicates...")
print("\nNumber of duplicate rows in the salaries dataset before removal:")
print(salaries_data.duplicated().sum())
salaries_data.drop_duplicates(inplace=True)
print("\nNumber of duplicate rows in the salaries dataset after removal:")
print(salaries_data.duplicated().sum())

# Display the first few rows of each dataset after cleaning
print("\nData after cleaning:")
print("\nStatistics Dataset:")
print(stats_data.head())
print("\nSalaries Dataset:")
print(salaries_data.head())

# Calculate summary statistics for statistics dataset
stats_summary = stats_data.describe()

# Calculate summary statistics for salaries dataset
salaries_summary = salaries_data.describe()

# Display the summary statistics
print("\nSummary Statistics for Statistics Dataset:")
print(stats_summary)

print("\nSummary Statistics for Salaries Dataset:")
print(salaries_summary)

# Set the style of seaborn
sns.set(style="whitegrid")

# Define the performance metrics to visualize
performance_metrics = ['PTS', 'AST', 'TRB']  # Points, Assists, Rebounds

# Loop through each performance metric and create visualizations
for metric in performance_metrics:
    plt.figure(figsize=(10, 6))
    
    # Create a histogram
    plt.subplot(2, 1, 1)
    sns.histplot(stats_data[metric], kde=True)
    plt.title(f'Distribution of {metric}')
    plt.xlabel(metric)
    plt.ylabel('Frequency')
    
    # Create a box plot
    plt.subplot(2, 1, 2)
    sns.boxplot(x=stats_data[metric])
    plt.title(f'Boxplot of {metric}')
    plt.xlabel(metric)
    
    plt.tight_layout()
    plt.show()
