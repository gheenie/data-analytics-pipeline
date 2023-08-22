import pandas
import plotly.express as px

# Requirements/hypothesis

# Collecting

# Processing

df = pandas.read_csv('data/unit05-data.csv')

avg_incidence_by_year = df.groupby('year', as_index=False).agg({'Estimated incidence (all forms) per 100 000 population': 'mean'})
print(avg_incidence_by_year)
print(avg_incidence_by_year.columns)

# Cleaning

# Quantitative/statistical analysis

# Graphical analysis/visualisation

figure = px.bar(avg_incidence_by_year, x='year', y='Estimated incidence (all forms) per 100 000 population')
figure.show()

# Decision making/conclusions
