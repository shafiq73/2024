# Pakistan Population Data Analysis 🇵🇰

This project analyzes Pakistan's population data to understand distribution, growth trends, and demographic patterns.

## Import Libraries
In this step, we import all the necessary Python libraries required for data analysis and visualization.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
```

## Load Dataset
Here, we load the dataset using Pandas and preview the first few rows to understand its structure.

```python
df = pd.read_csv("pak_population.csv")
df.head()
```

## Dataset Overview
This step helps us understand the dataset structure, data types, and basic statistical summary.

```python
df.info()
df.describe()
```

## Missing Values Check
We check for missing values in the dataset to ensure data quality.

```python
df.isnull().sum()
```

## Data Cleaning
In this step, we handle missing values and clean column names for better processing.

```python
df.fillna(method='ffill', inplace=True)
df.columns = df.columns.str.strip()
```

## Population by Province
This visualization shows how population is distributed across different provinces.

```python
plt.figure()
df.groupby('Province')['Population'].sum().sort_values().plot(kind='bar')
plt.title("Population by Province")
plt.xlabel("Province")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.show()
```

## Urban vs Rural Population
This chart compares the urban and rural population distribution.

```python
urban = df['Urban_Population'].sum()
rural = df['Rural_Population'].sum()

plt.figure()
plt.pie([urban, rural], labels=['Urban', 'Rural'], autopct='%1.1f%%')
plt.title("Urban vs Rural Population")
plt.show()
```

## Gender Distribution
This section analyzes the distribution of male and female population.

```python
male = df['Male_Population'].sum()
female = df['Female_Population'].sum()

plt.figure()
plt.pie([male, female], labels=['Male', 'Female'], autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.show()
```

## Population Growth Trend
This visualization shows how the population changes over time.

```python
if 'Year' in df.columns:
    plt.figure()
    df.groupby('Year')['Population'].sum().plot()
    plt.title("Population Growth Over Time")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()
```

## Top Regions by Population
This chart highlights the regions with the highest population.

```python
top_regions = df.groupby('Region')['Population'].sum().sort_values(ascending=False).head(10)

plt.figure()
top_regions.plot(kind='bar')
plt.title("Top 10 Regions by Population")
plt.xticks(rotation=45)
plt.show()
```

## Correlation Analysis
This heatmap shows the relationship between different numerical variables.

```python
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()
```

## Conclusion
This project provides insights into Pakistan’s population distribution and demographic trends. It highlights differences between provinces, urban and rural populations, and gender distribution. The analysis demonstrates the importance of data-driven decision-making.

## Debug Tip
```python
print(df.columns)
```
