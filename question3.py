import pandas as pd

# Load the data
data = pd.read_csv('gapminder.csv')

# Find the countries with the highest and lowest fertility rates
highest_fertility = data.loc[data['FertilityRate'].idxmax()]
lowest_fertility = data.loc[data['FertilityRate'].idxmin()]

# Create a DataFrame to store these results
extreme_fertility = pd.DataFrame([highest_fertility, lowest_fertility], index=['Highest', 'Lowest'])

# Print the results
print("Highest Fertility Rate:\n", highest_fertility)
print("Lowest Fertility Rate:\n", lowest_fertility)

# Save the results to a CSV file
extreme_fertility.to_csv('extreme_fertility_rates.csv')
