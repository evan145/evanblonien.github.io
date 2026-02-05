
# This imports the fastHTML package
from fasthtml.common import *  
# This is the monsterUI package for styling
from monsterui.all import *  
# This is for importing the markdown files 
import os, yaml 
# This initializes the app
app,rt = fast_app(live=False, hdrs=Theme.blue.headers(mode='light'))  

# Navbar
navbar = Nav(
    DivLAligned(
        A("evan's homepage", href='/', cls="text-2xl font-bold tracking-wide"),
        cls="gap-3"),
    DivRAligned(
        A("Blog",href="/blog"),
        A('Projects',href='/projects'),
        A('Photos',href='/under_construction'),
        A("Contact Me",href="/contact"),
        A(UkIcon("settings"), href="/theme"),
        cls="gap-6"),
    cls="flex justify-between items-center bg-gradient-to-r from-slate-900 via-blue-950 to-slate-900 px-8 py-5 shadow-2xl border-b border-blue-400/20 text-white"
)

# This parses the content from the md file
#"---" means the beginning of the doc (title)
def parse_meta(content):
    return yaml.safe_load(content.split("---")[1])

# This is for the blog card on intro page
def Blogcard(meta, fname):
    return Card(
        Div(
            # Random image
            A(Img(src=meta["image"], cls="w-full h-48 object-cover hover:scale-105 transition-transform duration-500"), href=blog_post.to(fname=fname)),
            cls="overflow-hidden"
        ),
        Div(
            # Gets the title and the desciption from the md file
            H2(meta["title"], cls="text-xl font-bold text-slate-800 hover:text-blue-600 transition-colors duration-300"),  
            P(meta["description"], cls="text-slate-600 leading-relaxed mt-2"),  
            DivFullySpaced(  
                # Gets author and the date
                P(meta["author"], cls=TextT.muted),  
                P(meta["date"], cls=TextT.muted),
                cls="mt-4"),  
            DivFullySpaced(
                # This unpacks all of the blog elements and displays them on the page
                Div(*[Label(cat, cls="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-xs font-semibold") for cat in meta["categories"]], cls="flex flex-wrap gap-2"),
                A("read more", href=blog_post.to(fname=fname), cls="uk-button bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white px-5 py-2 rounded-lg font-semibold shadow-lg hover:-translate-y-0.5 transition-all duration-300"),
                cls="mt-4 items-end"
            ),
            cls="p-6"
        ),
        cls="bg-white rounded-2xl shadow-lg hover:shadow-2xl border border-slate-100 hover:border-blue-200 transition-all duration-500 hover:-translate-y-2 overflow-hidden"
    )

#========================= FastHTML code =======================================#

@rt('/')
# This is the homepage
def homepage(): 
    return(
        navbar,
        Div(
            H1("Evan's Homepage", cls="text-4xl md:text-5xl lg:text-6xl font-bold text-slate-800 tracking-tight"),
            P("Here is a collection of my Blogs, Projects, and Photos", cls="text-lg md:text-xl text-slate-500 mt-4"),
            Div(cls="w-24 h-1 bg-gradient-to-r from-blue-500 to-blue-700 mx-auto mt-6 rounded-full"),
            Div(
                A("Read my blog", href="/blog", cls="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white px-6 py-3 rounded-lg font-semibold shadow-lg hover:-translate-y-0.5 transition-all duration-300"),
                A("Contact me", href="/contact", cls="border border-slate-300 text-slate-700 hover:border-blue-500 hover:text-blue-600 px-6 py-3 rounded-lg font-semibold transition-all duration-300"),
                cls="flex gap-4 mt-8"
                ),
                cls="text-center py-24 md:py-32 bg-gradient-to-b from-slate-100 to-white flex flex-col items-center"))


@rt('/blog')
# This is the blog page
def index(): 
    # This gets all of the md files in post folder
    posts = os.listdir("posts")
    # Opens each md file and parses its content 
    post_contents = [open(f"posts/{post}").read() for post in posts]  
    post_meta = [parse_meta(content) for content in post_contents]
    return(
        navbar,
        Div(
            H1("evan's Blog", cls="text-4xl md:text-5xl lg:text-6xl font-bold text-slate-800 tracking-tight"),
            Div(cls="w-24 h-1 bg-gradient-to-r from-blue-500 to-blue-700 mx-auto mt-6 rounded-full"),
            cls="text-center py-16 md:py-24 bg-gradient-to-b from-slate-100 to-white"
        ),
        # Unpacks the different blog posts and adds them to grid format 
        Div(*[Blogcard(m,f) for m,f in zip(post_meta, posts)], 
            cls="grid grid-cols-1 md:grid-cols-2 gap-8 px-8 pb-16 max-w-7xl mx-auto")
    )

