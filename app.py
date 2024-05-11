import streamlit as st
from moviesdata import movies

# Helloo welcome to my project :)
# I put all the movies in a different file called moviesdata.py for a neater and clearer code 
# I used Streamlit for the UI design and deployment

# Part 2: Recommendations 
def get_recs(fav_genre):
    movies_rec = [title for title, info in movies.items() if fav_genre in info["Genres"]]
    return movies_rec

# Part 3: Find a movie
def find_movie(search_movie):
    found_movie = [title for title in movies.keys() if search_movie in title]
    return found_movie

# Part 4: Filter Movies
def filter_movies(filter_type, filter_value):
    if filter_type == "rating":
        mvs_filtered = [title for title, info in movies.items() if info.get("Rating") == float(filter_value)]
    elif filter_type == "year":
        mvs_filtered = [title for title, info in movies.items() if info.get("Year") == int(filter_value)]
    else: 
        return None

    return mvs_filtered

# Part 5: Insert Movies
def insert_movie(new_movie, genres, year, runtime, rating, actors):
    movies[new_movie] = {
        "Genres": [genre.strip() for genre in genres.split(",")],
        "Year": int(year) if year else None,
        "Run Time": int(runtime) if runtime else None,
        "Rating": float(rating) if rating else None,
        "Actors": [actor.strip() for actor in actors.split(',')]
    }
    return True

# Part 6: UI WOOHOO!!!

def main():
    st.title('Movie Recommender System 🎭')

    menu = ['Home', 'Get Recommendations', 'Find Movies', 'Filter Movies', 'Insert New Movie']
    choice = st.sidebar.selectbox('Pick an option', menu)

    if choice == 'Home':
        st.write('Hello world! Welcome to the greatest movie recommender system ever 🎞️🍿')
        st.write('Choose an option from the sidebar :)')
        st.write('© 2024 Dana AlSiddig. All Rights Reserved. >:)')

    elif choice == 'Get Recommendations':
        st.header('Get Recommendations 💭')
        fav_genre = st.text_input('Enter your favorite genre:')
        if st.button('Get Recommendations'):
            movies_rec = get_recs(fav_genre)
            if movies_rec:
                st.success("Based on your favorite genre: **{}**, here are some movies you might like: 🎉🎉".format(fav_genre))
                st.write(movies_rec)
            else:
                st.warning("Uh oh... No movies found. 👺")

    elif choice == 'Find Movies':
        st.header('Find Movies 🔍')
        search_movie = st.text_input('Enter movie title or a part of it:')
        if st.button('Find Movies'):
            found_movie = find_movie(search_movie)
            if found_movie:
                st.write("Movies matching your search:")
                st.write(found_movie)
            else:
                st.warning("Whoops! No movies found. 🤣🫵")

    elif choice == 'Filter Movies':
        st.header('Filter Movies 🤺')
        filter_type = st.selectbox('Pick filtering type:', ['Rating', 'Year'])
        filter_value = st.text_input('Enter value:')
        if st.button('Filter Movies'):
            mvs_filtered = filter_movies(filter_type.lower(), filter_value)
            if mvs_filtered:
                st.write("Movies found:")
                st.write(mvs_filtered)
            else:
                st.warning("Uh oh... No movies found. 👺")

    elif choice == 'Insert New Movie':
        st.header('Insert New Movie 👻')
        new_movie = st.text_input('Enter new movie title: 🎟️')
        genres = st.text_input('Enter genres (comma-separated): 🎭')
        year = st.text_input('Enter year: ⌛')
        runtime = st.text_input('Enter run time: 🕚')
        rating = st.text_input('Enter rating: 💯')
        actors = st.text_input('Enter actors (comma-separated): 🧑‍🎤')
        if st.button('Insert New Movie'):
            success = insert_movie(new_movie, genres, year, runtime, rating, actors)
            if success:
                st.success("Woohoo! New movie added! 🎉")
            else:
                st.error("Oops! Something went wrong. 🤣🫵")


main()
