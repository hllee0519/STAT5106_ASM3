import statsmodels.api as sm
import seaborn as sns


airports = sm.datasets.get_rdataset('airports', 'nycflights13').data
flights = sm.datasets.get_rdataset('flights', 'nycflights13').data
planes = sm.datasets.get_rdataset('planes', 'nycflights13').data
# airlines = sm.datasets.get_rdataset('airlines', 'nycflights13').data

#a
# newFlights = flights.groupby('dest')['arr_delay'].mean()
# df_join = newFlights.to_frame().merge(airports, how='left', left_on='dest', right_on='faa')
# print(df_join)

#b
df_join = flights.merge(planes, how='left', left_on='tailnum', right_on='tailnum')[(flights.dep_delay<=0)].filter(['year_y', 'arr_delay']).set_index('year_y')
# newDf_join = df_join.groupby('year_y')
# newDf_by_year=df_join.stack()
print(df_join)
sns.scatterplot(data=df_join, x=df_join.year_y, y=df_join.arr_delay)
# print(snsPlanesAge)