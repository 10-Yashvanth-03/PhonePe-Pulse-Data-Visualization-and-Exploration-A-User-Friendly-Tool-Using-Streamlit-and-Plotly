import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
import time

import mysql.connector
from sqlalchemy import create_engine

#mycurser and engine created to intreact with MYSQL Database
mydb = mysql.connector.connect(host="localhost",user="root",password="Yash")
mycursor = mydb.cursor(buffered=True,)
engine = create_engine("mysql+mysqlconnector://root:Yash@localhost/phonepe") 

#create database and use for table creation
mycursor.execute('create database if not exists phonepe')
mycursor.execute('use phonepe')


#Setting  Streamlit page

#seting page configuration for streamlit
icon=Image.open('E:\Education\Project\Phone Pe\PhonePe.png')
st.set_page_config(page_title='PHONEPE PULSE',
                   page_icon=icon,
                   initial_sidebar_state='expanded',
                   layout='wide')
                   

#setting home page and optionmenu 
with st.sidebar:
    selected = option_menu("Main-Menu",
                        options=["ABOUT", "HOME", "GEO VISUALIZATION","District Wise Bar-Chart","Top Charts"],
                        icons=["info-circle", "house", "globe","bar-chart", "graph-up-arrow"],
                        orientation="vertical")
                        

#setting the details for the option 'ABOUT'
if selected == "ABOUT":
    st.title(':violet[Phonepe] *_Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly_*''')
    
    st.title(':red[Domain:] Fintech')
    st.title(':red[Technologies]')
    st.subheader('- **Github Cloning**') 
    st.subheader('- **Python**') 
    st.subheader('- **Pandas**')  
    st.subheader('- **MySQL**')           
    st.subheader('- **mysql-connector-python**')     
    st.subheader('- **Streamlit**')             
    st.subheader('- **Plotly**')             
                    
    st.title(':red[Overview:]')
    st.markdown('''
            #### :green[**Git**]:  Employed Git for version control and efficient collaboration, enabling seamless cloning of the PhonePe dataset from GitHub.
            
            #### :green[**Pandas**]: Leveraged the powerful Pandas library to transform the dataset from JSON format into a structured dataframe.
            #### Pandas facilitated data manipulation, cleaning, and preprocessing, ensuring the data was ready for analysis.
            
            #### :green[**SQL Alchemy**]: Utilized SQL Alchemy to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
            #### and the data was efficiently inserted into relevant tables for storage and retrieval.
            
            #### :green[**Streamlit**]: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.
            
            #### :green[**Plotly**]: Integrated Plotly, a versatile plotting library, to generate insightful visualizations from the dataset. Plotly's interactive plots,
            #### including geospatial plots and other data visualizations, provided users with a comprehensive understanding of the dataset's contents.''')

    st.title(':red[Developed By:] :blue[Yashvanth]')
    
      


#setting the details for the option 'HOME'
if selected =="HOME":
        col1,col2=st.columns(2)
        with col1:
                st.subheader(':violet[What is Phonepe?]')
                st.markdown('''<h5>PhonePe is a popular digital payments platform in India, offering a range of financial services through its mobile app.
                        Users can make payments, transfer money, recharge phones, pay bills, invest, shop online, and more.<p>
                        <h5>PhonePe has become a preferred choice for millions of users, contributing to India's digital payments revolution.<h5>''',unsafe_allow_html=True)
                
                st.subheader(':violet[what is Phonepe Pulse?]')
                st.markdown('''<h5>PhonePe Pulse provides real-time insights and trends on digital payments across India.
                Its offers comprehensive analytics including transaction volumes, consumer demographics, popular merchant categories,
                geographic trends, transaction values, payment methods, and seasonal fluctuations.<h5>''',unsafe_allow_html=True)
        with col2:
                st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2Vvb2oyaHBqNHZzdm9ycG5lcDEyczk3dDZtcnplamdpbGJudG8xNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gSU4qpRY00OOe6v8I8/giphy-downsized-large.gif)")

        col1,col2=st.columns(2)
        with col1:
                st.image('https://www.phonepe.com/pulsestatic/791/pulse/static/4cb2e7589c30e73dca3d569aea9ca280/1b2a8/pulse-2.webp',use_column_width=True)
        with col2:
                st.write(' ')
                st.subheader(':violet[Discover Insights:]')
                st.markdown('''
                        <h4>Transaction:<h5>Transaction insights involve analyzing customer transaction data to understand behavior and preferences.
                        By examining trends, categorizing transactions,and identifying patterns of india.
                        <h4>User: <h5>User insights refer to analyzing customer demographics, engagement metrics, and feedback.
                        By understanding demographics, tracking engagement of user in India ''',unsafe_allow_html=True)
        


