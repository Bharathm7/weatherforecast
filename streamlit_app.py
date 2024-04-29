import streamlit as st;
import plotly.express as px;
from backend import get_data

st.title("WEATHER FORCAST");
place = st.text_input("enter the place",value='bangalore');
days = st.slider("how many days",min_value=1,max_value=5)
option = st.selectbox("enter the kind",('temperature','sky','humidity'))

st.subheader(f"{place}'s weather forecast for the next {days} days");
if option == 'temperature':
    filter = get_data(place,days);
    temp = [dict["main"]["temp"] for dict in filter];
    days = [dict["dt_txt"] for dict in filter];
    figure = px.line(x=days,y=temp,labels={'x':'days','y':'temperature'})
    st.plotly_chart(figure);
if option == 'sky':
    filter = get_data(place,days);
    sky = [dict["weather"][0]["main"] for dict in filter]
    days = [dict["dt_txt"] for dict in filter]
    humidity = [dict["main"]["humidity"] for dict in filter]
    figure = px.strip(x=days,y=sky,labels={'x':'days','y':'sky','z':'humidity'})
    st.plotly_chart(figure);
if option == 'humidity':
    filter = get_data(place,days);
    humidity = [dict["main"]["humidity"] for dict in filter];
    days = [dict["dt_txt"] for dict in filter]
    humidity = [dict["main"]["humidity"] for dict in filter];
    figure = px.area(x=days,y=humidity,labels={'x':'days','y':'humidity'})
    st.plotly_chart(figure);

st.info("Bharath :sunglasses:")
 
