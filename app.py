from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def home_page():
    return render_template('words.html')

@app.get('/create_form')
def create_form():
    words = request.args['words'].split(' ')
    story = request.args['story']

    return render_template('questions.html', words=words)
