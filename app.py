import streamlit as st
import pickle
import pandas as pd
import requests

with open("style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8593abb43e4f99a345f4ff1793d127ad'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    recommended_movies_poster = []
    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id
        #fetch movie poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster
def recommend1(movie):
    movie_index = bollywood_movies[bollywood_movies['title'] == movie].index[0]
    distances = similarity1[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    recommended_movies_poster = []
    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        poster_path = bollywood_movies.iloc[i[0]].poster_path
        #fetch movie poster from API

        recommended_movies.append(bollywood_movies.iloc[i[0]].title)
        recommended_movies_poster.append(poster_path)
    return recommended_movies,recommended_movies_poster


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

bollywood_movies_dict = pickle.load(open('bollywood_movies_dict.pkl', 'rb'))
bollywood_movies = pd.DataFrame(bollywood_movies_dict)
# Load similarity data from Google Drive
similarity = pickle.load(open('similarity.pkl','rb'))
similarity1 = pickle.load(open('similarity1.pkl', 'rb'))


# Display title with two colors
st.markdown('<h1><span style="color: white;">Hey</span><span style="color: rgb(0, 190, 30);">Dude</span></h1>', unsafe_allow_html=True)

st.markdown('<h6><span style="color: white;">Search your</span><span style="color: rgb(190, 13, 13);"> favourite</span><span style="color: white;">movie</span></h6>', unsafe_allow_html=True)

st.markdown('<h3><span style="color: white;">Bollywood</span></h3>', unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Search',
    bollywood_movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend1(selected_movie_name)

    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(names[0])
        st.image(posters[0])

    with col7:
        st.text(names[1])
        st.image(posters[1])

    with col8:
        st.text(names[2])
        st.image(posters[2])

    with col9:
        st.text(names[3])
        st.image(posters[3])

    with col10:
        st.text(names[4])
        st.image(posters[4])

st.markdown('<h3><span style="color: white;">Hollywood</span></h3>', unsafe_allow_html=True)
selected_movie_name1 = st.selectbox(
    'Search',
    movies['title'].values)

if st.button('Recommend_'):
    names, posters = recommend(selected_movie_name1)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

#
#
#
# if st.button('Bollywood'):
#     selected_movie_name = st.selectbox(
#         'Search',
#         bollywood_movies['title'].values)
#
#     if st.button('Recommend'):
#         names, posters = recommend1(selected_movie_name)
#
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1:
#             st.text(names[0])
#             st.image(posters[0])
#
#         with col2:
#             st.text(names[1])
#             st.image(posters[1])
#
#         with col3:
#             st.text(names[2])
#             st.image(posters[2])
#
#         with col4:
#             st.text(names[3])
#             st.image(posters[3])
#
#         with col5:
#             st.text(names[4])
#             st.image(posters[4])

