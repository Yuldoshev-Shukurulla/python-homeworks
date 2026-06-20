# # ## Task 1: Weather API
# #    1. Use this url : https://openweathermap.org/
# #    2. Use the `requests` library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
# import requests

# key = '1' 

# city = input('Enter the city name that you want to see weather: ').strip()
# geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={key}"

# response = requests.get(geo_url)

# if response.status_code == 200:
#     data = response.json()
    
#     if data:
#         lat = data[0]['lat']
#         lon = data[0]['lon']
        
#         base_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric'
        
#         weather_response = requests.get(base_url)
        
#         if weather_response.status_code == 200:
#             weather_data = weather_response.json()
            
#             print(f"\n=== Current weather in {city.title()} ===")
#             print(f"Temperature: {weather_data['main']['temp']} °C")
#             print(f"Humidity: {weather_data['main']['humidity']}%")
#             print(f"Description: {weather_data['weather'][0]['description']}")
#         else:
#             print("Error: Could not fetch weather data.")
            
#     else:
#         print('Error: City not found.')
# else:
#     print(f"Error: API request failed with status code {response.status_code}")




# # ## Task 2: Movie Recommendation System
# #    1. Use this url https://developer.themoviedb.org/docs/getting-started/ to fetch information about movies.
# #    2. Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random

api = 'f57a1d46e21771a91cdaa63e818f071c'
baseurl = "https://api.themoviedb.org/3"

def get_movie():
    moviee = requests.get(f'{baseurl}/genre/movie/list?api_key={api}&language=en')
    if moviee.status_code != 200:
        print("Error with api.")
        return
    
    genres = moviee.json()['genres']
    print('===List of available genres===')
    for g in genres:
        print(g['name'])
    genreselected = input('Choose genre: ').strip().lower()
    genre_id = None
    for g in genres:
        if genreselected == g['name'].lower():
            genre_id = g['id']
            break
    if genre_id == None:
        print('Invalid genre selected.')
        return
    print(genre_id)
    movieurl = f'{baseurl}/discover/movie?api_key={api}&with_genres={genre_id}&language=en&page=1'
    movielist = requests.get(movieurl).json()['results']

    if movielist:
        rand = random.choice(movielist)
        print('Recommended movie for you:')
        print(f'Movie name: {rand['title']}')
        print(f'Release date: {rand['release_date']}')
        print(f'Rating: {rand['vote_average']}')
    else:
        print('No movie found with this genre.')

get_movie()









# import requests
# import random

# # 1. API Sozlamalari
# API_KEY = "f57a1d46e21771a91cdaa63e818f071c"
# BASE_URL = "https://api.themoviedb.org/3"

# def get_movie_recommendation():
#     genre_url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    
#     response = requests.get(genre_url)
#     if response.status_code != 200:
#         print("API bilan bog'lanishda xatolik yuz berdi!")
#         return

#     genres_data = response.json()['genres']
    
#     print("=== Available Genres ===")
#     for g in genres_data:
#         print(f"- {g['name']}")
        
#     user_genre = input("\nEnter a genre from the list above: ").strip().lower()
    
#     genre_id = None
#     for g in genres_data:
#         if g['name'].lower() == user_genre:
#             genre_id = g['id']
#             break
            
#     if genre_id is None:
#         print("Invalid genre selected!")
#         return
        
#     discover_url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US&page=1"
    
#     movie_response = requests.get(discover_url)
#     print(movie_response.json())
#     movies_list = movie_response.json()['results']
    
#     if movies_list:
#         random_movie = random.choice(movies_list)
        
#         print(f"\n🎯 Recommended Movie for you:")
#         print(f"🎬 Title: {random_movie['title']}")
#         print(f"⭐️ Rating: {random_movie['vote_average']}")
#         print(f"📅 Release Date: {random_movie['release_date']}")
#         print(f"📝 Overview: {random_movie['overview']}")
#     else:
#         print("No movies found for this genre.")

# if __name__ == "__main__":
#     get_movie_recommendation()