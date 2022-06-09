from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story, silly_story

user_story = None
user_words = None


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def home_page():
    """ displies word.html"""

    return render_template('questions.html', words=silly_story.prompts)


# @app.get('/create_form')
# def create_form():
 #   """ updates global varilbles< displaies guestions.html
  #      w/ user_words passed into the form """
  #  user_words = request.args['words'].split(' ')
  #  user_story = request.args['story']

   # return render_template('questions.html', words=user_words)


@app.get('/results')
def creat_story():
    """ creates  a dictionary for passing user input and then genrates sory and
        display it on story.html"""

    # user_input = {}

    # for word in silly_story.prompts:
    #     user_input[word] = request.args[word]

    finshed_story = silly_story.generate(request.args)
    print(request.args)
    return render_template('story.html', finshed_story=finshed_story)
