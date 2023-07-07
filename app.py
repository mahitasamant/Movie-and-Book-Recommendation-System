
import streamlit as st
import pickle
import requests
import streamlit.components.v1 as components

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        return None


movies = pickle.load(open("moviess.pkl", 'rb'))
similarity_movie = pickle.load(open("latent_similarity.pkl", 'rb'))
movies_list = movies['title'].values


def recommend_Movie(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity_movie[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:11]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster


def show_movie_page():
    st.header("Movie Recommendation System")

    search_value = st.text_input("Search for a movie:")
    filtered_movies = [movie for movie in movies_list if search_value.lower() in movie.lower()]

    if filtered_movies:
        select_value = st.selectbox("Select a movie from the search results", filtered_movies)
        if st.button("Show Movie Recommendations"):
            movie_name, movie_poster = recommend_Movie(select_value)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(movie_name[0])
                st.image(movie_poster[0])
            with col2:
                st.text(movie_name[1])
                st.image(movie_poster[1])
            with col3:
                st.text(movie_name[2])
                st.image(movie_poster[2])
            with col4:
                st.text(movie_name[3])
                st.image(movie_poster[3])
            with col5:
                st.text(movie_name[4])
                st.image(movie_poster[4])
    else:
        st.write("No movies found matching the search criteria.")
def fetch_cover(book_id):
    full_path="https://covers.openlibrary.org/b/isbn/"+str(book_id)+"-M.jpg"
    return full_path
   


books = pickle.load(open("books.pkl", 'rb'))
similarity_book = pickle.load(open("book_latent_similarity.pkl", 'rb'))
books_list = books['title'].values

def recommend_book(book):
    index = books[books['title'] == books].index[0]
    distance = sorted(list(enumerate(similarity_book[index])), reverse=True, key=lambda vector: vector[1])
    recommend_book = []
    recommend_cover = []
    for i in distance[1:11]:
        book_id = books.iloc[i[0]].isbn13
        recommend_book.append(books.iloc[i[0]].title)
        recommend_cover.append(fetch_cover(book_id))
    return recommend_book, recommend_cover


def show_book_page():
    st.header("Book Recommendation System")

    search_value = st.text_input("Search for a Book:")
    filtered_books = [book for book in books_list if search_value.lower() in book.lower()]

    if filtered_books:
        select_value = st.selectbox("Select a book from the search results", filtered_books)
        if st.button("Show Book Recommendations"):
            book_name, book_poster = recommend_book(select_value)
            col1, col2, col3, col4, col5 = st.columns(5)
           
            with col1:
                st.text(book_name[0])
                st.image(book_poster[0])
            with col2:
                st.text(book_name[1])
                st.image(book_poster[1])
            with col3:
                st.text(book_name[2])
                st.image(book_poster[2])
            with col4:
                st.text(book_name[3])
                st.image(book_poster[3])
            with col5:
                st.text(book_name[4])
                st.image(book_poster[4])
            
    else:
        st.write("No books found matching the search criteria.")

    
    
def show_home_page():
    import streamlit as st

    st.header("Welcome to the Recommendation System")
   
    with st.container():
        import streamlit as st

        tab1, tab2 = st.tabs(["Movies", "Books"])

        with tab1:
            show_movie_page()
            

        with tab2:
            show_book_page() 
            


show_home_page()
