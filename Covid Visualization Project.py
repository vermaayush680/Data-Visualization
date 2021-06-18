"""
Covid Data Visualization

We are going to use the below data for visualization

https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/06-13-2021.csv

Also we are going to use Matplotlib, Seaborn and Plotly for visualization

"""

#Importing all the necessary modules

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Saving our file path in a variable

## MM-DD-YYYY
path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/06-16-2021.csv'

#Reading our data
df = pd.read_csv(path)

#Saving our csv in offline mode for future reference
df.to_csv('CovidData.csv')

#Getting the number of empty cells or NAN values in each column
df.info()

#Dropping/Removing all the columns not required for our project
#axis = 0 for row
#axis = 1 for column

df = df.drop(['FIPS',
         'Admin2',
         'Province_State',
         'Last_Update',
         'Lat',
         'Combined_Key',
         'Incident_Rate',
         'Case_Fatality_Ratio'],axis=1)

#Renaming the 'Country_Region' column to 'Country'
df = df.rename(columns={'Country_Region':'Country'})

#Dropping another unnecessary column
df = df.drop(['Long_'],axis=1)

#Saving our changed csv in offline mode for future reference
df.to_csv('CovidData.csv')

#Grouping similar Country columns by summing them
world = df.groupby('Country').sum()

#And Creating a new indexing
world = world.reset_index()

#Sorting the values in descending order
world = world.sort_values(by=['Confirmed'],ascending=False)

#Using the Top 20 Countries for our visualization
top20 = world[0:20]

#Plotting the Confirmed Cases vs Country bar graph
plt.figure(figsize=(8,7))
x1=top20['Country']
y1=top20['Confirmed']
sns.barplot(x=y1,y=x1)
plt.title('Top 20 Countries with confirmed cases')
plt.show()

#Getting the Top 10 countries out of the Top 20
#And Visualizing a Confirmed Vs Recovered graph
#keeping the Country as the constant axis

top10 = top20[0:10]

#Visualizing the graph
plt.figure(figsize=(8,7))
x1=top10['Country']
y1=top10['Confirmed']
z1=top10['Recovered']
sns.barplot(x=y1,y=x1,color='#ff33cc',label='Confirmed Cases')
plt.barh(x1,z1,color='#66ff33',height=0.3,label='Recovered Cases')
plt.legend()
plt.xlabel('Total Cases')
plt.title('Top 10 Countries with confirmed and recovered cases')
plt.show()

#Creating a choropleth world map
fig = px.choropleth(world,
              locations='Country',
              locationmode='country names',
              hover_name='Country',
              color='Confirmed',
              color_continuous_scale='peach',range_color=[1000,1e7])
fig.show()


