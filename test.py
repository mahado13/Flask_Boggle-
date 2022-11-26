from hashlib import new
from unittest import TestCase
from urllib import response
from app import app
from flask import session
from boggle import Boggle


'''
Author: Mahad Osman
Date: Nov 26
Assignment: Flask Boggle
'''

# class FlaskTests(TestCase):

#     # TODO -- write tests for every view function / feature!
class BoggleTests(TestCase):
    '''Test cases for boogle appx'''
    def setUp(self):
        '''A quick setup to save us the need to keep setting our client'''
        self.client = app.test_client()
    
    def test_home_screen(self):
        '''Testing the inital root path'''
        with self.client:
            res = self.client.get('/')
            html = res.get_data(as_text = True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<button>Start Game</button>', html)
    
    def test_start_redirect(self):
        '''Testing our games setup and redirect to our board'''
        with self.client:
            res = self.client.post('/start')
            # print('*****************')
            # print(session['board'])
            # print('*****************')

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, "/board")

            self.assertEqual(session.get('board'), [])
            self.assertEqual(session.get('highscore'), 0)
            self.assertEqual(session.get('numofplays'), 0)
    
    def test_word_check(self):
        '''With a set board we will be testing if:
            - if the guess is correct
            - if the correct score is returned
            - if the guess is a word but not on the board
        '''
        with self.client as client:
            with client.session_transaction() as newsession:
                newsession['board'] =[["M","W","V","P","H"],
                                  ["G","B","T","A","W"],
                                  ["J","R","M","S","P"],
                                  ["L","Z","O","Y","Y"],
                                  ["A","L","H","A","T"],]
                newsession['score'] =0

            res = self.client.get(f'/word_check?guess=hat')
            self.assertEqual(res.json['response'], 'ok')
            self.assertEqual(res.json['score'], 3)

            res2 = self.client.get(f'/word_check?guess=joke')
            self.assertEqual(res2.json['response'], 'not-on-board')


    def test_not_a_word(self):
        '''Testing if an invalid guess was passed in'''
        self.client.get('/board')
        res = self.client.get('/word_check?guess=hjfdskjbk')
        self.assertEqual(res.json['response'], 'not-word')


