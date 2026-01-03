#---------------------Trivia API setup--------------------------------------------------
import requests  # type: ignore
score = 0
questions = [] # List of questions
correct_ans = [] # List of answers

# This creates a new list based on user settings 
def get_list(x, category, difficulty):
    if (category==1):
        # The URL for 'all categories' is different so this is how I fixed it 
        url = f"https://opentdb.com/api.php?amount={x}&difficulty={difficulty}&type=boolean"
    else:
        url = f"https://opentdb.com/api.php?amount={x}&category={category}&difficulty={difficulty}&type=boolean"
    response = requests.get(url)
    data = response.json()
    # Clears the previous list [when user restarts]
    questions.clear() 
    correct_ans.clear()
    # This adds questions to list even if requested amount > actual question amount 
    if "results" in data and len(data["results"]) > 0: 
        for question in data["results"]: 
            questions.append(question["question"])
            correct_ans.append(question["correct_answer"])

# This checks to see if user answer matches correct answer
def check(question_index, answer): 
    if answer == correct_ans[question_index]:
        return True # If correct, the function returns True
    return False # If incorrect, the function returns False 

#---------------------All of the fastHTML stuff ----------------------------------------
from fasthtml import common as fh #type: ignore  # noqa: E402

app, rt = fh.fast_app(static_path='public', live=False) # Connects the fast app to the static folder of images
@rt('/') # Home page 
def get():
    global score
    score = 0 # Resets the score to zero every restart 
    return fh.Titled(
        fh.Group(
        "Trivia Game",
        fh.Img(src="question.png", style="max-width: 100px; height: auto;"), 
        style="display: flex; align-items: center; gap: 20px"
        ),
        fh.P("Here is a Trivia game that I made using API calls and FastHTML. Click start to begin"), 
        fh.Form(
            # Connects to the questions page and starts at the first question
            fh.Button("Start", type="submit", style="width: 100%"),  
                action='/settings',
                method='get'))

@rt('/settings') # settings page for the types of questions
def get():  # noqa: F811
    def mk_input(): return fh.Input(name="question_amount", required=True, type="number", min="1", value=10)    
    question_amount = mk_input()
    # These are all the categories (the value cooresponds to API URL)
    category_dd = fh.Select(
        fh.Option("All", value="1", selected=True),
        fh.Option("General Knowledge", value="9"),
        fh.Option("Books", value="10"),
        fh.Option("Film", value="11"),
        fh.Option("Music", value="12"),
        fh.Option("Theatre", value="13"),
        fh.Option("Television", value="14"),
        fh.Option("Video Games ", value="15"),
        fh.Option("Board Games", value="16"),
        fh.Option("Science and Nature", value="17"),
        fh.Option("Science: Computers", value="18"),
        fh.Option("Science: Mathmatics", value="19"),
        fh.Option("Mythology", value="20"),
        fh.Option("Sports", value="21"),
        fh.Option("Geography", value="22"),
        fh.Option("History", value="23"),
        fh.Option("Politics", value="24"),
        fh.Option("Art", value="25"),
        fh.Option("Celebrities", value="26"),
        fh.Option("Animals", value="27"),
        fh.Option("Vehicles", value="28"),
        fh.Option("Comics", value="29"),
        fh.Option("Science: Gadgets", value="30"),
        fh.Option("Japanese Anime", value="31"),
        fh.Option("Cartoons", value="32"),
        name="category_dd"
    )    
    # Difficulty dropdown menu
    difficulty_dd = fh.Select(
        fh.Option("Easy", value="easy", selected=True),
        fh.Option("Medium", value="medium"),
        fh.Option("Hard", value="hard"),
        name="difficulty_dd"
    )
    return fh.Titled(
        fh.P("Settings Menu"),
        fh.Form(
        # Puts drop down + text onto page 
        fh.Header(("Number of Questions:"), question_amount), 
        fh.Header(("Select Category:"), category_dd),
        fh.Header(("Select Difficulty:"), difficulty_dd), 
        fh.Button("Start", action="/createlist"), type="submit", method="post"))

@rt('/settings')
# This posts the settings from the settings screen into the get_list function
def post(question_amount:int, category_dd:str, difficulty_dd:str):  
    get_list(question_amount, int(category_dd), difficulty_dd)
    return fh.Redirect('/questions/0') # noqa: F841

# Each question has a different page, this is the general page
@rt('/questions/{question_num:int}') 
def get(question_num: int):  # noqa: F811
    if question_num >= len(questions): # Repeats questions until list is over 
        return fh.Titled(
            fh.P("DONE"), 
            fh.P(f"Score: {score}"), # Displays how many correct answers
            fh.Form(
                fh.Button("Return Home", type="submit", style="width: 25%", ), 
            action='/', method='get')) 
    inp = fh.Form(
        fh.Group(
            # True button, contains 'id' answer, and value True
            fh.Button("True", name="answer", value="True"), 
            # False button, contains 'id' answer, and value False
            fh.Button("False", name="answer", value="False")),
            # This switches the root to check the answer  
            hx_post=f'/check/{question_num}') 
    return fh.Titled(
        fh.P(f"Question: {question_num + 1}/{len(questions)}"),  # This tells you what question you are on
        fh.P(questions[question_num]), inp) # This creates the question and the True/False buttons

@rt('/check/{question_num:int}')
def Post(question_num: int, answer: str):  # noqa: F811
    global score # gets thes score variable
    is_correct = check(question_num, answer) # Connects to the check function and gives user input
    if is_correct: 
        score = score + 1 # noqa: F823, F841, increases the score by one
        result_msg = fh.Div(
            fh.P("Correct"),
            fh.Form(
                # Connects to the questions page and starts at the first question 
                fh.Button("Next Question", type="submit", style="width: 25%", ), 
            # Changes to the next question and switches root
            action=f'/questions/{question_num +1}', method='get')) 
    else: 
        result_msg = fh.Div(
            fh.P("Incorrect"),
            fh.Form(
                # Connects to the questions page and starts at the first question
                fh.Button("Next Question", type="submit", style="width: 25%", ),  
            # Changes to the next question and switches root
            action=f'/questions/{question_num +1}', method='get')) 
    # Returns the Correct/Incorrect and links the next question
    return result_msg 


fh.serve() # Runs the code
