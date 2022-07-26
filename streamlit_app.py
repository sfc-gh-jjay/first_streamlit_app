
#testing

import streamlit 
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('🥑Breakfast Menu')
streamlit.text('🥑Omega 3 and Blueberry Oatmeal')
streamlit.text('🥑Kale....')
streamlit.text('🥑Head-Boiled...)
               
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
               
# interactions 
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
               
streamlit.dataframe =(fruits_to_show)

# Display the table on the page.
               
# pull data 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# sets the fruit list to display in menu
my_fruit_list = my_fruit_list.set_index('Fruit')

# display data
streamlit.dataframe(my_fruit_list)
