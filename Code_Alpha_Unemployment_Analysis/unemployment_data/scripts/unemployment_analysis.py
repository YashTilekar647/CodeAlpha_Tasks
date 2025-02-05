import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\CODING\CodeAlphaInternship\Unemployment_Analysis\unemployment_data\data\unemployment_data.csv")


# Display first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Melt the dataframe to reshape for easier analysis
df_melted = pd.melt(df, id_vars=["Country Name", "Country Code"], var_name="Year", value_name="Unemployment Rate")

# Convert 'Year' column to datetime
df_melted['Year'] = pd.to_datetime(df_melted['Year'], format='%Y')

# Check data types and basic statistics
print(df_melted.dtypes)
print(df_melted.describe())

# Filter data for the United States (example)
usa_data = df_melted[df_melted['Country Name'] == 'United States']

# Plot Unemployment Rate Over Time for USA
plt.figure(figsize=(10,5))
sns.lineplot(x='Year', y='Unemployment Rate', data=usa_data)
plt.title("Unemployment Rate Over Time (USA)")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.savefig('unemployment_rate_usa.png')  # Save plot as image
plt.show()

# Bar plot for unemployment rate by country for the latest year
latest_year = df_melted['Year'].max()
df_latest = df_melted[df_melted['Year'] == latest_year]

plt.figure(figsize=(12,6))
sns.barplot(x='Country Name', y='Unemployment Rate', data=df_latest)
plt.xticks(rotation=90)
plt.title(f"Unemployment Rate by Country in {latest_year.year}")
plt.savefig('unemployment_rate_by_country_2021.png')  # Save plot as image
plt.show()

# Correlation Heatmap for numerical data (if available)
# Here we need only the columns with numeric data
numeric_df = df_melted.copy()
numeric_df['Unemployment Rate'] = pd.to_numeric(numeric_df['Unemployment Rate'], errors='coerce')
# Remove non-numeric columns (Country Name, Country Code)
numeric_df = numeric_df.drop(columns=['Country Name', 'Country Code'])

plt.figure(figsize=(8,5))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig('correlation_heatmap.png')  # Save plot as image
plt.show()

# Final print statement to ensure everything is completed
print("Data analysis completed. Plots saved as images.")
