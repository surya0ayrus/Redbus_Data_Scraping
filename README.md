# Redbus_Data_Scraping

# Redbus Data Scraping and Filtering with Streamlit

## Introduction
The **Redbus Data Scraping and Filtering with Streamlit Application** aims to transform the transportation industry by offering a robust solution for collecting, analyzing, and visualizing bus travel data. Leveraging **Selenium** for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly enhance operational efficiency and strategic planning within the transportation sector.

## Domain
**Transportation**

## Skill Takeaway
- Python scripting
- Selenium for web automation
- Data Collection and Management using SQL
- Building interactive web applications with Streamlit

## Technology Used
- Python 3.9
- MySQL 8.0
- Streamlit
- Selenium

## Features of the Application

### Retrieve Bus Information
Utilizing Selenium, the application automates the web browsing process to efficiently scrape bus details from Redbus. This involves interacting with web elements such as input fields and buttons, managing page loads, and extracting necessary details from search results.

### Store Data in Database
Collected bus detail data is transformed into Pandas DataFrames. A new database and its corresponding tables are created using the MySQL connector, allowing for seamless insertion of the scraped data. This database can be accessed and managed within the MySQL environment for further analysis.

### Web Application with Streamlit
The application employs Streamlit to create an interactive platform akin to Redbus. Users can search for bus routes, view available buses, and access crucial information such as departure times and pricing through a user-friendly interface.

## Packages and Libraries
- `pandas` as `pd`
- `mysql.connector`
- `time`
- `streamlit` as `slt`
- `datetime`
- `streamlit_option_menu`
- `selenium.webdriver`

## Conclusion
The Redbus Data Scraping and Filtering with Streamlit Application is a powerful tool for anyone in the transportation sector looking to harness the potential of data. By automating the collection and visualization of bus travel information, this project not only facilitates better decision-making but also contributes to improved operational efficiency.

---

For more details, contributions, or issues, feel free to open an issue or submit a pull request!
