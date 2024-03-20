import pandas as pd
import numpy as np

"""
flight1= pd.read_excel('data/1Flight 1.xlsx')
flight2= pd.read_excel('data/1Flight 2.xlsx')
flight3= pd.read_excel('data/1Flight 3.xlsx')
flight4= pd.read_excel('data/1Flight 4.xlsx')
flight5= pd.read_excel('data/1Flight 5.xlsx')
flight6= pd.read_excel('data/1Flight 6.xlsx')
flight7= pd.read_excel('data/1Flight 7.xlsx')
flight31= pd.read_excel('data/30Flight 1.xlsx')
flight32= pd.read_excel('data/30Flight 2.xlsx')
flight33= pd.read_excel('data/30Flight 3.xlsx')
flight34= pd.read_excel('data/30Flight 4.xlsx')
flight35= pd.read_excel('data/30Flight 5.xlsx')
flight36= pd.read_excel('data/30Flight 6.xlsx')
flight37= pd.read_excel('data/30Flight 7.xlsx')
"""

airport= pd.read_csv('data/airports-extended-clean.csv', sep = ';', decimal=',')
schedule= pd.read_csv('data/schedule_airport.csv')

# Controleren als NaN of - in de dataframe zit en anders veranderen naar de de nul
"""
flight1['TRUE AIRSPEED (derived)'].fillna(0, inplace=True)
flight2[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight4['TRUE AIRSPEED (derived)'].fillna(0, inplace=True)
flight5['TRUE AIRSPEED (derived)'].fillna(0, inplace=True)
flight6['TRUE AIRSPEED (derived)'].fillna(0, inplace=True)
flight7[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight32[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight33[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight34[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight36[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
"""
schedule[["DL1", "IX1", "DL2", "IX2"]] = schedule[["DL1", "IX1", "DL2", "IX2"]].replace("-", "0")

# Controleren op duplicaten in de dataframe 
scheduleclean= schedule.drop_duplicates()
airportclean= airport.drop_duplicates().dropna()

"""
flight1clean= flight1.drop_duplicates()
flight2clean= flight2.drop_duplicates()
flight3clean= flight3.drop_duplicates()
flight4clean= flight4.drop_duplicates()
flight5clean= flight5.drop_duplicates()
flight6clean= flight6.drop_duplicates()
flight7clean= flight7.drop_duplicates()
flight31clean= flight31.drop_duplicates()
flight32clean= flight32.drop_duplicates()
flight33clean= flight33.drop_duplicates()
flight34clean= flight34.drop_duplicates()
flight35clean= flight35.drop_duplicates()
flight36clean= flight36.drop_duplicates()
flight37clean= flight37.drop_duplicates()
"""

