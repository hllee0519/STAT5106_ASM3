import statsmodels.api as sm
flights = sm.datasets.get_rdataset('flights', 'nycflights13').data
airlines = sm.datasets.get_rdataset('airlines', 'nycflights13').data

df_out = flights.merge(airlines, how='left', left_on='carrier', right_on='carrier')

#a i
newFlights = df_out[(df_out.arr_delay >= 120)]
print(newFlights)

#a ii
newFlights = df_out[(df_out.dest.isin(["IAH", "HOU"]))]
print(newFlights)

#a iii
newFlights = df_out[(df_out.name.isin(["United Air Lines Inc.", "American Airlines Inc.", "Delta Air Lines Inc."]))]
print(newFlights)

#a iv
newFlights = df_out[(df_out.month.isin([7, 8, 9]))]
print(newFlights)

#a v
newFlights = df_out[(df_out.arr_delay>120) & (df_out.dep_delay<=0)]
print(newFlights)

#a vi
newFlights = df_out[(df_out.arr_delay<=-30) & (df_out.dep_delay>=60)]
print(newFlights)

#a vii
newFlights = df_out[(df_out.dep_time>=0000) & (df_out.dep_time<=600)]
print(newFlights)

#b
mostDepartureDelayed = df_out.sort_values(by='dep_delay', ascending=False)
print(mostDepartureDelayed)
#b
leftEarliest = df_out.sort_values(by= 'dep_time', ascending=True)
print(leftEarliest)