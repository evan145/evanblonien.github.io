import requests
import json 
import os 
import subprocess

# url = "https://api.themoviedb.org/3/search/movie"
cast_url = "https://api.themoviedb.org/3/movie/379040/credits?api_key=THE_KEY&language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNWU1NmM5NWQ2ZWYxYjM1NDA4ZmZiOTY1ZTUzMjBjZSIsIm5iZiI6MTc2MDMzMDcwNi44Niwic3ViIjoiNjhlYzgzZDJkNTMzOGM5YjIyNzg0ZDM5Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.Qaf1tWCCoDJjIFha_-HEYFt21gU8QaEpK8kWajY20ks"
}

params = {
    "query": "good will hunting",
    "include_adult": "false",
    "language": "en-US",
    "page": 1
}

response = requests.get(cast_url, headers=headers, params=params)
data = response.json()

# movie = data['results'][0]
cast = data['cast']
for n in range(5): 
    print(cast[n]['name'])
    print(cast[n]['profile_path'])
    print("\n")



# ==============================================================================
