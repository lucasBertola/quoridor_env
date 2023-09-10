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
        

if __name__ == "__main__":
    pytest.main()