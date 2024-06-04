import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('gapminder.csv')

# Group the data by region and calculate the average life expectancy
life_expectancy_by_region = data.groupby('Region')['LifeExpectancy'].mean().reset_index()

# Print the results
print(life_expectancy_by_region)

# Save the results to a CSV file
life_expectancy_by_region.to_csv('life_expectancy_by_region.csv', index=False)