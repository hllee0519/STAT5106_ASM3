import pandas as pd
from pandas import DataFrame, read_csv

file = r'asg3_Q3_data/Athletes.xlsx'
athletes_df = pd.read_excel(file).rename(columns={'name': 'athleteName'})
file = r'asg3_Q3_data/Coaches.xlsx'
coaches_df = pd.read_excel(file).rename(columns={'name': 'coachesName'})
file = r'asg3_Q3_data/EntriesGender.xlsx'
entriesGender_df = pd.read_excel(file)
file = r'asg3_Q3_data/Medals.xlsx'
medal_df = pd.read_excel(file)
file = r'asg3_Q3_data/Teams.xlsx'
teams_df = pd.read_excel(file)
print("------------------------------------------------------------------\n")
new_athletes_df=athletes_df.rename(columns={'Name': 'athleteName'})
new_coaches_df=athletes_df.rename(columns={'Name': 'coachesName'})
athletes_coaches_df = new_athletes_df.merge(new_coaches_df, how='left', left_on=['NOC', 'Discipline'], right_on=['NOC', 'Discipline']).groupby('coachesName').count().sort_values(by='athleteName', ascending=False)
print(athletes_coaches_df.head())
print("\nLINDEN Desiree, LIGHTFOOT Kc, ZIEMEK Zachery, ZIEMEK Zachery and WINGER Kara are the top 5 coaches")
print("------------------------------------------------------------------\n")

entriesGender_df['female_proportions']=(entriesGender_df.Female/entriesGender_df.Total)*100
print(entriesGender_df.sort_values(by='female_proportions', ascending=False))
print("\nArtistic Swimming, Rhythmic Gymnastics, Cycling BMX Freestyle, Diving and 3x3 Basketball are the top 5")
print("------------------------------------------------------------------\n")



