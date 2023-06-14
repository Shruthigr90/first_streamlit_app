import streamlit
streamlit.title('my parents New healthy diner')
streamlit.header('BREAKFAST Favorite')
streamlit.text('🥣Omega 3 & blueberry oatmeal')
streamlit.text('🥗Kale , Spinach Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free range Egg')
streamlit.text('🥑🍞 Avacado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

Streamlit.multiselect("pick some fruits :",list(my_fruit_list.index),['Avocado','strabwerry'])

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

