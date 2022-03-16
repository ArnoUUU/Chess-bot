'''
This module is responsible foe storing all of the Gamedata. This will  be responsible for generating all legal moves. This will also keep a move log. Which (optional) may be eportabel as PGN
'''
class Gamedata():
  def _init_(self):
    self.chessboard=[
      ["BR","BN","BB","BQ","BK","BB","BN","BR"],
      ["BP","BP","BP","BP","BP","BP","BP","BP"],
      ["--","--","--","--","--","--","--","--"],
      ["--","--","--","--","--","--","--","--"],
      ["--","--","--","--","--","--","--","--"],
      ["--","--","--","--","--","--","--","--"],
      ["WP","WP","WP","WP","WP","WP","WP","WP"],
      ["WR","WN","WB","WQ","WK","WB","WN","WR"]]
    self.white_to_move=True
    self.move_log=[]