#setting details for the option "Geo Visualization"
if selected =="GEO VISUALIZATION":
        st.title(':violet[GEO VISUALIZATION]')
        
        def ind_geo():
                geo="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                return geo
        
        geo_type = st.radio('Category Selection',["**Transactions**","**Users**"], index = None)
        st.write("You selected:", f"<span style='color:#F8CD47'>{geo_type}</span>", unsafe_allow_html=True)

        if geo_type=="**Transactions**":
                trans_geo_year_wise = st.toggle('Year-Wise')

                if not trans_geo_year_wise:
                        cat=st.radio('Category Selection',["Transaction Amount","Transaction Count"])
                        st.write("You selected:", f"<span style='color:#F8CD47'>{cat}</span>", unsafe_allow_html=True)

                        if cat =="Transaction Amount":
                                st.title(":violet[ Total Transaction Amount for States-Sum of all Year ]")

                                df = pd.read_sql_query('''SELECT state,sum(Transaction_amount) as 'Total Transaction Amount',
                                        AVG(Transaction_amount) as 'Average Transaction Amount'
                                        from agg_transaction
                                        GROUP by state''',con=engine)

                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Transaction Amount','Average Transaction Amount'],
                                        color='Total Transaction Amount',
                                        color_continuous_scale='Viridis',
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)
 
                                
                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.plotly_chart(fig,use_container_width = True)

                        if cat =="Transaction Count":
                                st.title(":violet[Total Transaction Count for States-Sum of all Year]")

                                df = pd.read_sql_query('''SELECT state,sum(Transaction_count) as 'Total Transaction Count',
                                        AVG(Transaction_count) as 'Average Transaction Count'
                                        from agg_transaction
                                        GROUP by state''',con=engine)

                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Transaction Count','Average Transaction Count'],
                                        color='Total Transaction Count',
                                        color_continuous_scale='Viridis',
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)

                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.plotly_chart(fig,use_container_width = True)

                if trans_geo_year_wise:
                        df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from agg_transaction''',con=engine)
                        selected_year = st.select_slider("Select Year",options=df_year['Year'].tolist())
                        trans_geo_quater_wise= st.toggle('Quater-Wise')

                        if not trans_geo_quater_wise:
                                df = pd.read_sql_query('''SELECT state,sum(Transaction_amount) as 'Total Transaction Amount',
                                                AVG(Transaction_amount) as 'Average Transaction Amount',
                                                sum(Transaction_count) as 'Total Transaction Count',
                                                AVG(Transaction_count) as 'Average Transaction Count'
                                                from agg_transaction where year=%s
                                                GROUP by state''',con=engine,params=[(selected_year,)])
                        
                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Transaction Amount','Average Transaction Amount','Total Transaction Count','Average Transaction Count'],
                                        color='Total Transaction Amount',
                                        color_continuous_scale=px.colors.sequential.Plasma,
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)
                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.subheader(f":violet[Total Transaction Amount and Count for States in {selected_year}  ]")
                                st.plotly_chart(fig,use_container_width = True)

                        if trans_geo_quater_wise:
                                df_quater=pd.read_sql_query('''SELECT DISTINCT Quater as 'Quater' from agg_transaction''',con=engine)
                                selected_Quater = st.select_slider("Select Quater",options=df_quater['Quater'].tolist())

                                df = pd.read_sql_query('''SELECT state,sum(Transaction_amount) as 'Total Transaction Amount',
                                                AVG(Transaction_amount) as 'Average Transaction Amount',
                                                sum(Transaction_count) as 'Total Transaction Count',
                                                AVG(Transaction_count) as 'Average Transaction Count'
                                                from agg_transaction where year=%s and Quater=%s
                                                GROUP by state''',con=engine,params=(selected_year, selected_Quater))
                                
                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Transaction Amount','Average Transaction Amount','Total Transaction Count','Average Transaction Count'],
                                        color='Total Transaction Amount',
                                        color_continuous_scale=px.colors.sequential.matter_r,
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)
                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.subheader(f":violet[Total Transaction Amount and Count for States in {selected_year}-Q{selected_Quater}]")
                                st.plotly_chart(fig,use_container_width = True)

        if geo_type=="**Users**":
                user_geo_year_wise = st.toggle('Year-Wise')

                if not user_geo_year_wise:
                        st.title(":violet[ Total Register users Across States-Sum of all Year ]")

                        df = pd.read_sql_query('''SELECT DISTINCT state, SUM(Registered_Users) as 'Total Registered User',
                                        AVG(Registered_Users) as 'Average Register User'
                                        FROM map_user
                                        GROUP BY state''',con=engine)

                        fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                        locations='state',
                                        hover_data=['Total Registered User','Average Register User'],
                                        color='Total Registered User',
                                        color_continuous_scale='Viridis',
                                        mapbox_style="carto-positron",zoom=3.5,
                                        center={"lat": 21.7679, "lon": 78.8718},)

                        fig.update_geos(fitbounds="locations", visible=False)
                        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                        fig.update_layout(height=600)
                        st.plotly_chart(fig,use_container_width = True)

                if user_geo_year_wise:
                        df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from map_user''',con=engine)
                        selected_year = st.select_slider("Select Year",options=df_year['Year'].tolist())
                        user_geo_quater_wise= st.toggle('Quater-Wise')

                        if not user_geo_quater_wise:
                                df = pd.read_sql_query('''SELECT DISTINCT state, SUM(Registered_Users) as 'Total Registered User',
                                                AVG(Registered_Users) as 'Average Register User'
                                                FROM map_user WHERE  year=%s
                                                GROUP BY state''',con=engine,params=[(selected_year,)])
                        
                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                locations='state',
                                                hover_data=['Total Registered User','Average Register User'],
                                                color='Total Registered User',
                                                color_continuous_scale=px.colors.sequential.Plasma,
                                                mapbox_style="carto-positron",zoom=3.5,
                                                center={"lat": 21.7679, "lon": 78.8718},)
                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.subheader(f":violet[Total Registered User for States in {selected_year}  ]")
                                st.plotly_chart(fig,use_container_width = True)

                        if user_geo_quater_wise:
                                df_quater=pd.read_sql_query('''SELECT DISTINCT Quater as 'Quater' from map_user''',con=engine)
                                selected_Quater = st.select_slider("Select Quater",options=df_quater['Quater'].tolist())

                                df = pd.read_sql_query('''SELECT DISTINCT state, SUM(Registered_Users) as 'Total Registered User',
                                                AVG(Registered_Users) as 'Average Register User'
                                                FROM map_user WHERE  year=%s and Quater=%s
                                                GROUP BY state''',con=engine,params=(selected_year,selected_Quater))
                        
                                fig = px.choropleth_mapbox(df,geojson=ind_geo(),featureidkey='properties.ST_NM',
                                                locations='state',
                                                hover_data=['Total Registered User','Average Register User'],
                                                color='Total Registered User',
                                                color_continuous_scale=px.colors.sequential.matter_r,
                                                mapbox_style="carto-positron",zoom=3.5,
                                                center={"lat": 21.7679, "lon": 78.8718},)
                                fig.update_geos(fitbounds="locations", visible=False)
                                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                                fig.update_layout(height=600)
                                st.subheader(f":violet[Total Registered User for States in {selected_year}-Q{selected_Quater} ]")
                                st.plotly_chart(fig,use_container_width = True)


