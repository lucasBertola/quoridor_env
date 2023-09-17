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

def test_player_should_not_be_able_to_pass_between_two_wall():
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

    player_who_finish,isFinish  = env.play(MoveWall(1,1,'h',boardSize))
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
 2 |                   |
   +---+---+   +   +   +
 1 |         1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(3,1,'h',boardSize))
    assert player_who_finish == 0, "game should not be finished"
    assert isFinish == False, "game should not be finished"
    
    assert env.render() == \
"""Player 2 : 5 walls left
   +---+---+---+---+---+
 5 |         2         |
   +   +   +   +   +   +
 4 |                   |
   +   +   +   +   +   +
 3 |                   |
   +   +   +   +   +   +
 2 |                   |
   +---+---+---+---+   +
 1 |         1         |
   +---+---+---+---+---+
     1   2   3   4   5
Player 1 : 5 walls left"""

    player_who_finish,isFinish  = env.play(MoveWall(4,1,'v',boardSize))
    assert isFinish == True, "game should be finished"
    assert player_who_finish == env.player_2_number
    
    
if __name__ == "__main__":
    pytest.main()