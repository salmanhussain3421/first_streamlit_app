import streamlit
import pandas
streamlit.title('My Parents New Healthier Meal')
streamlit.header('Main')
streamlit.text('Jokes, you are not getting anythign served. Get Out!')
streamlit.header('Life is great')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.header('Giving selection')
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