#setting details for the option "District Wise Bar-Chart"
if selected =="District Wise Bar-Chart":
        st.title(':violet[District Wise Bar-Chart]')
        
        query_unique_States = "SELECT DISTINCT State FROM map_transaction order by State"   #To get Unique State Name
        unique_States = pd.read_sql_query(query_unique_States, engine) 

        selected_state = st.selectbox('Select State Name:', unique_States['State'])   
        
        Type = st.radio('Category Selection',["**Transactions**","**Users**"], index = None)
        st.write("You selected:", f"<span style='color:#F8CD47'>{Type}</span>", unsafe_allow_html=True)
        
        if Type=="**Transactions**":
                year_and_Quater_wise = st.toggle('Year And Quater Wise')

                if not year_and_Quater_wise:
                        st.title(":violet[ TOTAL TRANSACTIONS DISTRICT WISE-Sum of all Year ]")

                        mycursor.execute(f'''select State, District,year,Quater, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount 
                                             from map_transaction 
                                             where State = '{selected_state}'
                                             group by State, District,year,Quater 
                                             order by state,district''')
                
                        df1 = pd.DataFrame(mycursor.fetchall(), columns=['State','District','Year','Quater',
                                                                        'Total_Transactions','Total_amount'])
                        fig = px.bar(df1,
                                title= selected_state,
                                x="District",
                                y="Total_Transactions",
                                orientation='v',
                                color='Total_amount',
                                color_continuous_scale=px.colors.sequential.Agsunset)
                        st.plotly_chart(fig,use_container_width=True) 


                if year_and_Quater_wise:
                        
                        df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from map_transaction''',con=engine)
                        Year = st.select_slider("Select Year",options=df_year['Year'].tolist())
                        df_quater=pd.read_sql_query('''SELECT DISTINCT Quater as 'Quater' from map_transaction''',con=engine)
                        Quater = st.select_slider("Select Quater",options=df_quater['Quater'].tolist())
                        
                        st.title(f":violet[TOTAL TRANSACTIONS DISTRICT WISE in {Year}-Q{Quater} ]")  

                        mycursor.execute(f'''select State, District,year,Quater, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from map_transaction 
                                             where year = {Year} and Quater = {Quater} and State = '{selected_state}' 
                                             group by State, District,year,Quater 
                                             order by state,district''')
                
                        df1 = pd.DataFrame(mycursor.fetchall(), columns=['State','District','Year','Quater',
                                                                        'Total_Transactions','Total_amount'])
                        fig = px.bar(df1,
                                title= selected_state,
                                x="District",
                                y="Total_Transactions",
                                orientation='v',
                                color='Total_amount',
                                color_continuous_scale=px.colors.sequential.Agsunset)
                        st.plotly_chart(fig,use_container_width=True) 

        if Type=="**Users**":
                year_and_Quater_wise = st.toggle('Year And Quater Wise')

                if not year_and_Quater_wise:
                        st.title(":violet[TOTAL USERS DISTRICT WISE-Sum of all Year ]")

                        mycursor.execute(f'''select State,year,Quater,District,sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_Appopens 
                                             from map_user 
                                             where State = '{selected_state}'
                                             group by State, District,year,Quater 
                                             order by state,district''')
                
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State','year', 'quarter', 'District', 'Total_Users','Total_Appopens'])
                        df.Total_Users = df.Total_Users.astype(int)
                        
                        fig = px.bar(df,
                                title=selected_state,
                                x="District",
                                y="Total_Users",
                                orientation='v',
                                color='Total_Users',
                                color_continuous_scale=px.colors.sequential.Agsunset)
                        st.plotly_chart(fig,use_container_width=True)

                if year_and_Quater_wise:
                        
                        df_year=pd.read_sql_query('''SELECT DISTINCT year as 'Year' from map_user''',con=engine)
                        Year = st.select_slider("Select Year",options=df_year['Year'].tolist())
                        df_quater=pd.read_sql_query('''SELECT DISTINCT Quater as 'Quater' from map_user''',con=engine)
                        Quater = st.select_slider("Select Quater",options=df_quater['Quater'].tolist())
                        
                        st.title(f":violet[TOTAL USERS DISTRICT WISE in {Year}-Q{Quater}]") 
                        mycursor.execute(f'''select State,year,Quater,District,sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_Appopens 
                                             from map_user 
                                             where year = {Year} and Quater = {Quater} and state = '{selected_state}' 
                                             group by State, District,year,Quater 
                                             order by state,district''')
                                
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State','year', 'quarter', 'District', 'Total_Users','Total_Appopens'])
                        df.Total_Users = df.Total_Users.astype(int)
                        
                        fig = px.bar(df,
                                title=selected_state,
                                x="District",
                                y="Total_Users",
                                orientation='v',
                                color='Total_Users',
                                color_continuous_scale=px.colors.sequential.Agsunset)
                        st.plotly_chart(fig,use_container_width=True)                                          




#setting details for the option "Top Charts"
if selected == "Top Charts":
    st.title(":violet[Top Charts]")
    Type = st.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    with colum1:
        Year = st.slider("**Year**", min_value=2018, max_value=2024)
        Quater = st.slider("**Quater**", min_value=1, max_value=4)
    
    with colum2:
        st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quater.
                - Top 10 Highest and Lowest State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 Highest snd Lowest State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                - Top Payment Type based on Total amount spent and Total Transcation. 
                """,icon="🔍"
                )
        


    #Top Charts - TRANSACTIONS    
    if Type == "Transactions":
        col1,col2,col3 = st.columns([1,1,1],gap="small")
        
        # Pie-Chart for Top 10 Highest State based on Total number of transaction and Total amount spent on phonepe.
        with col1:
            st.markdown("### :violet[State]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from agg_transaction where year = {Year} and quater = {Quater} group by state order by Total desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
                fig = px.pie(df, values='Total_Amount',
                                names='State',
                                title=(f"Top 10 Highest in {Year}-Q{Quater}"),
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})
                                

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)
        
        # Bar-Chart for Top 10 lowest State based on Total number of transaction and Total amount spent on phonepe.
        with col1:
            st.markdown("### :violet[State]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from agg_transaction where year = {Year} and quater = {Quater} group by state order by Total asc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
                df = df.sort_values(by='Transactions_Count', ascending=False)
                fig = px.bar(df,
                                title=(f"Top 10 Lowest in {Year}-Q{Quater}"),
                                x="Total_Amount",
                                y="State",
                                orientation='h',
                                color='Transactions_Count',
                                color_continuous_scale=px.colors.sequential.Agsunset)

                st.plotly_chart(fig,use_container_width=True)   
        
        # Pie-Chart for Top 10 Highest District based on Total number of transaction and Total amount spent on phonepe.    
        with col2:
            st.markdown("### :violet[District]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select district , sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total from map_transaction where year = {Year} and quater = {Quater} group by district order by Total desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])

                fig = px.pie(df, values='Total_Amount',
                                names='District',
                                title=(f"Top 10 Highest in {Year}-Q{Quater}"),           
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)
        
        # Bar-Chart for Top 10 Lowest District based on Total number of transaction and Total amount spent on phonepe.
        with col2:
            st.markdown("### :violet[District]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select district , sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total from map_transaction where year = {Year} and quater = {Quater} group by district order by Total desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])

                fig = px.bar(df,
                                title=(f"Top 10 Lowest in {Year}-Q{Quater}"),
                                x="Total_Amount",
                                y="District",
                                orientation='h',
                                color='Transactions_Count',
                                color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)   
            

        # Pie-Chart for Top 10 Highest Pincode based on Total number of transaction and Total amount spent on phonepe.
        with col3:
            st.markdown("### :violet[Pincode]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select pincode, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from top_transaction where year = {Year} and quater = {Quater} group by pincode order by Total desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
                fig = px.pie(df, values='Total_Amount',
                                names='Pincode',
                                title=(f"Top 10 Highest in {Year}-Q{Quater}"),
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)

        # Pie-Chart for Top 10 Lowest Pincode based on Total number of transaction and Total amount spent on phonepe.
        with col3:
            st.markdown("### :violet[Pincode]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select pincode, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from top_transaction where year = {Year} and quater = {Quater} group by pincode order by Total asc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
                
                fig = px.pie(df, values='Total_Amount',
                                names='Pincode',
                                title=(f"Top 10 Lowest in {Year}-Q{Quater}"),
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Transactions_Count'],
                                labels={'Transactions_Count':'Transactions_Count'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)
        
        # BAR CHART - TOP PAYMENT TYPE
        with col2:
                st.markdown("## :violet[Top Payment Type]")
                if Year == 2024 and Quater in [2,3,4]:
                        st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
                else:
                        mycursor.execute(f"select Transaction_type, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from agg_transaction where year= {Year} and Quater = {Quater} group by transaction_type order by Transaction_type")
                        df = pd.DataFrame(mycursor.fetchall(), columns=['Transaction_type', 'Total_Transactions','Total_amount'])
                        df = df.sort_values(by='Transaction_type', ascending=True)
                        fig = px.bar(df,
                                title=(f"Transaction Types vs Total_Transactions in {Year}-Q{Quater}"),
                                x="Transaction_type",
                                y="Total_Transactions",
                                orientation='v',
                                color='Total_amount',
                                color_continuous_scale=px.colors.sequential.Agsunset)
                        st.plotly_chart(fig,use_container_width=False)    


    # Top Charts - USERS          
    if Type == "Users":
        col1,col2,col3 = st.columns([1,1,1],gap="small")
        
        # Bar-Chart for Top 10 Highest State based on Total phonepe users and their app opening frequency.
        with col1:
                st.markdown("### :violet[State]")
                if Year == 2024 and Quater in [2,3,4]:
                        st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
                else:
                        mycursor.execute(f"select state, sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_Appopens from map_user where year = {Year} and quater = {Quater} group by state order by Total_Users desc limit 10")
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
                        df = df.sort_values(by='Total_Users', ascending=True)
                        fig = px.bar(df,
                                title=(f"Top 10 Highest in {Year}-Q{Quater}"),
                                x="Total_Users",
                                y="State",
                                orientation='h',
                                color='Total_Users',
                                color_continuous_scale=px.colors.sequential.Agsunset)

                        st.plotly_chart(fig,use_container_width=True)
                
        # Bar-Chart for Top 10 Lowest State based on Total phonepe users and their app opening frequency.
        with col1:
                st.markdown("### :violet[State]")
                if Year == 2024 and Quater in [2,3,4]:
                        st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
                else:
                        mycursor.execute(f"select state, sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_Appopens from map_user where year = {Year} and quater = {Quater} group by state order by Total_Users asc limit 10")
                        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
                        df = df.sort_values(by='Total_Users', ascending=False)
                        fig = px.bar(df,
                                title=(f"Top 10 Lowest in {Year}-Q{Quater}"),
                                x="Total_Users",
                                y="State",
                                orientation='h',
                                color='Total_Users',
                                color_continuous_scale=px.colors.sequential.Agsunset)

                        st.plotly_chart(fig,use_container_width=True)
                

        # Bar-Chart for Top 10 Highest District based on Total phonepe users and their app opening frequency. 
        with col2:
            st.markdown("### :violet[District]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select district, sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_Appopens from map_user where year = {Year} and quater = {Quater} group by district order by Total_Users desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
                df.Total_Users = df.Total_Users.astype(float)
                df = df.sort_values(by='Total_Users', ascending=True)
                fig = px.bar(df,
                                title=(f"Top 10 Highest in {Year}-Q{Quater}"),
                                x="Total_Users",
                                y="District",
                                orientation='h',
                                color='Total_Users',
                                color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)
        
        # Bar-Chart for Top 10 Lowest District based on Total phonepe users and their app opening frequency.
        with col2:
            st.markdown("### :violet[District]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select district, sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_Appopens from map_user where year = {Year} and quater = {Quater} group by district order by Total_Users asc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
                df.Total_Users = df.Total_Users.astype(float)
                df = df.sort_values(by='Total_Users', ascending=False)
                fig = px.bar(df,
                                title=(f"Top 10 Lowest in {Year}-Q{Quater}"),
                                x="Total_Users",
                                y="District",
                                orientation='h',
                                color='Total_Users',
                                color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)
        
        
        # Bar-Chart for Top 10 mobile brands and its percentage based on the how many people use phonepe.
        with col2:
            st.markdown("### :violet[Mobile Brands]")
            if Year in [2022] and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2022,2023,2024 Qtr 1,2,3,4")
            elif Year in [2023,2024] and Quater in [1,2,3,4]:
                st.markdown("#### No Data to Display for 2023,2024 Qtr 1,2,3,4")
            
            else:
                mycursor.execute(f"select User_brand, sum(User_count) as Total_Count, avg(User_percentage)*100 as Avg_Percentage from agg_user where year = {Year} and quater = {Quater} group by User_brand order by Total_Count desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
                df = df.sort_values(by='Total_Users', ascending=True)
                fig = px.bar(df,
                             title=(f"Top 10 mobile brands in {Year}-Q{Quater}"),
                             x="Total_Users",
                             y="Brand",
                             orientation='h',
                             color='Avg_Percentage',
                             color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)       
                
        
        # Pie-Chart for Top 10 Highest Pincode based on Total phonepe users and their app opening frequency.
        with col3:
            st.markdown("### :violet[Pincode]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select Pincode, sum(Registered_Users) as Total_Users from top_user where year = {Year} and quater = {Quater} group by Pincode order by Total_Users desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Users'])
                fig = px.pie(df, values='Total_Users',
                                names='Pincode',
                                title=(f"Top 10 Highest in {Year}-Q{Quater}"),
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Total_Users'],
                                labels={'Total_Users':'Total_Users'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)      
                
        # Pie-Chart for Top 10 Lowest Pincode based on Total phonepe users and their app opening frequency.
        with col3:
            st.markdown("### :violet[Pincode]")
            if Year == 2024 and Quater in [2,3,4]:
                st.markdown("#### No Data to Display for 2024 Qtr 2,3,4")
            else:
                mycursor.execute(f"select Pincode, sum(Registered_Users) as Total_Users from top_user where year = {Year} and quater = {Quater} group by Pincode order by Total_Users asc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Users'])
                fig = px.pie(df, values='Total_Users',
                                names='Pincode',
                                title=(f"Top 10 Lowest in {Year}-Q{Quater}"),
                                color_discrete_sequence=px.colors.sequential.Agsunset,
                                hover_data=['Total_Users'],
                                labels={'Total_Users':'Total_Users'})

                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig,use_container_width=True)
        
       


