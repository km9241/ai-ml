import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv(r"C:\pythonforml\tmdb_5000_movies.csv")
movies = movies[['title', 'overview']]
movies['overview'] = movies['overview'].fillna('')
cv = CountVectorizer(stop_words='english')
vectors = cv.fit_transform(movies['overview'])
similarity = cosine_similarity(vectors)
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        print("Movie not found in dataset.")
        return
    idx = movies[movies['title'].str.lower() == movie].index[0]
    distances = list(enumerate(similarity[idx]))
    movies_list = sorted(distances, reverse=True, key=lambda x: x[1])[1:6] 
    print(f"Top 5 choices for '{movies.iloc[idx].title}':")
    for i in movies_list:
        print(movies.iloc[i[0]].title)
recommend("the dark knight")

