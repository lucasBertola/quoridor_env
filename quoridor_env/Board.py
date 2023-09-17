import numpy as np

from .Move import MoveWall
from .Move import PlayerMove

class PlayerPosition():
    def __init__(self, col, row):
        self.col = col
        self.row = row
        
        self.board_col = (col-1)*2
        self.board_row = (row-1)*2
        
        self.board_position = (self.board_col,self.board_row)
        
    def move(self, move:PlayerMove):
        return PlayerPosition(self.col+move.col_change, self.row+move.row_change)

class WallPosition():
    def __init__(self, move:MoveWall):
        self.move  = move
        if(move.move_type=='v'):
            x1 = (move.col-1)*2 +1
            y1 = (move.row-1)*2
            x2=x1
            y2=y1+1
            x3=x1
            y3=y1+2
            self.boardPosition = ((x1,y1),(x2,y2),(x3,y3))
        else:
            x1 = (move.col-1)*2
            y1 = (move.row-1)*2 +1
            x2=x1+1
            y2=y1
            x3=x1+2
            y3=y1
            self.boardPosition = ((x1,y1),(x2,y2),(x3,y3))
        
        
class Board():
    def __init__(self, size=3,wall_number = -1):
        self.size = size
        self.wall_number = wall_number
        self.maxBoardSize = self._maxBoardSize()
        self.board = np.zeros((self.maxBoardSize,self.maxBoardSize), dtype=np.int8)

    def _maxBoardSize(self):
        return (self.size*2)-1
        
    def set_player_position(self,player:PlayerPosition, player_number):
        self.board[player.board_col][player.board_row] = player_number
        
    def position_is_player(self, position:PlayerPosition):
        return self.board[position.board_col][position.board_row] != 0
    
    def player_position_is_outside(self, player:PlayerPosition):
        return player.col < 1 or player.col > self.size or player.row < 1 or player.row > self.size
    
    def have_wall_between_players(self, player_1:PlayerPosition, player_2:PlayerPosition):
        if player_1.col == player_2.col and int(abs(player_1.row-player_2.row)) == 1:
            col_board = player_1.board_col
            row_board = (player_1.board_row+player_2.board_row)//2
            return self.board[col_board][row_board] != 0
        elif player_1.row == player_2.row and int(abs(player_1.col-player_2.col)) == 1:
            col_board = (player_1.board_col+player_2.board_col)//2
            row_board = player_1.board_row
            return self.board[col_board][row_board] != 0
        else:
            return False

    def set_wall_position(self, wall: WallPosition):
        position_wall = wall.boardPosition
        self.board[position_wall[0][0]][position_wall[0][1]] = self.wall_number
        self.board[position_wall[1][0]][position_wall[1][1]] = self.wall_number
        self.board[position_wall[2][0]][position_wall[2][1]] = self.wall_number
        
    def remove_wall_position(self, wall: WallPosition):
        position_wall = wall.boardPosition
        self.board[position_wall[0][0]][position_wall[0][1]] = 0
        self.board[position_wall[1][0]][position_wall[1][1]] = 0
        self.board[position_wall[2][0]][position_wall[2][1]] = 0
    
    def wall_may_be_blocking(self,wall: WallPosition):
        position_wall = wall.boardPosition
        wall_1 = (position_wall[0][0],position_wall[0][1])
        wall_2 = (position_wall[2][0],position_wall[2][1])
        
        if(wall.move.move_type=='h'):
            bottom_left = (wall_1[0]-1,wall_1[1]-1)
            bottom_middle = (wall_1[0]+1,wall_1[1]-1)
            bottom_right = (wall_2[0]+1,wall_2[1]-1)
            right = (wall_2[0]+1,wall_2[1])
            top_right = (wall_2[0]+1,wall_2[1]+1)   
            top_middle = (wall_1[0]+1,wall_1[1]+1)
            top_left = (wall_1[0]-1,wall_1[1]+1)
            left = (wall_1[0]-1,wall_1[1])
        else:
            bottom_left = (wall_2[0]-1,wall_2[1]+1)
            bottom_middle = (wall_2[0]-1,wall_2[1]-1)
            bottom_right = (wall_1[0]-1,wall_1[1]-1)
            right= (wall_1[0],wall_1[1]-1)
            top_right = (wall_1[0]+1,wall_1[1]-1)
            top_middle = (wall_2[0]+1,wall_2[1]-1)
            top_left = (wall_2[0]+1,wall_2[1]+1)
            left = (wall_2[0],wall_2[1]+1)
            
        bottom_left_is_blocking = not self.player_can_move_on_position(bottom_left[0],bottom_left[1])
        bottom_middle_is_blocking = not self.player_can_move_on_position(bottom_middle[0],bottom_middle[1])
        bottom_right_is_blocking = not self.player_can_move_on_position(bottom_right[0],bottom_right[1])
        right_is_blocking = not self.player_can_move_on_position(right[0],right[1])
        top_right_is_blocking = not self.player_can_move_on_position(top_right[0],top_right[1])
        top_middle_is_blocking = not self.player_can_move_on_position(top_middle[0],top_middle[1])
        top_left_is_blocking = not self.player_can_move_on_position(top_left[0],top_left[1])
        left_is_blocking = not self.player_can_move_on_position(left[0],left[1])
        
        return \
        (bottom_left_is_blocking and bottom_middle_is_blocking) or \
        (bottom_left_is_blocking and bottom_right_is_blocking) or \
        (bottom_left_is_blocking and right_is_blocking) or \
        (bottom_left_is_blocking and top_right_is_blocking) or \
        (bottom_left_is_blocking and top_middle_is_blocking) or \
        \
        (bottom_middle_is_blocking and bottom_right_is_blocking) or \
        (bottom_middle_is_blocking and right_is_blocking) or \
        (bottom_middle_is_blocking and top_right_is_blocking) or \
        (bottom_middle_is_blocking and top_left_is_blocking) or \
        (bottom_middle_is_blocking and left_is_blocking) or \
        \
        (bottom_right_is_blocking and top_middle_is_blocking) or \
        (bottom_right_is_blocking and top_left_is_blocking) or \
        (bottom_right_is_blocking and left_is_blocking) or \
        \
        (right_is_blocking and top_middle_is_blocking) or \
        (right_is_blocking and top_left_is_blocking) or \
        (right_is_blocking and left_is_blocking) or \
        \
        (top_right_is_blocking and top_middle_is_blocking) or \
        (top_right_is_blocking and top_left_is_blocking) or \
        (top_right_is_blocking and left_is_blocking) or \
        \
        (top_middle_is_blocking and top_left_is_blocking) or \
        (top_middle_is_blocking and left_is_blocking) 
                
        
    def player_can_move_on_position(self,x1,y1):
        if(x1<0):
            return False
        elif(x1>=self.maxBoardSize):
            return False
        elif(y1<0):
            return False
        elif(y1>=self.maxBoardSize):
            return False
        else:
            return self.board[x1][y1] == 0 
        
    def wall_is_blocking_player_to_reach_end(self, wall: WallPosition,player1:PlayerPosition,player2:PlayerPosition):
        
        if(not self.wall_may_be_blocking(wall)):
            return False
                     
        # We suppose that the wall is on the board
        self.set_wall_position(wall)
        
        # Check if a path exists for both players using DFS
        player1_can_reach = self._dfs(player1.board_position, self.maxBoardSize - 1, set())
        player2_can_reach = self._dfs(player2.board_position, 0, set())
        
        # We remove the wall from the graph
        self.remove_wall_position(wall)
        
        return not player1_can_reach or not player2_can_reach

    def _dfs(self, position, target_y, visited):
        if position[1] == target_y:
            return True
        
        visited.add(position)
        
        neighborMoves = [(0,1),(1,0),(-1,0),(0,-1)]
        for neighborMove in neighborMoves:
            wall_between = (position[0]+neighborMove[0],position[1]+neighborMove[1])
            neighbor = (wall_between[0]+neighborMove[0],wall_between[1]+neighborMove[1])
            
            # if neighbor is outside the board or is a wall, we skip it
            if neighbor[0] < 0 or neighbor[0] >= self.maxBoardSize or neighbor[1] < 0 or neighbor[1] >= self.maxBoardSize:
                continue
            if self.board[wall_between[0]][wall_between[1]] == self.wall_number:
                continue
            
            if neighbor not in visited:
                if self._dfs(neighbor, target_y, visited):
                    return True

        return False
    
    def getBoardInTwoDimention(self):
        return self.board
    
    def wall_is_on_something(self, wall: WallPosition):
        position_wall = wall.boardPosition
        return self.board[position_wall[0][0]][position_wall[0][1]] != 0 \
            or self.board[position_wall[1][0]][position_wall[1][1]] != 0 \
            or self.board[position_wall[2][0]][position_wall[2][1]] != 0

    def clone(self):
        new_board = Board(self.size,self.wall_number) 
        #todo le probleme c'est que ut cree le board pour rien la dans le constructeur
        new_board.board = np.copy(self.board)
        return new_board
