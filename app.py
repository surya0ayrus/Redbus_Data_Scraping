import pandas as pd
import mysql.connector
import streamlit as st
from streamlit_option_menu import option_menu

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






# Function to load CSV data
def load_csv_data(filename):
    df = pd.read_csv(filename)
    return df['Route_name'].tolist()

# Load data for all states
states_data = {
    "Kerala": load_csv_data("df_k.csv"),
    "Andhra Pradesh": load_csv_data("df_A.csv"),
    "Telangana": load_csv_data("df_T.csv"),
    "Goa": load_csv_data("df_G.csv"),
    "Rajasthan": load_csv_data("df_R.csv"),
    "South Bengal": load_csv_data("df_SB.csv"),
    "Haryana": load_csv_data("df_H.csv"),
    "Assam": load_csv_data("df_AS.csv"),
    "Uttar Pradesh": load_csv_data("df_UP.csv"),
    "West Bengal": load_csv_data("df_WB.csv")
}

# Setting up streamlit page
st.set_page_config(layout="wide", page_title="OnlineBus")

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #f81009;
    }
    .stSelectbox, .stRadio > div, .stDateInput > div > div > input {
        #background-color: #0e0d0d;
    }
    .stDataFrame {
        #background-color: #0e0d0d;
    }
</style>
""", unsafe_allow_html=True)

# Horizontal menu
selected = option_menu(
    menu_title="🚌 REDBUS 🚍",
    options=["Home", "States and Routes"],
    icons=["house", "geo-alt"],
    menu_icon="bus-front",
    default_index=1,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#ee6a11"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#0e0d0d"},
        "nav-link-selected": {"background-color": "#76c0c0"},
    }
)

# Database connection function
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="redbus",
        auth_plugin='mysql_native_password'  
    )

# Query function
def query_bus_data(route_name, bus_type, fare_min, fare_max, departure_time):
    conn = connect_to_db()
    cursor = conn.cursor()

    bus_type_condition = {
        "Sleeper": "Bus_type LIKE '%Sleeper%'",
        "Semi-Sleeper": "Bus_type LIKE '%Semi Sleeper%'",
        "Others": "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
    }[bus_type]

    query = f"""
    SELECT ID, Bus_name, Bus_type, Start_time, End_time, Total_duration, Price, Seats_Available, Ratings, Route_link
    FROM bus_details 
    WHERE Price BETWEEN {fare_min} AND {fare_max}
    AND Route_name = %s
    AND {bus_type_condition}
    AND Start_time >= %s
    ORDER BY Start_time, Price
    """
    
    cursor.execute(query, (route_name, departure_time))
    result = cursor.fetchall()
    
    conn.close()
    
    return pd.DataFrame(result, columns=[
        "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
        "Price", "Seats_Available", "Ratings", "Route_link"
    ])

if selected == "Home":
    st.title("Welcome to OnlineBus")
    st.write("This application helps you find bus routes and schedules across different states in India.")
    st.title("🚌 Redbus Data Scraping with Selenium & Dynamic Filtering")
    st.subheader("Domain: Transportation")
    
    st.markdown("""
    **Objective:**  
    The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.
    """)
    
    st.subheader("Overview") 
    st.markdown("""
    **Selenium:**  
    A tool for automating web browsers, commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages to collect the desired data.
    
    **Pandas:**  
    A powerful library for transforming datasets from CSV format into structured dataframes, facilitating data manipulation, cleaning, and preprocessing to ensure readiness for analysis.
    
    **MySQL:**  
    Helps establish a connection to a SQL database, enabling seamless integration of the transformed dataset and efficient insertion into relevant tables for storage and retrieval.
    
    **Streamlit:**  
    A user-friendly framework for developing interactive web applications for data visualization and analysis.
    """)
    
    st.subheader("Skills Developed")
    st.markdown("Selenium, Python, Pandas, MySQL, mysql-connector-python, Streamlit.")



elif selected == "States and Routes":
    st.subheader("Choose Your Bus Route")
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected_state = st.selectbox("List of States", list(states_data.keys()))
        select_type = st.radio("Choose bus type", ("Sleeper", "Semi-Sleeper", "Others"))
        
    with col2:
        select_fare = st.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))
        departure_time = st.time_input("Select the time")

    selected_route = st.selectbox("List of routes", states_data[selected_state])

    # Convert fare range to min and max values
    fare_ranges = {
        "50-1000": (50, 1000),
        "1000-2000": (1000, 2000),
        "2000 and above": (2000, 100000)
    }
    fare_min, fare_max = fare_ranges[select_fare]
    
    df_result = query_bus_data(selected_route, select_type, fare_min, fare_max, str(departure_time))
    if not df_result.empty:
        st.dataframe(df_result, use_container_width=True)
    else:
        st.warning("No buses found matching your criteria. Try adjusting your search parameters.")