@rt('/blog/{fname}')
def blog_post(fname:str):
    file_content = open(f"posts/{fname}").read()
    meta = parse_meta(file_content)
    content = file_content.split("---")[2]
    return(
        navbar,
        Div(
            H1(meta["title"], cls="text-4xl md:text-5xl font-bold text-slate-800 tracking-tight"),
            Div(
                P(meta["author"], cls="font-medium"),
                P("•", cls="text-slate-300"),
                P(meta["date"]),
                cls="flex gap-3 text-slate-500 mt-4",
            ),
            Div(*[Span(x, cls="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-xs font-semibold") for x in meta["categories"]], cls="flex flex-wrap gap-2 mt-4"),
            A('← Back', href='/blog', cls='text-blue-600 hover:text-blue-800 font-medium mt-4 transition-colors'),
            cls="text-center py-16 bg-gradient-to-b from-slate-100 to-white flex flex-col items-center"
        ),
        Div(
            render_md(content),
            cls="max-w-[95%] lg:max-w-[85%] mx-auto px-8 md:px-16 py-12 bg-white rounded-2xl shadow-lg my-8 border border-slate-100 prose prose-lg prose-slate prose-headings:text-slate-800 prose-headings:font-bold prose-p:text-slate-600 prose-p:leading-relaxed prose-a:text-blue-600 prose-strong:text-slate-800 prose-code:bg-slate-100 prose-code:px-2 prose-code:py-1 prose-code:rounded prose-code:text-slate-800 prose-pre:bg-slate-900 prose-pre:text-slate-100 prose-li:text-slate-600"
        ))


@rt('/projects')
# This is the blog page
def index(): 
    # This gets all of the md files in post folder
    projects = os.listdir("projects")
    # Opens each md file and parses its content 
    post_contents = [open(f"projects/{project}").read() for project in projects]  
    post_meta = [parse_meta(content) for content in post_contents]
    return(
        navbar,
        Div(
            H1("evan's projects", cls="text-4xl md:text-5xl lg:text-6xl font-bold text-slate-800 tracking-tight"),
            Div(cls="w-24 h-1 bg-gradient-to-r from-blue-500 to-blue-700 mx-auto mt-6 rounded-full"),
            cls="text-center py-16 md:py-24 bg-gradient-to-b from-slate-100 to-white"
        ),
        # Unpacks the different blog posts and adds them to grid format 
        Div(*[Blogcard(m,f) for m,f in zip(post_meta, projects)], 
            cls="grid grid-cols-1 md:grid-cols-2 gap-8 px-8 pb-16 max-w-7xl mx-auto")
    )

@rt('/projects/{fname}')
def project_post(fname:str):
    file_content = open(f"projects/{fname}").read()
    meta = parse_meta(file_content)
    content = file_content.split("---")[2]
    return(
        navbar,
        Div(
            H1(meta["title"], cls="text-4xl md:text-5xl font-bold text-slate-800 tracking-tight"),
            Div(
                P(meta["author"], cls="font-medium"),
                P("•", cls="text-slate-300"),
                P(meta["date"]),
                cls="flex gap-3 text-slate-500 mt-4",
            ),
            Div(*[Span(x, cls="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-xs font-semibold") for x in meta["categories"]], cls="flex flex-wrap gap-2 mt-4"),
            A('← Back', href='/projects', cls='text-blue-600 hover:text-blue-800 font-medium mt-4 transition-colors'),
            cls="text-center py-16 bg-gradient-to-b from-slate-100 to-white flex flex-col items-center"
        ),
        Div(
            render_md(content),
            cls="max-w-[95%] lg:max-w-[85%] mx-auto px-8 md:px-16 py-12 bg-white rounded-2xl shadow-lg my-8 border border-slate-100 prose prose-lg prose-slate prose-headings:text-slate-800 prose-headings:font-bold prose-p:text-slate-600 prose-p:leading-relaxed prose-a:text-blue-600 prose-strong:text-slate-800 prose-code:bg-slate-100 prose-code:px-2 prose-code:py-1 prose-code:rounded prose-code:text-slate-800 prose-pre:bg-slate-900 prose-pre:text-slate-100 prose-li:text-slate-600"
        ))

# This is the contact page 
@rt('/contact')
def contact(): 
    return(
        navbar,
        Div(
            H1("Contact Me", cls="text-4xl md:text-5xl font-bold text-slate-800 text-center tracking-tight"),
            Div(cls="w-24 h-1 bg-gradient-to-r from-blue-500 to-blue-700 mx-auto mt-6 rounded-full"),
            cls="text-center py-16 bg-gradient-to-b from-slate-100 to-white"
        ),
        Div(
            Form(
                LabelInput("Name", cls="mb-5"),
                LabelInput("Email", cls="mb-5"),
                LabelInput("Message", cls="mb-6"),
                Button("Submit", cls="w-full bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white py-3 rounded-xl font-semibold shadow-lg hover:-translate-y-0.5 transition-all duration-300"),
                cls="bg-white rounded-2xl shadow-xl p-8 border border-slate-100"
            ),
            Div(
                A(UkIcon("linkedin",height=30,width=30), href="https://linkedin.com/in/evan-blonien-a39047387", cls="text-slate-600 hover:text-blue-600 transition-colors"),
                A(UkIcon("github", height=25, width=25), href="https://github.com/evan145", cls="text-slate-600 hover:text-blue-600 transition-colors"),
                cls="flex justify-center gap-6 mt-8"
            ), 
            cls="max-w-md mx-auto px-4 pb-16"
        )
    )

# Settings page
@rt('/theme')
def theme(): 
    # This is the mui theme and the light/dark mode is turned off
    return navbar, ThemePicker(mode=False)

# Standard under construction page
@rt('/under_construction')
def get():  # noqa: F811
    return(
        navbar,
        Div(
            Div(
                UkIcon('construction', height=80,width=80, cls='text-yellow-500 mb-6'),
                H1('Under Construction', cls='text-4xl font-bold mb-4'),
                A('← Back to Home', href=('/'), cls='bg-blue-600 hover:bg-blue-700 text-white py-3 px-6 rounded-lg'),
                cls='text-center' 
            ),
            cls='flex items-center justify-center min-h-[70vh]'
        )
    )

serve()  