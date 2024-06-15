# PhonePe-Pulse-Data-Visualization-and-Exploration-A-User-Friendly-Tool-Using-Streamlit-and-Plotly

## Approach
 - Data extraction: Clone the Github using scripting to fetch the data from the
 Phonepe pulse Github repository and store it in a suitable format such as CSV
 or JSON.

- Data transformation: Use a scripting language such as Python, along with
  libraries such as Pandas, to manipulate and pre-process the data. This may
  include cleaning the data, handling missing values, and transforming the data
  into a format suitable for analysis and visualization.

- Database insertion: Use the "mysql-connector-python" library in Python to
  connect to a MySQL database and insert the transformed data using SQL
  commands.

- Dashboard creation: Use the Streamlit and Plotly libraries in Python to create
  an interactive and visually appealing dashboard. Plotly's built-in geo map
  functions can be used to display the data on a map and Streamlit can be used
  to create a user-friendly interface with multiple dropdown options for users to
  select different facts and figures to display.

- Data retrieval: Use the "mysql-connector-python" library to connect to the
  MySQL database and fetch the data into a Pandas dataframe. Use the data in
  the dataframe to update the dashboard dynamically.

- Deployment: Ensure the solution is secure, efficient, and user-friendly. Test
  the solution thoroughly and deploy the dashboard publicly, making it
  accessible to users.




## THE MAIN COMPONENTS OF DASHBOARD ARE

    1 "GEO VISUALIZATION"
    
    2 "District Wise Bar-Chart" 
    
    3 "Top Charts"
   
### 1 Geo-Visualization:
    The India map shows the Total Transactions and Users of PhonePe in state wise.we can also see Total Transaction and 
    User details by Year and Quater wise

### 2 District Wise Bar-Chart
     In this page we can total transaction and User details in district wise in bar chart. By selecting year and quater 
     wise we can see total transaction and User details by Year and Quater wise for every district by selecting State Name.

### 3 Top Charts 
     In this we can get insights like, 
          - Overall ranking on a particular Year and Quater.
          - Top 10 Highest and Lowest State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
          - Top 10 Highest snd Lowest State, District, Pincode based on Total phonepe users and their app opening frequency.
          - Top 10 mobile brands and its percentage based on the how many people use phonepe.
          - Top Payment Type based on Total amount spent and Total Transcation. 
  
    
