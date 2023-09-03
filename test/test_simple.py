import sys
import pytest

sys.path.append('../')
from quoridor_env import MoveWall
from quoridor_env import QuoridorEnv
from quoridor_env import PlayerMove

def test_simple_game():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |   |       |
   +   +   +   +
 1 |   | 1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |         2 |
   +   +   +   +
 2 |   |       |
   +   +   +   +
 1 |   | 1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |         2 |
   +   +   +   +
 2 |   | 1     |
   +   +   +   +
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |   | 1   2 |
   +   +   +   +
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == env.player_1_number, "player1 should win"
    assert isFinish == True, "game  be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     1     |
   +   +   +   +
 2 |   |     2 |
   +   +   +   +
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""
    

def test_jump_down():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     1     |
   +   +   +   +
 1 |     2     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""


def test_jump_up():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |   |       |
   +   +   +   +
 1 |   | 1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |   | 2     |
   +   +   +   +
 1 |   | 1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     1     |
   +   +   +   +
 2 |   | 2     |
   +   +   +   +
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""


def test_jump_left_right():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |         1 |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |         1 |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""


    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |         1 |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 | 2       1 |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""


    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 | 2   1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     1   2 |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,2,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +---+---+   +
 2 |     1   2 |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +---+---+   +
 2 | 2   1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""


def test_jump_up_left():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,2,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +---+---+   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |         2 |
   +---+---+   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |         2 |
   +---+---+   +
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +---+---+   +
 2 |     1   2 |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +---+---+   +
 2 |         2 |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +---+---+   +
 2 |     2     |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +---+---+   +
 2 | 1   2     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_jump_up_right():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,2,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +---+---+
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +---+---+
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +---+---+
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +---+---+
 2 | 2   1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +---+---+
 2 | 2         |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +---+---+
 2 |     2     |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +---+---+
 2 |     2   1 |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_jump_up_right_2():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 | 1         |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |       |   |
   +   +   +   +
 1 | 1     |   |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 | 1     |   |
   +   +   +   +
 1 |       |   |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 | 1   2 |   |
   +   +   +   +
 1 |       |   |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_right'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     1     |
   +   +   +   +
 2 |     2 |   |
   +   +   +   +
 1 |       |   |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

def test_jump_down_right_2():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 | 1         |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |       |   |
   +   +   +   +
 1 | 1     |   |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 | 1     |   |
   +   +   +   +
 1 |       |   |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 | 1   2 |   |
   +   +   +   +
 1 |       |   |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down_right'))
    assert player_who_finish == 0
    assert isFinish == False
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2 |   |
   +   +   +   +
 1 |     1 |   |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

def test_jump_down_right():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |     1     |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,2,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |   | 2     |
   +   +   +   +
 2 |   | 1     |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down_right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |   |       |
   +   +   +   +
 2 |   | 1   2 |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_jump_down_left():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |     1     |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |     1 |   |
   +---+---+   +
 1 |       |   |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down_left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 | 2   1 |   |
   +---+---+   +
 1 |       |   |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_jump_down_left_2():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |         1 |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |   |       |
   +   +   +   +
 1 |   |     1 |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |   |     1 |
   +   +   +   +
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |   | 2   1 |
   +   +   +   +
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down_left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |   | 2     |
   +   +   +   +
 1 |   | 1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""


def test_jump_up_left_2():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |         1 |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |   |       |
   +   +   +   +
 1 |   |     1 |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |   |     1 |
   +   +   +   +
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |   | 2   1 |
   +   +   +   +
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     1     |
   +   +   +   +
 2 |   | 2     |
   +   +   +   +
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""



def test_jump_up_left_on_board():
    boardSize = 3
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |     1     |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert isFinish == True
    assert player_who_finish == env.player_1_number
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 | 1   2     |
   +   +   +   +
 2 |           |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

if __name__ == "__main__":
    pytest.main()