import numpy as np
import math
import pygame as pg
import engine
from keras import * 
import tensorflow
#won't work on repl, as the version of python is outdated
from pip import *
from pip import chess
'''
this module is resposible for the User Input and displaying the Gamedata
'''
#importing necesary modules
#Defining Variables
Width=Height=400
Dimension=8
Square_size=Height//Dimension
Max_Fps=10
Images={}
# initializing pygame
p.init()

'''
Initialize a dictionary of the images. THis will be stored in your RAM, and will be optimized to minimize the operations necessary
'''
def Load_Images():
  pieces=['BR','BN','BB','BQ','BK','BP','WR','WN','WB','WQ','WK','WP']
  for piece in pieces:
    Images[piece] = p.transform.scale(p.image.load("images/"+piece+".png")), (Square_size, Square_size)
#Now we can access images with "Images['BB']" for example
# https://python-chess.readthedocs.io/en/latest/pgn.html#writing

# https://levelup.gitconnected.com/chess-python-ca4532c7f5a4

def eval():
  




