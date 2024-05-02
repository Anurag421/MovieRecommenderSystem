import pandas as pd
import streamlit as st
import pickle
st.title("Movie Recommender System")


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in movies_list:
        movies_id = i[0]
        #fetch posters of the recommended movies from API


        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

similarity = pickle.load(open('similarity.pkl','rb'))

movies_dict = pickle.load(open('movies_d.pkl','rb'))
movies = pd.DataFrame(movies_dict)

selected_movie_name = st.selectbox('Enter the movie name ',
movies['title'].values)


if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)