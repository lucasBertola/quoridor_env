import numpy as np

from .Move import MoveWall
from .Move import PlayerMove
from .BoardGraph import BoardGraph
from .BoardGraph import Edge
from .BoardGraph import Node

class PlayerPosition():
    def __init__(self, col, row):
        self.col = col
        self.row = row
        
        self.board_col = (col-1)*2
        self.board_row = (row-1)*2
        
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
    def __init__(self, size=3):
        self.size = size
        self.board = np.zeros((self.maxBoardSize(),self.maxBoardSize()), dtype=np.int8)
        self.boardGraph = BoardGraph(self.maxBoardSize())

    def maxBoardSize(self):
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

    def set_wall_position(self, wall: WallPosition, value,player_1:PlayerPosition, player_2:PlayerPosition):
        position_wall = wall.boardPosition
        self.board[position_wall[0][0]][position_wall[0][1]] = value
        self.board[position_wall[1][0]][position_wall[1][1]] = value
        self.board[position_wall[2][0]][position_wall[2][1]] = value
        
        wall_1 = (position_wall[0][0],position_wall[0][1])
        wall_2 = (position_wall[2][0],position_wall[2][1])
        
        if(wall.move.move_type=='v'):
            edge1 = Edge(Node(wall_1[0]-1,wall_1[1]),Node(wall_1[0]+1,wall_1[1]))
            edge2 = Edge(Node(wall_2[0]-1,wall_2[1]),Node(wall_2[0]+1,wall_2[1]))
        else:
            edge1 = Edge(Node(wall_1[0],wall_1[1]-1),Node(wall_1[0],wall_1[1]+1))
            edge2 = Edge(Node(wall_2[0],wall_2[1]-1),Node(wall_2[0],wall_2[1]+1))
              
        self.boardGraph.remove_edges(edge1,edge2,Node(player_1.board_col,player_1.board_row),Node(player_2.board_col,player_2.board_row))

    def wall_is_blocking_player_to_reach_end(self, wall: WallPosition,player1:PlayerPosition,player2:PlayerPosition):
        #todo doublon
        position_wall = wall.boardPosition
        wall_1 = (position_wall[0][0],position_wall[0][1])
        wall_2 = (position_wall[2][0],position_wall[2][1])
        
        if(wall.move.move_type=='v'):
            edge1 = Edge(Node(wall_1[0]-1,wall_1[1]),Node(wall_1[0]+1,wall_1[1]))
            edge2 = Edge(Node(wall_2[0]-1,wall_2[1]),Node(wall_2[0]+1,wall_2[1]))
        else:
            edge1 = Edge(Node(wall_1[0],wall_1[1]-1),Node(wall_1[0],wall_1[1]+1))
            edge2 = Edge(Node(wall_2[0],wall_2[1]-1),Node(wall_2[0],wall_2[1]+1))
        
        return not self.boardGraph.edges_can_be_removed(edge1,edge2,Node(player1.board_col,player1.board_row),Node(player2.board_col,player2.board_row))

    def getBoardInTwoDimention(self):
        return self.board
    
    def wall_is_on_something(self, wall: WallPosition):
        position_wall = wall.boardPosition
        return self.board[position_wall[0][0]][position_wall[0][1]] != 0 \
            or self.board[position_wall[1][0]][position_wall[1][1]] != 0 \
            or self.board[position_wall[2][0]][position_wall[2][1]] != 0

    def clone(self):
        new_board = Board(self.size)
        new_board.board = np.copy(self.board)
        new_board.boardGraph = self.boardGraph.clone()
        return new_board
