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


#Setting up Streamlit page
#set up page configuration for streamlit
icon=Image.open('E:\Education\Project\Phone Pe\PhonePe.png')
st.set_page_config(page_title='PHONEPE PULSE',
                   page_icon=icon,
                   initial_sidebar_state='expanded',
                   layout='wide')
                   

#set up home page and optionmenu 
with st.sidebar:
    selected = option_menu("Navigation",
                        options=["ABOUT", "HOME", "GEO VISUALIZATION", "Top Charts"],
                        icons=["info-circle", "house", "globe", "graph-up-arrow"],
                        orientation="vertical")
                        

#setup the detail for the option 'ABOUT'
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

#setup the detail for the option 'HOME'
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
                
                st.subheader(':violet[This Project is Inspired From Phonepe pulse]')
                st.link_button('Go to Phonepe Pulse','https://www.phonepe.com/pulse/')


#setup details for the option "Geo Visualization"
if selected =="GEO VISUALIZATION":
        
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


# MENU 2 - TOP CHARTS
if selected == "Top Charts":
    st.markdown("## :violet[Top Charts]")
    Type = st.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    with colum1:
        Year = st.slider("**Year**", min_value=2018, max_value=2022)
        Quater = st.slider("Quater", min_value=1, max_value=4)
    
    with colum2:
        st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quater.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
        
# Top Charts - TRANSACTIONS    
    if Type == "Transactions":
        col1,col2,col3 = st.columns([1,1,1],gap="small")
        
        with col1:
            st.markdown("### :violet[State]")
            mycursor.execute(f"select state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from agg_transaction where year = {Year} and quater = {Quater} group by state order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                             names='State',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Transactions_Count'],
                             labels={'Transactions_Count':'Transactions_Count'})
                             

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select district , sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total from map_transaction where year = {Year} and quater = {Quater} group by district order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])

            fig = px.pie(df, values='Total_Amount',
                             names='District',
                             title='Top 10',           
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Transactions_Count'],
                             labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select pincode, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from top_transaction where year = {Year} and quater = {Quater} group by pincode order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                             names='Pincode',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Transactions_Count'],
                             labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
# Top Charts - USERS          
    if Type == "Users":
        col1,col2,col3,col4 = st.columns([2,2,2,2],gap="small")
        
        with col1:
            st.markdown("### :violet[Brands]")
            if Year == 2022 and Quater in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")
            else:
                mycursor.execute(f"select User_brand, sum(User_count) as Total_Count, avg(User_percentage)*100 as Avg_Percentage from agg_user where year = {Year} and quater = {Quater} group by User_brand order by Total_Count desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
                fig = px.bar(df,
                             title='Top 10',
                             x="Total_Users",
                             y="Brand",
                             orientation='h',
                             color='Avg_Percentage',
                             color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)   
    
        with col2:
            st.markdown("### :violet[District]")
            mycursor.execute(f"select district, sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_Appopens from map_user where year = {Year} and quater = {Quater} group by district order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.bar(df,
                         title='Top 10',
                         x="Total_Users",
                         y="District",
                         orientation='h',
                         color='Total_Users',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
              
        with col3:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(f"select Pincode, sum(Registered_Users) as Total_Users from top_user where year = {Year} and quater = {Quater} group by Pincode order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Users'])
            fig = px.pie(df,
                         values='Total_Users',
                         names='Pincode',
                         title='Top 10',
                         color_discrete_sequence=px.colors.sequential.Agsunset,
                         hover_data=['Total_Users'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col4:
            st.markdown("### :violet[State]")
            mycursor.execute(f"select state, sum(Registered_Users) as Total_Users, sum(App_Opens) as Total_Appopens from map_user where year = {Year} and quater = {Quater} group by state order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
            fig = px.pie(df, values='Total_Users',
                             names='State',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Total_Appopens'],
                             labels={'Total_Appopens':'Total_Appopens'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        

