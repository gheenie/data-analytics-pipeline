import pandas
import plotly.express as px

# Requirements/hypothesis

# Collecting

# Processing

df = pandas.read_csv('data/unit05-data.csv')

df_avg_incidence_by_year = df.groupby('year', as_index=False).agg({'Estimated incidence (all forms) per 100 000 population': 'mean'})
# print(df_avg_incidence_by_year)

df_singapore = df[df['country'] == 'Singapore']
print(df_singapore)

# Cleaning

# Quantitative/statistical analysis

# Graphical analysis/visualisation

figure = px.bar(df_avg_incidence_by_year, x='year', y='Estimated incidence (all forms) per 100 000 population')
# figure.show()

figure = px.line(df_singapore, x='year', y='Estimated incidence (all forms) per 100 000 population')
figure.show()

# Decision making/conclusions
