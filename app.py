import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time


# kerala bus
lists_k=[]
df_k=pd.read_csv("df_k.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#Andhra bus
lists_A=[]
df_A=pd.read_csv("df_A.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#Telungana bus
lists_T=[]
df_T=pd.read_csv("df_T.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

#Goa bus
lists_g=[]
df_G=pd.read_csv("df_G.csv")
for i,r in df_G.iterrows():
    lists_g.append(r["Route_name"])

#Rajastan bus
lists_R=[]
df_R=pd.read_csv("df_R.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])


# South bengal bus 
lists_SB=[]
df_SB=pd.read_csv("df_SB.csv")
for i,r in df_SB.iterrows():
    lists_SB.append(r["Route_name"])

# Haryana bus
lists_H=[]
df_H=pd.read_csv("df_H.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])

#Assam bus
lists_AS=[]
df_AS=pd.read_csv("df_AS.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv("df_UP.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

#West bengal bus
lists_WB=[]
df_WB=pd.read_csv("df_WB.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])

#setting up streamlit page
slt.set_page_config(layout="wide")

web=option_menu(menu_title="🚌OnlineBus",
                options=["Home","📍States and Routes"],
                icons=["house","info-circle"],
                orientation="horizontal"
                )


# Home page setting
if web == "Home":
    # Uncomment this line if you add the image back
    # slt.image("t_500x300.jpg", width=200)
    
    slt.title("🚌 Redbus Data Scraping with Selenium & Dynamic Filtering")
    slt.subheader("Domain: Transportation")
    
    slt.markdown("""
    **Objective:**  
    The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.
    """)
    
    slt.subheader("Overview") 
    slt.markdown("""
    **Selenium:**  
    A tool for automating web browsers, commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages to collect the desired data.
    
    **Pandas:**  
    A powerful library for transforming datasets from CSV format into structured dataframes, facilitating data manipulation, cleaning, and preprocessing to ensure readiness for analysis.
    
    **MySQL:**  
    Helps establish a connection to a SQL database, enabling seamless integration of the transformed dataset and efficient insertion into relevant tables for storage and retrieval.
    
    **Streamlit:**  
    A user-friendly framework for developing interactive web applications for data visualization and analysis.
    """)
    
    slt.subheader("Skills Developed")
    slt.markdown("Selenium, Python, Pandas, MySQL, mysql-connector-python, Streamlit.")

# States and Routes page setting
if web == "📍States and Routes":
    slt.header("Choose Your Bus Route")
    S = slt.selectbox("Select a State", ["Kerala", "Andhra Pradesh", "Telangana", "Goa", "Rajasthan", 
                                          "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"])
    
    col1, col2 = slt.columns(2)
    with col1:
        select_type = slt.radio("Bus Type", ("Sleeper", "Semi-Sleeper", "Others"), index=0)
    with col2:
        select_fare = slt.radio("Fare Range", ("₹50-₹1000", "₹1000-₹2000", "₹2000 and above"), index=0)
    
    TIME = slt.time_input("Select Departure Time")


    