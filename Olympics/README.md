# Olympic Medal Analysis Project

## Project Overview

This project involves analyzing the comprehensive dataset of Olympic athletes to uncover patterns and trends related to athletic success. The analysis focuses on the relationship between Body Mass Index (BMI), age, and medal success, as well as examining the distribution of medals among different regions and National Olympic Committees (NOCs) over time.

## Project Objectives

1. Analyze the relationship between an athlete's BMI and their likelihood of winning a medal.
2. Explore how age and experience influence the probability of winning medals in various sports.
3. Investigate trends in the distribution of medals among different regions and NOCs over time.

## Dataset

- **Olympics Dataset**: Contains data on athletes including attributes like age, height, weight, team, sport, event, and medals won.
- **NOC Regions Dataset**: Provides region information for National Olympic Committees (NOCs).

## Requirements

- Python 3. x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLAlchemy (if using SQL for data extraction)
- Jupyter Notebook (for running the analysis in an interactive environment)

## Installation

To set up the project environment, install the required packages using pip:

```bash
pip install pandas numpy matplotlib seaborn sqlalchemy jupyter
```

## Usage

### Data Preparation

1. Load Data: Import the datasets using pandas.

```bash
import pandas as pd

olympics_df = pd.read_csv('olympics_data.csv')
noc_regions_df = pd.read_csv('noc_regions.csv')
```

2. Merge Datasets: Combine the datasets to include region information in the main dataset.

```bash
merged_df = pd.merge(olympics_df, noc_regions_df, left_on='NOC', right_on='NOC', how='left')
```

3. Data Cleaning: Perform necessary data cleaning and preprocessing.

```bash
merged_df.dropna(inplace=True)
```

### Analysis

1. Correlation Analysis: Analyze the relationship between BMI and medal success.
```bash
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x='BMI', y='Medal_Won', data=merged_df)
plt.title('BMI vs Medal Success')
plt.show()
```

2. Age Analysis: Explore the age distribution of medal winners.

```bash
sns.histplot(merged_df[merged_df['Medal_Won'] == 1]['Age'], bins=20, kde=True)
plt.title('Age Distribution of Medal Winners')
plt.show()
```

3. Geographical Trends: Visualize medal distribution by region over time.

```bash
sns.lineplot(x='Year', y='Medals', hue='Region', data=merged_df.groupby(['Year', 'Region']).size().reset_index(name='Medals'))
plt.title('Medal Distribution by Region Over Time')
plt.show()
```

### Visualization
Create visualizations for different sports and countries to observe trends.

```bash
for sport in top_sports:
    sns.lineplot(x='Year', y='Medals', hue='Country', data=merged_df[merged_df['Sport'] == sport])
    plt.title(f'Medal Distribution in {sport}')
    plt.show()
```

## Results

- BMI and Medal Success: Insights into how BMI affects medal success across different sports.
- Age and Performance: Understanding the optimal age ranges for peak performance.
- Geographical Trends: Analysis of medal distribution by region and NOC over time.

## Contribution
Feel free to contribute to the project by submitting issues or pull requests. Your feedback and suggestions are welcome.

