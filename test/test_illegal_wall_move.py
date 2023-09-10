import sys
import pytest

sys.path.append('../')
from quoridor_env import MoveWall
from quoridor_env import QuoridorEnv
from quoridor_env import PlayerMove

def test_put_wall_outside_x():
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

    anErrorHappened = False
    try:
        env.play(MoveWall(3,1,'h',boardSize))
    except AssertionError:
        anErrorHappened = True
      
    assert anErrorHappened == True
        
def test_put_wall_outside_x_2():
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

def test_put_wall_outside_x_3():
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

    anErrorHappened = False
    try:
        env.play(MoveWall(3,1,'v',boardSize))
    except AssertionError:
        anErrorHappened = True
      
    assert anErrorHappened == True
    
def test_put_wall_outside_y_2():
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

    anErrorHappened = False
    try:
        env.play(MoveWall(1,0,'h',boardSize))
    except AssertionError:
        anErrorHappened = True
      
    assert anErrorHappened == True
    
def test_put_wall_outside_y():
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

    anErrorHappened = False
    try:
        env.play(MoveWall(1,3,'v',boardSize))
    except AssertionError:
        anErrorHappened = True
      
    assert anErrorHappened == True
    
    
def test_put_wall_bad_orientation():
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

    anErrorHappened = False
    try:
        env.play(MoveWall(1,2,'t',boardSize))
    except AssertionError:
        anErrorHappened = True
      
    assert anErrorHappened == True
 
 
def test_put_wall_with_no_wall_left():
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

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'v',boardSize))
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
 2 |   |               |
   +   +   +   +   +   +
 1 |   |     1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |     2             |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |   |     1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,3,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |     2             |
   +   +   +   +   +   +
 4 |   |               |
   +   +   +   +   +   +
 3 |   |               |
   +   +   +   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |   |     1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('left'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 | 2                 |
   +   +   +   +   +   +
 4 |   |               |
   +   +   +   +   +   +
 3 |   |               |
   +   +   +   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |   |     1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 4 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(1,2,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 | 2                 |
   +   +   +   +   +   +
 4 |   |               |
   +   +   +   +   +   +
 3 |   |               |
   +---+---+   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |   |     1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 | 2 |               |
   +   +   +   +   +   +
 3 |   |               |
   +---+---+   +   +   +
 2 |   |               |
   +   +   +   +   +   +
 1 |   |     1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 | 2 |               |
   +   +   +   +   +   +
 3 |   |               |
   +---+---+   +   +   +
 2 |   |   |           |
   +   +   +   +   +   +
 1 |   |   | 1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 2 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('down'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |   |               |
   +   +   +   +   +   +
 3 | 2 |               |
   +---+---+   +   +   +
 2 |   |   |           |
   +   +   +   +   +   +
 1 |   |   | 1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 2 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,3,'v',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 |   |   |           |
   +   +   +   +   +   +
 3 | 2 |   |           |
   +---+---+   +   +   +
 2 |   |   |           |
   +   +   +   +   +   +
 1 |   |   | 1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 1 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 | 2 |   |           |
   +   +   +   +   +   +
 3 |   |   |           |
   +---+---+   +   +   +
 2 |   |   |           |
   +   +   +   +   +   +
 1 |   |   | 1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 1 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(3,2,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 |                   |
   +   +   +   +   +   +
 4 | 2 |   |           |
   +   +   +   +   +   +
 3 |   |   |           |
   +---+---+---+---+   +
 2 |   |   |           |
   +   +   +   +   +   +
 1 |   |   | 1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 0 walls left"""

    player_who_finish,isFinish  = env.play(PlayerMove('up'))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 | 2                 |
   +   +   +   +   +   +
 4 |   |   |           |
   +   +   +   +   +   +
 3 |   |   |           |
   +---+---+---+---+   +
 2 |   |   |           |
   +   +   +   +   +   +
 1 |   |   | 1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 0 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(3,4,'v',boardSize))
    assert player_who_finish == env.player_2_number
    assert isFinish == True
    
    assert env.render() == \
"""Player 2 : 6 walls left
   +---+---+---+---+---+
 5 | 2                 |
   +   +   +   +   +   +
 4 |   |   |           |
   +   +   +   +   +   +
 3 |   |   |           |
   +---+---+---+---+   +
 2 |   |   |           |
   +   +   +   +   +   +
 1 |   |   | 1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 0 walls left"""

def test_put_wall_on_the_exact_place_of_an_other_wall():
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

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'v',boardSize))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
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

def test_put_wall_on_the_exact_place_of_an_other_wall_2():
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

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'v',boardSize))
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


def test_put_wall_on_the_half_exact_place_of_an_other_wall():
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

    player_who_finish,isFinish  = env.play(MoveWall(1,2,'v',boardSize))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
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

def test_put_wall_on_another_one():
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

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'h',boardSize))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
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

if __name__ == "__main__":
    pytest.main()