import sys
import pytest

sys.path.append('../')
from quoridor_env import MoveWall
from quoridor_env import QuoridorEnv
from quoridor_env import PlayerMove

def test_close_player1():
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

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +---+---+   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,1,'v',boardSize))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +---+---+   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

def test_close_player2():
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

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +---+---+   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(2,2,'v',boardSize))
    assert player_who_finish == env.player_1_number
    assert isFinish == True
    assert env.render() == \
"""Player 2 : 4 walls left
   +---+---+---+
 3 |     2     |
   +   +   +   +
 2 |           |
   +---+---+   +
 1 |     1     |
   +---+---+---+
     1   2   3
Player 1 : 3 walls left"""

if __name__ == "__main__":
    pytest.main()