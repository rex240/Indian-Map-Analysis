import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout = 'wide')

df = pd.read_csv('India.csv')

list_of_state = df['State'].unique().tolist()
list_of_state = sorted(list_of_state)
list_of_state.insert(0, 'Overall India')

st.sidebar.title('India Data Visualization')

selected_state = st.sidebar.selectbox('Select a State', list_of_state)
primary = st.sidebar.selectbox('select Primary Parameter', sorted(df[['Population', 'Households_with_Internet','Housholds_with_Electric_Lighting','sex_ratio', 'literacy_rate']]))
secondary = st.sidebar.selectbox('select Secondary Parameter', sorted(df[['Population', 'Households_with_Internet','Housholds_with_Electric_Lighting','sex_ratio', 'literacy_rate']]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        # plot for India
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                                size = primary, color = secondary, mapbox_style= 'carto-positron',
                                color_continuous_scale=px.colors.cyclical.IceFire, zoom=3,
                                size_max = 35, width = 1200, height = 700,
                                hover_name = 'District')
        # Update hover template to change the background color and data color
        st.plotly_chart(fig, use_container_width = True)
    else:
        # plot for selected state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",
                                size = primary, color = secondary,  mapbox_style= 'carto-positron',
                                color_continuous_scale=px.colors.cyclical.IceFire, zoom=5,
                                size_max = 35, width = 1200, height = 700,
                                hover_name = 'District')
        st.plotly_chart(fig, use_container_width = True)
