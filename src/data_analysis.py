import pandas
import plotly.express as px

# 1. Requirements/hypothesis

# 2. Collecting

df = pandas.read_csv('data/unit05-data.csv')

df_world_happiness_report = pandas.read_csv('data/2019.csv')
df_world_happiness_report.to_csv('data/output.csv')

# 3. Cleaning

# 4. Processing

# Example 1
df_avg_incidence_by_year = df.groupby('year', as_index=False).agg({'Estimated incidence (all forms) per 100 000 population': 'mean'})
# print(df_avg_incidence_by_year)

# Example 2
df_singapore = df[df['country'] == 'Singapore']
# print(df_singapore)

# 5. Quantitative analysis

# Which factors appear to have the greatest impact on a nation's happiness
print(df_world_happiness_report['Score'].corr(df_world_happiness_report['GDP per capita']))
print(df_world_happiness_report['Score'].corr(df_world_happiness_report['Healthy life expectancy']))
print(df_world_happiness_report['Score'].corr(df_world_happiness_report['Social support']))
print(df_world_happiness_report['Score'].corr(df_world_happiness_report['Freedom to make life choices']))
print(df_world_happiness_report['Score'].corr(df_world_happiness_report['Perceptions of corruption']))
print(df_world_happiness_report['Score'].corr(df_world_happiness_report['Generosity']))
# Answers are in descending order of the above columns

# 6. Graphical analysis

# Incidences across years
figure = px.bar(df_avg_incidence_by_year, x='year', y='Estimated incidence (all forms) per 100 000 population')
# figure.show()

# Incidences across years, within Singapore
figure = px.line(df_singapore, x='year', y='Estimated incidence (all forms) per 100 000 population')
# figure.show()

# Overall happiness by country
fig = px.bar(df, x='Score', y='Country or region', orientation='h', title='Overall happiness by country')
# fig.show()

# 7. Decision making/conclusions
