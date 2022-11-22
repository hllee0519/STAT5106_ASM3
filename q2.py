import statsmodels.api as sm
import seaborn as sns


airports = sm.datasets.get_rdataset('airports', 'nycflights13').data
flights = sm.datasets.get_rdataset('flights', 'nycflights13').data
planes = sm.datasets.get_rdataset('planes', 'nycflights13').data
weather = sm.datasets.get_rdataset('weather', 'nycflights13').data

### a
newFlights = flights.groupby('dest')['arr_delay'].mean()
df_join = newFlights.to_frame().merge(airports, how='left', left_on='dest', right_on='faa')
df_join.head()

### b
df_join = flights.merge(planes, how='left', left_on='tailnum', right_on='tailnum')[(flights.dep_delay<=0)].filter(['year_y', 'arr_delay'])
sns.scatterplot(data=df_join, x=df_join['year_y'], y=df_join['arr_delay'])
print('This graph shows the delay time of the plane by manufacture year with no departure delay.')
print('There is no devedence that shows age of the plane is related to arrival delay.')

### c
df_dep_delay = flights.merge(weather, how='left', left_on=['origin', 'time_hour'], right_on=['origin', 'time_hour']).filter(['time_hour', 'sched_dep_time', 'dep_delay', 'origin', 'temp', 'dewp', 'humid', 'wind_dir', 'wind_gust', 'precip', 'pressure', 'visib']).sort_values(by='dep_delay', ascending=False)
print('This table shows the delay time of the plane by and the weather conditions')
print('There is strong relation between them')
df_dep_delay.head(100)

### d
sortByDep=flights[(flights.year==2013) & (flights.month==6) & (flights.day==13)].sort_values(by='dep_delay', ascending=False)
print('This table shows the delay time of departure order by departure time desc')
print('There was rain, fog and strong wind in New York')
sortByDep.head(100)