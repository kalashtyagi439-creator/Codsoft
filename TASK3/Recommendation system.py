movies = [
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 9.0},
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7},
    {"title": "Avengers", "genre": "Action", "rating": 8.5},
    {"title": "John Wick", "genre": "Action", "rating": 8.3},
    {"title": "3 Idiots", "genre": "Comedy", "rating": 8.4},
    {"title": "Hera Pheri", "genre": "Comedy", "rating": 8.2},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8},
    {"title": "The Pursuit of Happyness", "genre": "Drama", "rating": 8.5}
]

print("===== MOVIE RECOMMENDATION SYSTEM =====")

genres = sorted(set(movie["genre"] for movie in movies))

print("\nAvailable Genres:")
for g in genres:
    print("-", g)

user_genre = input("\nEnter preferred genre: ")
min_rating = float(input("Enter minimum rating (0-10): "))

recommendations = []

for movie in movies:
    if (movie["genre"].lower() == user_genre.lower()
            and movie["rating"] >= min_rating):
        recommendations.append(movie)

recommendations.sort(
    key=lambda x: x["rating"],
    reverse=True
)

if recommendations:
    print("\nRecommended Movies:\n")

    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie['title']} "
              f"(Genre: {movie['genre']}, "
              f"Rating: {movie['rating']})")
else:
    print("\nNo recommendations found.")
