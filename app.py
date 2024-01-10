import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import pandas as pd  # Corrected import statement

with open('similarity.pxl', 'rb') as file:
    data = pickle.load(file)

similarity = data['similarity']
dataset_dict = data['dataset']

# Convert the dataset dictionary back to a pandas DataFrame if needed
dataset = pd.DataFrame.from_dict(dataset_dict)

def recommendation(movie):
    movie_index = dataset[dataset['title'] == str(movie)].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    final_list = []
    for movie in movie_list:
        print(dataset.iloc[movie[0]]['title'])
        final_list.append(dataset.iloc[movie[0]]['title'])
    return final_list

st.title('Movies Recommendation System')
selected_movie_name = st.selectbox('Search Your Movie', dataset['title'].values)

if st.button('Recommand'):
    movies = recommendation(selected_movie_name)
    st.write(movies)