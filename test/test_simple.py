import sys
import pytest
sys.path.append('../')
from quoridor_env import QuoridorEnv

def test_empty_table():
    env = QuoridorEnv(size=9)
    env.reset()
    print('coucou')
    print(env.render())

if __name__ == "__main__":
    pytest.main()