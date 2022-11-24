from boggle import Boggle
from flask import Flask, request, session, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "test_secret123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False #Removing the consistent redirect
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def index():
    return render_template("home.html")