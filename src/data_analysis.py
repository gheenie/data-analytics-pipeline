import pandas
import plotly.express as px

# 1. Requirements/hypothesis

# 2. Collecting/scraping

# 3. Cleaning

# 4. Processing/manipulating

df = pandas.read_csv('data/unit05-data.csv')

# Example 1
df_avg_incidence_by_year = df.groupby('year', as_index=False).agg({'Estimated incidence (all forms) per 100 000 population': 'mean'})
# print(df_avg_incidence_by_year)

# Example 2
df_singapore = df[df['country'] == 'Singapore']
print(df_singapore)

# 5a. Quantitative/statistical analysis

# 5b. Graphical analysis/visualisation

# Example 1
figure = px.bar(df_avg_incidence_by_year, x='year', y='Estimated incidence (all forms) per 100 000 population')
# figure.show()

# Example 2
figure = px.line(df_singapore, x='year', y='Estimated incidence (all forms) per 100 000 population')
figure.show()

# 6. Decision making/conclusions
