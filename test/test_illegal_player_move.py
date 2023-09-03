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

if __name__ == "__main__":
    pytest.main()