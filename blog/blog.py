from fasthtml import common as fh
from monsterui import all as mui

#===========Fast_HTML Stuff========================#

hdrs = mui.Theme.blue.headers()

app,rt = fh.fast_app(hdrs=hdrs, live=False)

navbar = mui.NavBar(
            fh.A('Blog',href='/under_construction'),
            fh.A('Projects',href='/under_construction'),
            fh.A('Photos',href='/under_construction'),
            fh.A('CV',href='/under_construction'),
            fh.A(mui.UkIcon('settings'), href='/under_construction'),
            brand=mui.DivLAligned(
                fh.A(mui.UkIcon('linkedin',height=30,width=30), href='https://linkedin.com/in/evan-blonien-a39047387'),
                fh.A(mui.UkIcon('github', height=25, width=25), href='https://github.com/evan145'),
                fh.P('Evan Homepage')), 
                cls='bg-red-950 px-6 py-4 shadow-lg'
                )

# Homepage
@rt('/')
def get(): 
    return(
    navbar,
        # Similar homepage to the film_app
        mui.Titled('Hello world')
    )

@rt('/Blog')
def get():  # noqa: F811
    return(
    navbar,
        # Filter by keywork (python, front end, fasthtmll, opinion, etc.)
        # Scoll feature to see all of the projects
        # Link to each project 
            # In each link there will be:
                # 1. a link to the github page, 
                # 2. a short paragraph explaining the project
                # 3. (hopefully) a video going through the code of the proejct
    )

@rt('/Photos')
def get():  # noqa: F811
    return(
    navbar, 
        # A grid filled with my photos
        # If the user clicks on the photo there will be a separate page that has just that photo and all of the metadata
    )

# need to define all of the photos as a list
@rt('/Photos/{photo}')
def get(photo_number=int, photo_img=str):  # noqa: F811
    return(
        navbar, 
    )

@rt('/CV')
def get():  # noqa: F811
    return(
        # This is a page that is just an image of my Resume and all of my experiences 
        # Use the fast_html card feature to make it look cooler when you hover over the image
    )

@rt('/Settings')
def get():  # noqa: F811
    return(
        # This is where I flex
        # accessability settings to make it easier to read
        # (hopefully) Light and dark mode
    )


# under construction page
@rt('/under_construction')
def get():  # noqa: F811
    return(
        navbar,
        fh.Div(
            fh.Div(
                mui.UkIcon('construction', height=80,width=80, cls='text-yellow-500 mb-6'),
                fh.H1('Under Construction', cls='text-4xl font-bold mb-4'),
                fh.A('← Back to Home', href=('/'), cls='bg-blue-600 hover:bg-blue-700 text-white py-3 px-6 rounded-lg'),
                cls='text-center' 
            ),
            cls='flex items-center justify-center min-h-[70vh]'
        )
    )

fh.serve()