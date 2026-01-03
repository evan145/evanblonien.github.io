from fasthtml import common as fh 

app, rt = fh.fast_app()

# list[
#     Good Will Hunting - https://image.tmdb.org/t/p/original/bpV8wn48s82au37QyUJ51S7X2Vf.jpg, 
#     cars 2 - https://image.tmdb.org/t/p/original/yMmhALrLWj9amm2pAelmdXggxk2.jpg, 
#     fight club - https://image.tmdb.org/t/p/original/5TiwfWEaPSwD20uwXjCTUqpQX70.jpg    
#     ]

# This is a list of all of the images 
image_path = ['https://image.tmdb.org/t/p/original/bpV8wn48s82au37QyUJ51S7X2Vf.jpg', 
              'https://image.tmdb.org/t/p/original/yMmhALrLWj9amm2pAelmdXggxk2.jpg', 
              'https://image.tmdb.org/t/p/original/5TiwfWEaPSwD20uwXjCTUqpQX70.jpg', 
              'https://image.tmdb.org/t/p/original/9jrHaaXWB37VcA4KGemP8iF7bFB.jpg', 
              'https://image.tmdb.org/t/p/original/2w4xG178RpB4MDAIfTkqAuSJzec.jpg', 
              'https://image.tmdb.org/t/p/original/2Nti3gYAX513wvhp8IiLL6ZDyOm.jpg', 
              'https://image.tmdb.org/t/p/original/sUGwd2X3G5VJcgc2vju7BPTEcI2.jpg']

@rt('/')
def index(): 
    
    # This creates an image card for each of the images in the list
    cards = []
    for img in image_path:
        cards.append(fh.Card(fh.Img(src=img, style="width: a; height: auto; object-fit: cover;")))
    
    # This unpacks the card list and outputs the image cards, also includes formatting for images
    return fh.Div(
        *cards,
        style="display: flex; align-items: center; padding: 20px; gap: 20px;"
    )

fh.serve() 