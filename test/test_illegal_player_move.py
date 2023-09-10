import sys
import pytest

sys.path.append('../')
from quoridor_env import MoveWall
from quoridor_env import QuoridorEnv
from quoridor_env import PlayerMove

def test_move_player_outside_board():
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

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +---+---+
 1 | 1         |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +---+---+
 1 | 1         |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

def test_move_player_outside_board_when_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2     |
   +   +   +   +
 1 | 1         |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 | 1   2     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == env.player_1_number, "game should not be finished"
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 | 1   2     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

def test_move_player_cross_wall_down():
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

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert isFinish == True
    assert player_who_finish == env.player_1_number
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
if __name__ == "__main__":
    pytest.main()
    
    
def test_move_player_cross_wall_up():
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

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +   +---+---+
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
   +   +   +   +
 2 |           |
   +   +---+---+
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |           |
   +   +---+---+
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_move_player_cross_wall_left():
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

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |   |       |
   +   +   +   +
 1 |   | 1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |   |       |
   +   +   +   +
 1 |   | 1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_move_player_cross_wall_right():
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

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |       |   |
   +   +   +   +
 1 |     1 |   |
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
   +   +   +   +
 2 |       |   |
   +   +   +   +
 1 |     1 |   |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |       |   |
   +   +   +   +
 1 |     1 |   |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_move_up_left_without_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
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

