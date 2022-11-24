#from torch import BoolStorage
from operator import methodcaller
from boggle import Boggle
from flask import Flask, request, session, redirect , render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "test_secret123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False #Removing the consistent redirect
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/start', methods=["POST"])
def start_game():
    session['board'] =[]
    return redirect('/board')

@app.route('/board')
def generate_board():
    board = boggle_game.make_board()
    session['board'] = board

    print('*******SESSION*******')
    print(session['board'])
    print('*******SESSION*******')
    return render_template("board.html", board = board) 

