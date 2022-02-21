#
#
#

import requests
import csv

# your api key >>> the movie database"
api_key_ = "api_key"

# url requested by the api for popular movies
daily_trend_movies_url = "https://api.themoviedb.org/3/trending/movie/day"

# query string parameters
daily_trend_query_params = {
    "api_key": api_key_
}

response = requests.get(daily_trend_movies_url, daily_trend_query_params)

print(response)  # <Response [200]>
type(response)
data = response.json()
type(data)

print(data)

for key in data:
    print(f"Key : {key}")

print(data["page"])  # page 1

len(data["results"])  # 20 >> movie count

# daily trend movies
for movie in data["results"]:
    print(f"Movie ID: {movie['id']}\n"
          f"Movie Title: {movie['original_title']}\n"
          f"Release Date: {movie['release_date']}\n"
          f"Overview:\n {movie['overview']}\n"
          f"Popularity: {movie['popularity']}\n"
          f"Vote Count: {movie['vote_count']}\n"
          f"Vote Average: {movie['vote_average']}\n")
    print("**************")

movie_ids = []
for movie in data["results"]:
    movie_ids.append(movie["id"])

print(movie_ids)

# details of trend movies
for movie_id in movie_ids:
    movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    details_query_params = {
        "api_key": api_key_,
        "language": "en-US",

    }
    response = requests.get(movie_details_url, details_query_params)
    detail_data = response.json()

    print(f"ID: {detail_data['id']}\n"
          f"Title: {detail_data['title']}\n"
          f"Budget: {detail_data['budget']}\n"
          f"Revenue: {detail_data['revenue']}\n"
          f"Status: {detail_data['status']}\n\n")

################################################################################################################################################
# trend movies process

# first : create csv file and write header
headers = ["movie_id", "movie_title", "overview", "popularity", "vote_count", "vote_average"]
# append data to file
with open("daily_trend_movies.csv", "a", newline="", encoding="utf-8") as file:
    csv_writer = csv.DictWriter(file, headers)
    csv_writer.writeheader()
    for movie in data["results"]:
        csv_writer.writerow({"movie_id": movie['id'],
                             "movie_title": movie['original_title'],
                             "overview": movie['overview'],
                             "popularity": movie['popularity'],
                             "vote_count": movie['vote_count'],
                             "vote_average": movie['vote_average'],
                             })

# check trend movies  -->  worked
with open("daily_trend_movies.csv", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for movies in csv_reader:
        print(f"Movie ID: {movies['movie_id']} ---> Title: {movies['movie_title']}")

################################################################################################################################################
# movie details process

detail_headers = ["movie_id", "title", "budget", "revenue", "status"]
# append data to file
movie_ids = []
for movie in data["results"]:
    movie_ids.append(movie["id"])

details_query_params = {
    "api_key": api_key_,
    "language": "en-US",
}

with open("movie_details.csv", "a", newline="", encoding="utf-8") as file:
    csv_writer = csv.DictWriter(file, detail_headers)
    csv_writer.writeheader()
    for movie_id in movie_ids:
        movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"

        response = requests.get(movie_details_url, details_query_params)
        detail_data = response.json()

        csv_writer.writerow({"movie_id": detail_data['id'],
                             "title": detail_data['original_title'],
                             "budget": detail_data['budget'],
                             "revenue": detail_data['revenue'],
                             "status": detail_data['status']})
