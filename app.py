#from torch import BoolStorage
from crypt import methods
from inspect import BoundArguments
from operator import methodcaller

from pkg_resources import working_set
from boggle import Boggle
from flask import Flask, request, session, redirect , render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

'''
Author: Mahad Osman
Date: Nov 26
Assignment: Flask Boggle
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = "test_secret123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False #Removing the consistent redirect
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def index():
    """ Route to return our home page"""
    return render_template("home.html")

@app.route('/start', methods=["POST"])
def start_game():
    """Start route to setup our game and refresh our session vars. Redirects to our game."""
    session['board'] =[]
    session['score'] = 0
    session['highscore'] = 0
    session['numofplays'] = 0
    return redirect('/board')

@app.route('/board')
def generate_board():
    """Our board view will set our game up"""
    board = boggle_game.make_board()
    session['board'] = board
    session['score'] = 0
    highscore = session.get("highscore", 0)
    numofplays = session.get("numofplays", 0)

    # print('*******SESSION*******')
    # print(session['board'])
    # print('*******SESSION*******')
    return render_template("board.html", board = board, highscore = highscore, numofplays = numofplays) 

@app.route("/word_check")
def word_validity():
    """Wordcheck handles the logic if a word exists on the board and passes back the result & score"""
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

    # print('**************')
    # print(session['score'])
    # print('**************')
    return jsonify({"response": res, "score": session['score']})

@app.route("/final_score")#, methods=["POST"])
def final_score():
    """Final Score shall handle determining how many times a game has been played, and the all time highscore."""
    #score = request.json["score"]
    score = session.get("score", 0)
    highscore = session.get("highscore", 0)
    numofplays = session.get("numofplays", 0)

    session['numofplays'] = numofplays + 1
    session['highscore'] = max(score, highscore)
    return jsonify({"score": score, "highscore": highscore, "numofplays" : numofplays}) 
