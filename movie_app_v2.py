from fasthtml import common as fh  # type: ignore
import httpx
from monsterui.all import * # type: ignore  # noqa: F403

# This sets up the API call and inputs the 
url = "https://api.themoviedb.org/3/search/movie"
movie_selection = "Cars 2"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNWU1NmM5NWQ2ZWYxYjM1NDA4ZmZiOTY1ZTUzMjBjZSIsIm5iZiI6MTc2MDMzMDcwNi44Niwic3ViIjoiNjhlYzgzZDJkNTMzOGM5YjIyNzg0ZDM5Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.Qaf1tWCCoDJjIFha_-HEYFt21gU8QaEpK8kWajY20ks"
}

params = {
    "query": movie_selection,
    "include_adult": "false",
    "language": "en-US",    
    "page": 1
}

response = httpx.get(url, headers=headers, params=params)
data = response.json()

movie = data["results"][0]
image_path = movie["backdrop_path"]
image_url = f"https://image.tmdb.org/t/p/original{image_path}"

# # ==============================================================================

hdrs = Theme.red.headers()  # type: ignore # noqa: F405
app, rt = fh.fast_app(hdrs=hdrs)

def get_movie_image(query):
    params["query"] = query 
    
    response = httpx.get(url, headers=headers, params=params)
    data = response.json()
    
    if data.get("results"):
        movie = data["results"][0]
        if movie.get("backdrop_path"):
            return f"https://image.tmdb.org/t/p/original{movie["backdrop_path"]}"
    return None

def movie_image_card(movie_name: str):
   # puts the movie poster in
    img_url = get_movie_image(movie_name)
    print(img_url)
    if img_url:
        return fh.Card(
            fh.Img(src=img_url, style="max-width: 50%; height: auto;"),
            fh.H4(f"Movie: {movie_name}")
        )
    return fh.Card(fh.P(f"No image found for: {movie_name}"))

@rt('/')
def index():
    return fh.Div(
        fh.H1("Movie Search"),
        
        # Search form with HTMX attributes
        fh.Form(
            fh.Input(name="query", placeholder="Enter a movie title", required=True),
            fh.Button("Search", type="submit"),
            hx_post="/search",
            hx_target="#results",
            hx_swap="innerHTML"
        ),
        
        # Results container
        fh.Div(
            # Initial movie display
            movie_image_card("Cars 2"),
            fh.Div(
                fh.H5(f"Overview: {movie['overview']}"),
                id="overview-container"
            ),
            id="results"
        )
    )

@rt('/search', methods=['POST'])
def search(query: str):
    # Fetch new movie data
    params["query"] = query 
    
    response = httpx.get(url, headers=headers, params=params)
    data = response.json()
    
    if data.get("results"):
        new_movie = data["results"][0]
        
        # Return the updated content
        return fh.Div(
            movie_image_card(query),
            fh.Div(
                fh.H5(f"Overview: {new_movie['overview']}"),
                id="overview-container"
            )
        )
    else:
        return fh.Div(
            fh.P(f"No results found for: {query}"),
            fh.Div(
                fh.H5("No overview available"),
                id="overview-container"
            )
        )

fh.serve()