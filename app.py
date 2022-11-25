#from torch import BoolStorage
from crypt import methods
from inspect import BoundArguments
from operator import methodcaller

from pkg_resources import working_set
from boggle import Boggle
from flask import Flask, request, session, redirect , render_template, jsonify
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
    session['score'] = 0
    return redirect('/board')

@app.route('/board')
def generate_board():
    board = boggle_game.make_board()
    session['board'] = board
    session['score'] = 0

    print('*******SESSION*******')
    print(session['board'])
    print('*******SESSION*******')
    return render_template("board.html", board = board) 

@app.route("/word_check")
def word_validity():
    guess = request.args["guess"]
    board = session['board']
    # print('**************')
    # print(guess)
    # print('**************')
    #Pass in a board and word
    res = boggle_game.check_valid_word(board, guess)
    if res == "ok":
        word_value = len(guess)
        session['score'] += word_value
        #word_value = session['score']

    print('**************')
    print(session['score'])
    print('**************')
    return jsonify({"response": res, "score": session['score']})

#@app.route("/score_check", methods=)
