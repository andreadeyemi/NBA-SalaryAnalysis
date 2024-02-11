import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # Import Plotly Express for interactive visualizations

# Load the datasets
stats_dataset_path = "nba_2022-23_all_stats_with_salary.csv"
salaries_dataset_path = "nba_salaries.csv"

# Read the datasets
stats_data = pd.read_csv(stats_dataset_path)
salaries_data = pd.read_csv(salaries_dataset_path)

# Adjust the merge based on the column names and ensure columns with the same name are handled properly
merged_data = pd.merge(stats_data, salaries_data, on='Player Name', suffixes=('_stats', '_salaries'))

# Find the highest-paid player using the correct salary column
highest_paid_player = merged_data.loc[merged_data['Salary_salaries'].idxmax()]

# Display the highest-paid player's name, team, position, and points per game
print("Highest Paid Player:")
print("Name:", highest_paid_player['Player Name'])
print("Team:", highest_paid_player['Team_stats'])  # Using the correct suffix as necessary
print("Position:", highest_paid_player['Position_stats'])  # Using the correct suffix as necessary
print("Points per Game:", highest_paid_player['PTS_stats'])  # Corrected to PTS_stats to avoid KeyError

# Add a constant to shift all PER values to be positive if necessary
min_per = merged_data['PER'].min()
if min_per < 0:
    merged_data['PER_positive'] = merged_data['PER'] - min_per + 1  # Shift PER to positive values
else:
    merged_data['PER_positive'] = merged_data['PER']

# Create an interactive scatter plot with Plotly Express
fig = px.scatter(merged_data,
                 x='PTS_stats',
                 y='Salary_salaries',
                 size='PER_positive',  # Use adjusted PER values for size
                 color='Team_stats',  # Color points by team
                 hover_name='Player Name',  # Show player names on hover
                 title='NBA Players: Points per Game vs. Salary (2022-23)')

fig.update_layout(xaxis_title='Points Per Game', yaxis_title='Salary', coloraxis_colorbar=dict(title='Team'))
fig.show()
