from fasthtml import common as fh 
import httpx
from monsterui import all as mui

hdrs = mui.Theme.red.headers()
app, rt = fh.fast_app(hdrs=hdrs)

url = "https://api.themoviedb.org/3/search/movie"
movie_selection = ""
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

app, rt = fh.fast_app(exts="ws")

def get_movie_image(query):
    """Fetch movie poster from TMDB API"""
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
    if img_url:
        return fh.Card(
            fh.Img(src=img_url, style="max-width: 50%; height: auto;"),
            fh.H4(f"Movie: {movie_name}")
        )
    return fh.Card(fh.P(f"No image found for: {movie_name}"))

# Input field that gets reset after sending
def mk_input(): 
    return fh.Input(id="msg", placeholder="Enter a movie title", value="", hx_swap_oob="true")

@rt('/')
def index():
    return fh.Div(
        fh.H1("Movie Search"),
        
        # Search form
        fh.Form(mk_input(), ws_send=True),
        
        # Movie display area - starts with a default movie
        fh.Div(
            movie_image_card("Cars 2"),
            id="movie-container"
        ),
        
        # Show movie
        fh.Div(
        fh.H5(f"Overview: {movie["overview"]}"),
        id="overview-container",
        ),

        hx_ext="ws", 
        ws_connect="/ws"
    )

@app.ws("/ws")
async def ws(msg: str, send):
    
    # Fetch new movie data
    params["query"] = msg 
    
    response = httpx.get(url, headers=headers, params=params)
    data = response.json()
    
    if data.get("results"):
        new_movie = data["results"][0]

    # Create a new movie card with the searched movie
        movie_card = movie_image_card(msg)
    
    # Updated overview 
        updated_overview = fh.Div(
            fh.H5(f"Overview: {new_movie["overview"]}"),
            id="overview-container",
            hx_swap_obb="true" # replace existing element
        )
    
    # Send both the new movie card and reset the input
    await send(fh.Div(movie_card, id="movie-container", hx_swap_oob="true"))
    await send(updated_overview)
    await send(mk_input())

fh.serve()