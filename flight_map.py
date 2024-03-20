import data_cleaning
import pyproj
import pandas as pd

start_ICAO = 'LSZH'

# Subesetting ICAO, LON, LAT from dataframe
airport_df = data_cleaning.airportclean[['Name', 'ICAO', 'Longitude', 'Latitude']]
airport_df.drop_duplicates()

# Pre-calculate flight paths
flight_paths = {}
for _, row in airport_df.iterrows():
    end_ICAO = row['ICAO']
    start = airport_df.loc[airport_df['ICAO'] == start_ICAO, ['Longitude', 'Latitude']].values[0]
    end = airport_df.loc[airport_df['ICAO'] == end_ICAO, ['Longitude', 'Latitude']].values[0]
    g = pyproj.Geod(ellps='WGS84')
    _, _, dist = g.inv(start[0], start[1], end[0], end[1])
    num_segments = int(dist / 1000) + 1
    lonlats = g.npts(start[0], start[1], end[0], end[1], num_segments)
    flight_paths[end_ICAO] = [(lat, lon) for lon, lat in lonlats]
    print(_)

# Create DataFrame from flight_paths
flight_paths_df = pd.DataFrame(flight_paths.items(), columns=['ICAO', 'FlightPath'])

# Export flight paths to CSV
flight_paths_df.head(100).to_csv('flight_paths.csv', index=False)