def test_move_up_right_without_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('up_right'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
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


def test_move_down_right_without_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down_right'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

def test_move_down_left_without_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down_left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 |     1     |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""


def test_move_down_left_without_wall_behind_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('down_left'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
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

def test_move_down_right_without_wall_behind_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('down_right'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
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

def test_move_down_right_2_without_wall_behind_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('down_left'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
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

def test_move_up_right_2_without_wall_behind_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
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

def test_move_up_left_2_without_wall_behind_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2     |
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
 3 |           |
   +   +   +   +
 2 |     2   1 |
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
 3 |           |
   +   +   +   +
 2 |     2   1 |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2   1 |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

def test_move_down_left_2_without_wall_behind_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2     |
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
 3 |           |
   +   +   +   +
 2 |     2   1 |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,2,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +---+---+   +
 2 |     2   1 |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""


    player_who_finish,isFinish  = env.play(PlayerMove('down_left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +---+---+   +
 2 |     2   1 |
   +   +   +   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""


def test_move_up_right_without_wall_behind_jump():
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

    player_who_finish,isFinish  = env.play(PlayerMove('up_right'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
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

def test_move_up_left_without_wall_behind_jump():
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

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |       |   |
   +   +   +   +
 1 |     1 |   |
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
 2 |     2 |   |
   +   +   +   +
 1 |     1 |   |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2 |   |
   +   +   +   +
 1 |     1 |   |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_move_down_right_with_blocked_wall():
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

    player_who_finish,isFinish  = env.play(PlayerMove('down_right'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
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

def test_move_down_left_with_blocked_wall():
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

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |     1     |
   +   +---+---+
 1 |           |
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
 2 |   | 1     |
   +   +---+---+
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down_left'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |   | 1     |
   +   +---+---+
 1 |   |       |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_move_down_left_2_with_blocked_wall():
    boardSize = 5
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |         1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |     1             |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |         2         |
   +   +   +   +   +   +
 2 |     1             |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |     1   2         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,2,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |     1   2         |
   +---+---+   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,3,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |   |               |
   +   +   +   +   +   +
 3 |   | 1   2         |
   +---+---+   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down_left'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |   |               |
   +   +   +   +   +   +
 3 |   | 1   2         |
   +---+---+   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

def test_move_down_right_2_with_blocked_wall():
    boardSize = 5
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |         1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |             1     |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |         2         |
   +   +   +   +   +   +
 2 |             1     |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |         2   1     |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(4,2,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |         2   1     |
   +   +   +   +---+---+
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""


    player_who_finish,isFinish  = env.play(MoveWall(4,3,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |               |   |
   +   +   +   +   +   +
 3 |         2   1 |   |
   +   +   +   +---+---+
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down_right'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |               |   |
   +   +   +   +   +   +
 3 |         2   1 |   |
   +   +   +   +---+---+
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

def test_move_up_left_with_blocked_wall():
    boardSize = 5
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |         1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |         1         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,4,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +---+---+   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |         1         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,3,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +---+---+   +   +
 4 |       | 2         |
   +   +   +   +   +   +
 3 |       | 1         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +---+---+   +   +
 4 |       | 2         |
   +   +   +   +   +   +
 3 |       | 1         |
   +   +   +   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |   |               |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""


    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +---+---+   +   +
 4 |       | 2         |
   +   +   +   +   +   +
 3 |       | 1         |
   +   +   +   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |   |               |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""


def test_move_up_right_with_blocked_wall():
    boardSize = 5
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |         1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |         1         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,4,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +---+---+   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |         1         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(3,3,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +---+---+   +   +
 4 |         2 |       |
   +   +   +   +   +   +
 3 |         1 |       |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +---+---+   +   +
 4 |         2 |       |
   +   +   +   +   +   +
 3 |         1 |       |
   +   +   +   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |   |               |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""


    player_who_finish,isFinish  = env.play(PlayerMove('up_right'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +---+---+   +   +
 4 |         2 |       |
   +   +   +   +   +   +
 3 |         1 |       |
   +   +   +   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |   |               |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""


def test_move_up_left_2_with_blocked_wall():
    boardSize = 5
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |         1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |     1             |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |         2         |
   +   +   +   +   +   +
 2 |     1             |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |     1   2         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,3,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +---+---+   +   +   +
 3 |     1   2         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,2,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +---+---+   +   +   +
 3 |   | 1   2         |
   +   +   +   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +---+---+   +   +   +
 3 |   | 1   2         |
   +   +   +   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""


def test_move_up_right_2_with_blocked_wall():
    boardSize = 5
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |         1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('right'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |             1     |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |         2         |
   +   +   +   +   +   +
 2 |             1     |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |         2   1     |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(4,3,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +---+---+
 3 |         2   1     |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""


    player_who_finish,isFinish  = env.play(MoveWall(4,2,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +---+---+
 3 |         2   1 |   |
   +   +   +   +   +   +
 2 |               |   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_right'))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +---+---+
 3 |         2   1 |   |
   +   +   +   +   +   +
 2 |               |   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""


def test_move_up_left_2_with_blocked_wall_on_board():
    boardSize = 5
    env = QuoridorEnv(size=boardSize)
    env.reset()
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |         1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |         1         |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |         2         |
   +   +   +   +   +   +
 3 |         1         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |         1         |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |         1         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,4,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |       | 2         |
   +   +   +   +   +   +
 4 |       | 1         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up_left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |       | 2         |
   +   +   +   +   +   +
 4 |       | 1         |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +   +   +   +   +   +
 1 |                   |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 6 walls left"""

def test_move_up_left_2_on_left_up_board():
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
 1 | 1         |
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
 2 | 1         |
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
 3 | 2         |
   +   +   +   +
 2 | 1         |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""


    player_who_finish,isFinish  =  env.play(PlayerMove('up_left'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 | 2         |
   +   +   +   +
 2 | 1         |
   +---+---+   +
 1 |           |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""


def test_jump_outside_board():
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

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
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

def test_jump_with_board_behind():
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


    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2     |
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
 3 |           |
   +   +   +   +
 2 |     2     |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,2,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +---+---+
 2 |     2     |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +---+---+
 2 |     2     |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

def test_jump_with_board_in_front():
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


    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2     |
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
 3 |           |
   +   +   +   +
 2 |     2     |
   +   +   +   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2     |
   +   +---+---+
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 3 walls left
   +---+---+---+
 3 |           |
   +   +   +   +
 2 |     2     |
   +   +---+---+
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 4 walls left"""

if __name__ == "__main__":
    pytest.main()