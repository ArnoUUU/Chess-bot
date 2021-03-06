# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

!pip install chess

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import chess
import tensorflow as tf
from tensorflow import keras 

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session



# NEW NOTEBOOK BOX




df = pd.read_csv('../input/chess-evaluations/chessData.csv')
training_set = df.loc[0:999999]
test_set = df.loc[1000000: 1999999]
training_set.head()
#training_set['FEN'].apply(function_name(args))


# NEW NOTEBOOK BOX



def con_pos_to_num(r, c):
    val = r * 8 + c
    return val

# NEW NOTEBOOK BOX



def bitboards_to_array(bb: np.ndarray) -> np.ndarray:
    bb = np.asarray(bb, dtype=np.uint64)[:, np.newaxis]
    s = 8 * np.arange(7, -1, -1, dtype=np.uint64)
    b = (bb >> s).astype(np.uint8)
    b = np.unpackbits(b, bitorder="little")
    return b.reshape(-1, 8, 8)



# NEW NOTEBOOK BOX




def network_input(s):
    bd = chess.Board(s)
    black, white = bd.occupied_co
    bitboards = np.array([
        black & bd.pawns,
        black & bd.knights,
        black & bd.bishops, 
        black & bd.rooks,
        black & bd.queens,
        black & bd.kings,
        white & bd.pawns,
        white & bd.knights,
        white & bd.bishops,
        white & bd.rooks,
        white & bd.queens,
        white & bd.kings
    ], dtype = np.uint64)
    board_array = bitboards_to_array(bitboards)
    arr = np.zeros((64, 64, 10), dtype = np.uint16)
    if (chess.BLACK):
        bd.apply_transform(chess.flip_horizontal)
        print(bd)
        print()
        bd.apply_mirror()
        bitboards = np.array([
        black & bd.pawns,
        black & bd.knights,
        black & bd.bishops, 
        black & bd.rooks,
        black & bd.queens,
        black & bd.kings,
        white & bd.pawns,
        white & bd.knights,
        white & bd.bishops,
        white & bd.rooks,
        white & bd.queens,
        white & bd.kings
    ], dtype = np.uint64)
    print(bitboards_to_array(np.array([black & bd.kings])))
    board_array = bitboards_to_array(bitboards)
#     print(chess.square(G8))
    print(bd)
    return bd, bd

# NEW NOTEBOOK BOX


pieces = np.array([
        black & bd.pawns,
        black & bd.knights,
        black & bd.bishops, 
        black & bd.rooks,
        black & bd.queens,
        white & bd.pawns,
        white & bd.knights,
        white & bd.bishops,
        white & bd.rooks,
        white & bd.queens
    ])
for i in range(10):
    
    white = True
    if i < 5:
        white = False
    
    poi = pieces[i]
    board = bitboards_to_array(np.array([poi]))
    r, c = None, None # find all nonzero elements
    
    index = con_pos_to_num(r, c)
    if white:
        bitboards_to_array(np.array([white & bd.kings]))
        r, c = 0,0#find position of king
        index_king = con_pos_to_num(r, c)
    
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(2))

