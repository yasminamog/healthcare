

import streamlit as st    
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Settings streamlit page configuration
st.set_page_config(layout="wide", page_title=None)

# Set the theme color
st.markdown(
    """
    <style>
    .theme-red .stRadio > label {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Tabs
tabs = st.tabs(["Overview", "Life Expectancy", "Diseases"]) 
 



# Graph for Overview tab
with tabs[0]:
    # Page title
      st.title("What Influences Life Expectancy in the US")
      st.markdown("""
<style>
.custom-text {
    line-height: 2; /* You can adjust this value as needed */
}
</style>
<div class="custom-text">
In this dashboard, we aim to investigate the discrepancy between high healthcare expenditure in the United States and comparatively lower life expectancy.Despite allocating significant resources to healthcare, the United States experiences challenges in achieving optimal life expectancy compared to other affluent nations.To explore this phenomenon further, we have analyzed several contributing factors that may play a role in shaping life expectancy trends.These factors include smoking, obesity, homicides, opioid overdoses, and road accidents.By examining these factors, we can gain insights into potential explanations for the lower life expectancy in the United States despite its high healthcare expenditure.Furthermore, our analysis will allow us to provide recommendations and steps that the US can take to address this issue.
</div>
""", unsafe_allow_html=True)
# Load and display the image
     # Load and display the image
      image = "INCREASE-LIFESPAN-750x410.png"
      st.image(image, width= 1400, caption="Image")
             
    
    #life expectancy
      
with tabs[1]:
    # Page title
      st.title("Life Expectancy ")
      
       
    # Load the health expenditure data
      data = pd.read_csv("DP_LIVE_09062023031048950.csv")
    
    # Define the selected countries and their corresponding labels
      selected_countries = {"ESP": "Spain", "JPN": "Japan", "AUS": "Australia", "DEU": "Germany", "FRA": "France", "USA": "United States", "CHE": "Switzerland"}
    
    # Filter the data for the selected countries
      filtered_data = data[data['LOCATION'].isin(selected_countries.keys())]
    
    # Filter the data for USD_CAP measure
      filtered_data_usd = filtered_data[filtered_data['MEASURE'] == 'USD_CAP']
    
    # Update the country labels in the data
      filtered_data_usd['LOCATION'] = filtered_data_usd['LOCATION'].map(selected_countries)
    
    # Define selectbox for country selection
      country_select1 = st.selectbox('Select Country for Health Expenditure:', options=['All']+list(selected_countries.values()), index=0, key='select1_health')
    
    # Filter data based on the selected country
      if country_select1 != 'All':
        filtered_data_usd = filtered_data_usd[filtered_data_usd['LOCATION'] == country_select1]
    
    # Plot the line graph for health expenditure
      fig1 = px.line(filtered_data_usd, x="TIME", y="Value", color="LOCATION")
    
    # Define color for the US line and other countries
      for trace in fig1.data:
        if trace.name == "United States":
            trace.line.color = "red"
        else:
            trace.line.color = "gray"
    
    # Update the axis labels and title for health expenditure
      fig1.update_layout(xaxis_title="Year", yaxis_title="Value in USD_CAP", title="Health Expenditure in Rich Countries",
                       plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    
    # Load the life expectancy data
      data2 = pd.read_csv("DP_LIVE_09062023034900901.csv")
    
    # Filter the data for the selected countries
      filtered_data2 = data2[data2['LOCATION'].isin(selected_countries.keys())]
    
    # Update the country labels in the data
      filtered_data2["LOCATION"] = filtered_data2["LOCATION"].map(selected_countries)
    
    # Define selectbox for country selection
      country_select2 = st.selectbox('Select Country for Life Expectancy:', options=['All']+list(selected_countries.values()), index=0, key='select2_life')
    
    # Filter data based on the selected country
      if country_select2 != 'All':
        filtered_data2 = filtered_data2[filtered_data2['LOCATION'] == country_select2]
    
    # Plot the line graph for life expectancy
      fig2 = px.line(filtered_data2, x="TIME", y="Value", color="LOCATION")
    
    # Define color for the US line and other countries
      for trace in fig2.data:
        if trace.name == "United States":
            trace.line.color = "red"
        else:
            trace.line.color = "gray"
    
    # Update the axis labels and title for life expectancy
      fig2.update_layout(xaxis_title="Year", yaxis_title="Life Expectancy", title="Life Expectancy in Selected Countries",
                       plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    
    # Render the selectboxes and the plots side by side using st.columns
      col1, col2 = st.columns(2)
      with col1:
        st.plotly_chart(fig1)
    
      with col2:
        st.plotly_chart(fig2)



    
# Data and visualization for Smoking 
# Diseases tab
with tabs[2]:
    st.title("Diseases")
   
    
    
    # Load the dataset for Sales of Cigarettes
    data1 = pd.read_csv("sales-of-cigarettes-per-adult-per-day (1).csv")  
    
    # Define the selected countries
    selected_countries = ["Spain", "Croatia", "Japan", "Austria", "Germany", "France", "United States", "Switzerland"]
    
    # Filter the data for the selected countries
    filtered_data1 = data1[data1['Entity'].isin(selected_countries)]

    # Define the range of years
    min_year1 = filtered_data1["Year"].min()
    max_year1 = filtered_data1["Year"].max()

    # Set up Streamlit app
    st.title("Sales of Cigarettes")
    st.write("Select the year range:")

    # Get the selected year range from the slider
    selected_years1 = st.slider("Select Year Range", min_value=int(min_year1), max_value=int(max_year1), value=(int(min_year1), int(max_year1)))


    # Filter the data based on the selected year range
    filtered_data1_years = filtered_data1[(filtered_data1["Year"] >= selected_years1[0]) & (filtered_data1["Year"] <= selected_years1[1])]

    # Display the filtered data
    st.write("Filtered Data:")
    st.dataframe(filtered_data1_years)

   # Plot the line graph for sales of cigarettes
    fig1 = go.Figure()

    for entity in selected_countries:
        entity_data = filtered_data1_years[filtered_data1_years["Entity"] == entity]
        fig1.add_trace(go.Scatter(x=entity_data["Year"], y=entity_data["Sales of cigarettes per adult per day (International Smoking Statistics (2017)) "],
                                  mode="lines", name=entity, line=dict(color=colors1[entity]))



# Update the layout
    fig1.update_layout(title="Sales of Cigarettes Per Adult Per Day, {} to {}".format(selected_years1[0], selected_years1[1]),
                   yaxis_title="Sales of Cigarettes", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')

    
    # Set color mapping
    colors1 = {"United States": "red", "Spain": "gray", "Croatia": "gray", "Japan": "gray", "Austria": "gray", "Germany": "gray", "France": "gray", "Switzerland": "gray"}
    
    # Apply color mapping to lines
    for trace in fig1.data:
        entity = trace.name
        trace.line.color = colors1[entity]
    
    # Load the dataset for Death Rate from Smoking
    data2 = pd.read_csv("death-rate-smoking.csv")  
    
    # Filter the data for the selected countries
    filtered_data2 = data2[data2['Entity'].isin(selected_countries)]
    
    # Define the range of years
    min_year2 = filtered_data2["Year"].min()
    max_year2 = filtered_data2["Year"].max()
    
    # Get the selected year range from the slider
    selected_years2 = st.slider("Select Year Range", min_value=int(min_year2), max_value=int(max_year2), value=(int(min_year2), int(max_year2)))

    
    # Filter the data based on the selected year range
    filtered_data2_years = filtered_data2[(filtered_data2["Year"] >= selected_years2[0]) & (filtered_data2["Year"] <= selected_years2[1])]
    
    # Create the heatmap
    fig2 = go.Figure(data=go.Heatmap(
        z=filtered_data2_years['Deaths - Cause: All causes - Risk: Smoking - Sex: Both - Age: Age-standardized (Rate)'].values,
        x=filtered_data2_years['Year'],
        y=filtered_data2_years['Entity'],
        colorscale='Reds',
        colorbar=dict(title='Death rate')
    ))
    
    fig2.update_layout(
        title={
            'text': 'Death rate from smoking, {} to {}<br><sub>Estimated annual number of deaths attributed to smoking per 100,000 people.</sub>'.format(selected_years2[0], selected_years2[1]),
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis=dict(title='Year'),
        yaxis=dict(title='Country')
    )
    
    # Create columns for the graphs
    col1, col2 = st.columns(2)
    
    # Display the graphs in the columns
    with col1:
        st.plotly_chart(fig1)
    
    with col2:
        st.plotly_chart(fig2)

    
    # Data and visualization for Obesity and opioid overdoeses tab
    
    
    # Load the dataset for Death Rate from Obesity
    data3 = pd.read_csv("death-rate-from-obesity.csv")
    
    # Define the selected countries
    selected_countries = ["Spain", "Japan", "Austria", "Germany", "France", "United States", "Switzerland"]
    
    # Filter the data for the selected countries
    filtered_data3 = data3[data3['Entity'].isin(selected_countries)]
    
    # Define the range of years
    min_year3 = filtered_data3["Year"].min()
    max_year3 = filtered_data3["Year"].max()
    
    selected_years3 = st.slider("Select Year Range", min_value=int(min_year3), max_value=int(max_year3), value=(int(min_year3), int(max_year3)), key="slider3")


    # Filter the data based on the selected year range
    filtered_data3_years = filtered_data3[(filtered_data3["Year"] >= selected_years3[0]) & (filtered_data3["Year"] <= selected_years3[1])]
    
    # Plot the line graph for Obesity
    fig3 = px.line(filtered_data3_years, x="Year", y="Deaths - Cause: All causes - Risk: High body-mass index - Sex: Both - Age: Age-standardized (Rate)", color="Entity")
    
    # Apply color mapping and customize line and marker properties
    for trace in fig3.data:
        entity = trace.name
        if entity == "United States":
            trace.line.color = "red"
            trace.mode = "lines+markers"
            trace.marker.symbol = "circle"
            trace.marker.size = 6
        else:
            trace.line.color = "gray"
            trace.mode = "lines"
    
    # Update the title and axis labels
    fig3.update_layout(
        title={
            'text': 'Death Rate from Obesity, {} to {}<br><sub>Estimated annual number of deaths attributed to obesity per 100,000 people.</sub>'.format(selected_years3[0], selected_years3[1]),
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Year",
        yaxis_title="Death Rate",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # Load the dataset for Opioid Overdoses
    data_opioid = pd.read_csv("death-rate-from-opioid-use.csv")
    
    # Create the choropleth map
    fig_opioid = px.choropleth(data_opioid,
                               locations="Code",
                               locationmode="ISO-3",
                               color="Deaths - Opioid use disorders - Sex: Both - Age: Age-standardized (Rate)",
                               hover_name="Entity",
                               animation_frame="Year",
                               color_continuous_scale="Reds")
    
    # Update the layout
    fig_opioid.update_geos(projection_type="equirectangular",
                           showcountries=True,
                           showcoastlines=True)
    fig_opioid.update_layout(
        title={
            'text': 'Death rate from opioid overdoses, 1990 to 2019',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        legend_title_text="Death Rate",
        coloraxis_colorbar=dict(title="Rate per 100,000 population"),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # Create columns for the graphs
    col1, col2 = st.columns(2)
    
    # Display the graphs in the columns
    with col1:
        st.plotly_chart(fig3)
    
    with col2:
        st.plotly_chart(fig_opioid)

#homicide and road accidents

    # Data for Homicide
    data_homicide = pd.read_csv("homicide-rate.csv")
    selected_countries = ["Spain", "Japan", "Austria", "Germany", "France", "United States", "Switzerland"]
    filtered_data_homicide = data_homicide[data_homicide['Entity'].isin(selected_countries)]
    min_year_homicide = filtered_data_homicide["Year"].min()
    max_year_homicide = filtered_data_homicide["Year"].max()
    selected_years_homicide = st.slider("Select Year Range for Homicide", key="homicide_slider1", min_value=int(min_year_homicide), max_value=int(max_year_homicide), value=(int(min_year_homicide), int(max_year_homicide)))
    filtered_data_homicide_years = filtered_data_homicide[(filtered_data_homicide["Year"] >= selected_years_homicide[0]) & (filtered_data_homicide["Year"] <= selected_years_homicide[1])]
    colors_homicide = {"United States": "red"}
    colors_homicide.update({country: "gray" for country in selected_countries if country != "United States"})
    fig_homicide = px.line(filtered_data_homicide_years, x="Year", y="Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Rate)", color="Entity")
    for trace in fig_homicide.data:
        entity = trace.name
        if entity == "United States":
            trace.line.color = "red"
            trace.mode = "lines+markers"
            trace.marker.symbol = "circle"
            trace.marker.size = 6
        else:
            trace.line.color = "gray"
            trace.mode = "lines"
    fig_homicide.update_layout(
        title={
            'text': 'Death Rate from Homicide, {} to {}<br><sub>Annual number of deaths from homicide per 100,000 people.</sub>'.format(selected_years_homicide[0], selected_years_homicide[1]),
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Year",
        yaxis_title="Death Rate",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # Road Injuries
    data_road = pd.read_csv("death-rates-road-incidents 2.csv")
    filtered_data_road = data_road[data_road['Entity'].isin(selected_countries)]
    min_year_road = filtered_data_road['Year'].min()
    max_year_road = filtered_data_road['Year'].max()
    selected_years_road = st.slider("Select Year Range for Road Injuries", key="road_injuries_slider1", min_value=int(min_year_road), max_value=int(max_year_road), value=(int(min_year_road), int(max_year_road)))

    filtered_data_years_road = filtered_data_road[(filtered_data_road['Year'] >= selected_years_road[0]) & (filtered_data_road['Year'] <= selected_years_road[1])]
    fig_road = px.area(filtered_data_years_road, x='Year', y='Deaths - Road injuries - Sex: Both - Age: Age-standardized (Rate)', color='Entity')
    colors_road = {"United States": "red", "Spain": "gray", "Japan": "gray", "Austria": "gray", "Germany": "gray", "France": "gray", "Switzerland": "gray"}
    for trace in fig_road.data:
        entity = trace.name
        trace.fillcolor = colors_road[entity]
        trace.line.color = "white"
    fig_road.update_layout(
        title={
            'text': 'Death rate from road injuries, 1990 to 2019<br><sub>The annual number of deaths from road injuries per 100,000 people.</sub>',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        yaxis_title="Death Rate",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # Create columns for the graphs
    col1, col2 = st.columns(2)
    
    # Display the graphs in the columns
    with col1:
        st.plotly_chart(fig_homicide)
    
    with col2:
        st.plotly_chart(fig_road)
