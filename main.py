import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("full_grouped.csv")

# Show first rows
print(df.head())

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Select countries
countries = ['Pakistan', 'India', 'US']

# Filter data
filtered_df = df[df['Country/Region'].isin(countries)]

# -----------------------------
# Daily Confirmed Cases Graph
# -----------------------------
plt.figure(figsize=(12,6))

for country in countries:
    country_data = filtered_df[filtered_df['Country/Region'] == country]

    plt.plot(
        country_data['Date'],
        country_data['Confirmed'],
        label=country
    )

plt.title("COVID-19 Confirmed Cases")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("covid_cases_graph.png", dpi=300)
plt.show()

# -----------------------------
# Death Comparison Chart
# -----------------------------
latest_data = filtered_df.groupby('Country/Region')['Deaths'].max()

latest_data.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Total Death Comparison")
plt.ylabel("Deaths")

plt.show()

# -----------------------------
# Recovery Rate Analysis
# -----------------------------
confirmed = filtered_df.groupby('Country/Region')['Confirmed'].max()
recovered = filtered_df.groupby('Country/Region')['Recovered'].max()

recovery_rate = (recovered / confirmed) * 100

print("\nRecovery Rate:\n")
print(recovery_rate)

recovery_rate.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Recovery Rate Analysis")
plt.ylabel("Recovery Rate %")

plt.show()

# -----------------------------
# Heatmap
# -----------------------------
heatmap_data = filtered_df[['Confirmed', 'Deaths', 'Recovered']]

sns.heatmap(
    heatmap_data.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("COVID Data Heatmap")

plt.show()