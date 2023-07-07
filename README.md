# Movie-and-Book-Recommendation-System
This is a  movie and book recommendation system built using Non-Negative Matrix Factorization (NMF) and Streamlit. It provides movie and book recommendations based on the similarity between plots and genres.
# DEMO VIDEO
https://youtu.be/3YYuvRX4Zz4
# Overview
The recommendation system is designed to help users discover new movies that are similar to the ones they already like. By analyzing the plot descriptions and genres the system identifies patterns and similarities, allowing it to generate relevant recommendations. The NMF algorithm is employed to extract latent factors from the dataset, which capture the underlying features and characteristics of the movies. These latent factors are then used to calculate the similarity between movies and books, enabling the system to recommend similar movies/books based on a user's input.

# How it Works
The system utilizes a dataset of movies and books containing information such as titles, plot descriptions, and genres.

The data is preprocessed by combining the plot descriptions and genres into a single feature column, ensuring all relevant information is captured.

The TF-IDF (Term Frequency-Inverse Document Frequency) vectorization technique is applied to the combined features. This step converts the textual data into numerical vectors, which can be used to measure the similarity between movies.

The NMF algorithm is employed to decompose the TF-IDF matrix into latent factors. These latent factors represent underlying features and patterns in the movie dataset.

Cosine similarity is calculated between the latent factors of each pair of movies /Books, generating a similarity matrix. The cosine similarity metric measures the similarity of vectors based on the angle between them, providing a measure of similarity between movies.

The Streamlit web application allows users to enter the title of a movie they enjoy. The system then retrieves the top similar movies based on the calculated similarity scores.

The recommended movies are displayed to the user, providing them with a personalized list of movies they may find interesting.
# Prerequisites
Python 3.7 or higher
Streamlit library
pandas library

