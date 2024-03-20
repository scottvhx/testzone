import pyproj
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import data_cleaning
import flight_map
import plotly.express as px
import plost
import altair as alt
import folium

st.set_page_config(layout='wide', 
                   page_title='',
                   page_icon='',
                   initial_sidebar_state='expanded')

alt.themes.enable('dark')

tab1, tab2, tab3, tab4, tab5= st.tabs([":blue[Introductie]", ":blue[Vlucht Planner]", ":blue[]", ":blue[]", ":green[About]"])

airport_df = data_cleaning.airportclean[['Name', 'ICAO', 'Longitude', 'Latitude']]
airport_df.drop_duplicates()

start_ICAO = 'LSZH'

# Load flight paths from CSV
flight_paths_df = pd.read_csv('flight_paths.csv')

# Function to create Folium map
def create_map(data, start_ICAO, flight_paths_df):
    folium_map = folium.Map(location=(0, 0), tiles="cartodb positron", zoom_start=1.5)
    for _, row in data.iterrows():
        end_ICAO = row['ICAO']
        flight_path = eval(flight_paths_df.loc[flight_paths_df['ICAO'] == end_ICAO, 'FlightPath'].iloc[0])
        folium.PolyLine(
            locations=flight_path,
            color='red',
            weight=2
        ).add_to(folium_map)

    return folium_map               

def main():
    # Set title
    st.title("Dynamic Folium Map")

    # Setup Folium map
    map_data = airport_df.copy()
    folium_map = create_map(map_data, start_ICAO)
    st.markdown("### Map")

    # Sidebar for user input
    st.sidebar.markdown("### Options")
    select_origin = st.sidebar.selectbox("Selecteer vliegveld van herkomst", 
                                         ["Zurich Airport"],
                                         index=None,
                                         placeholder='Selecteer vliegveld...')
    select_destination = st.sidebar.selectbox("Selecteer vliegveld van bestemming", 
                                    data_cleaning.airportclean["Name"],
                                    index=None,
                                    placeholder='Selecteer vliegveld...')
    
    # Update map based on user input
    if select_destination:
        highlighted_data = airport_df[airport_df['Name'] == select_destination]
        highlighted_map = create_map(highlighted_data, start_ICAO)
        folium_static(highlighted_map)
        

if __name__ == '__main__':
    main()
    




# flight_map.draw_flight_path("LSZH", data_cleaning.airportclean.loc[data_cleaning.airportclean['Name'] == select_destination, 'ICAO'].values[0])
# folium_static(flight_map.m, height=650)