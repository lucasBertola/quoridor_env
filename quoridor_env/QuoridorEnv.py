import numpy as np
from abc import ABC, abstractmethod


class Move(ABC):
    @abstractmethod
    def is_pawn_move(self):
        pass
    def is_wall_move(self):
        pass
    
class MoveWall(Move):
    def __init__(self, row, col, move_type, board_size):
        assert move_type in ['v', 'h'], "move_type must be 'v' or 'h'"
        
        assert 0 < row < board_size, "row must be between 0 and board_size"
        assert 0 < col < board_size, "col must be between 0 and board_size"
        
        self.row = row
        self.col = col
        self.move_type = move_type
        self.board_size = board_size

    def is_pawn_move(self):
        return False

    def is_wall_move(self):
        return True

class PlayerMove(Move):
    def __init__(self, direction):
        self.direction = direction
        assert direction in ['up', 'down', 'left', 'right', 'up_left', 'up_right', 'down_left', 'down_right'], "direction must be one of the valid directions"

        self.row_change=0
        self.col_change=0
        if direction == 'up':
            self.row_change = 1
            self.col_change = 0
        elif direction == 'down':
            self.row_change = -1
            self.col_change = 0
        elif direction == 'left':
            self.row_change = 0
            self.col_change = -1
        elif direction == 'right':
            self.row_change = 0
            self.col_change = 1
        elif direction == 'up_left':
            self.row_change = 1
            self.col_change = -1
        elif direction == 'up_right':
            self.row_change = 1
            self.col_change = 1
        elif direction == 'down_left':
            self.row_change = -1
            self.col_change = -1
        elif direction == 'down_right':
            self.row_change = -1
            self.col_change = 1
            
            
    def is_pawn_move(self):
        return True

    def is_wall_move(self):
        return False

class QuoridorEnv():
    WIN_REWARD = 1
    player_1_number = 1
    player_2_number = 2
    wall_number = -1

    def __init__(self, player_1_name='player1',player_2_name='player2', size=3):
        self.size = size
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.reset()

    def reset(self, seed=None):
        self.board = np.zeros((self.maxBoardSize(),self.maxBoardSize()), dtype=np.int8)
        self.last_move_row = None
        self.last_move_col = None
        self.last_move_type = None
        self.position_col_player_1 = (self.size+1)/2
        self.position_row_player_1 = 1
        self.position_col_player_2 = (self.size+1)/2
        self.position_row_player_2 = self.size 
        self.wall_left_player_1 = self.size+1
        self.wall_left_player_2 = self.size+1 
        self.invalid_move_has_been_played = False

        self.next_player_to_play = self.player_1_number

        return self.board, {}
    
    def play(self, move: Move):
        self.playMove(move)

        result, is_finish = self.is_finish()
        
        self.switch_player()
        
        if is_finish:            
            return self.board, result, True, False, {}

        return self.board, 0, False, False, {}
    
    def maxBoardSize(self):
        return (self.size*2)-1

    def is_move_valid(self, move: Move):
        #todo check if rang move if possible. if wall, test if no wall already there. if pawn, test if no pawn already there and if move is possible
        return True

    def is_finish(self):
        #return 0, False if not finish
        #return player_who_won, True if finish
        if self.invalid_move_has_been_played:
            return  self.player_2_number if self.next_player_to_play == self.player_1_number else self.player_1_name, True
        
        # Check if player 1 has reached the last row
        if self.position_row_player_1 == self.size:
            return self.player_1_number, True

        # Check if player 2 has reached the first row
        if self.position_row_player_2 == 1:
            return self.player_2_number, True
        return 0, False
    
    def set_board_case_with_player_notation(self, row, col, value):
        self.board[(row-1)*2][(col-1)*2] = value
        
    def insert_wall(self, wall: MoveWall):
        if(wall.move_type=='v'):
            x = (wall.col-1)*2 +1
            y = (wall.row-1)*2
            self.board[x][y] = self.wall_number
            self.board[x][y+1] = self.wall_number
        else: # wall.move_type=='h'
            x = (wall.col-1)*2
            y = (wall.row-1)*2 +1
            self.board[x][y] = self.wall_number
            self.board[x+1][y] = self.wall_number

    def playMove(self, move: Move):

        if move.is_pawn_move():
            # Gérer le mouvement du pion
            if(self.next_player_to_play == self.player_1_number):
                position_col = self.position_col_player_1
                position_row = self.position_row_player_1
            else:
                position_col = self.position_col_player_2
                position_row = self.position_row_player_2
            
            row_change, col_change = move.row_change, move.col_change
            
            #todo , si y a un joueur ca peut etre sauté et faire un deplacement en plus
            new_row = position_row + row_change
            new_col = position_col + col_change
            
            #todo verifier si le deplacement est legal (pas de mur, diagonal autorisé)
            if new_row <= 0 or new_row > self.size or new_col <= 0 or new_col > self.size:
                self.invalid_move_has_been_played = True
                return
            
            self.set_board_case_with_player_notation(position_row, position_col, 0)
            self.set_board_case_with_player_notation(new_row, new_col, self.next_player_to_play)
            
            if(self.next_player_to_play == self.player_1_number):
                self.position_col_player_1 = new_col
                self.position_row_player_1 = new_row
            else:
                self.position_col_player_2 = new_col
                self.position_row_player_2 = new_row
        else:
            # Gérer le placement du mur
            #todo verifier si y a pas de mur a cet endroit qui bloque
            #todo verifier si ce mur n'empeche pas un joueur d'arriver a la ligne d'arrivée
            #todo verifier si il y a assez de mur
            self.insert_wall(move)

        return

    
    def inverse_player_position(self):
        #todo
        # self.board = -self.board
        return
    
    def switch_player(self):
        if(self.next_player_to_play == self.player_1_number):
            self.next_player_to_play = self.player_2_number
        else:
            self.next_player_to_play = self.player_1_number
    
    def get_valid_actions(self):
        #todo
        return 
    
    def clone(self):
        new_env = QuoridorEnv(opponent=self._opponent, render_mode=self.render_mode, first_player=self.first_player)
        new_env.next_player_to_play = self.next_player_to_play
        new_env.board = self.board.copy()
        new_env.last_move_row = self.last_move_row
        new_env.last_move_col = self.last_move_col
        new_env.last_move_type = self.last_move_type
        new_env.invalid_move_has_been_played = self.invalid_move_has_been_played
        
        new_env.position_col_player_1 = self.position_col_player_1
        new_env.position_row_player_1 = self.position_row_player_1 
        new_env.position_col_player_2 = self.position_col_player_2
        new_env.position_row_player_2 = self.position_row_player_2
        
        return new_env

    def render(self):
        output = ""

        # Afficher les murs restants pour le joueur 2
        output += "   |" * self.wall_left_player_2 + "\n"

        # Afficher les numéros de colonne
        output += " "
        for col in range(1, self.size + 1):
            output += "   " + str(col)
        output += "\n"

        # Afficher les lignes du plateau
        for row in range(self.size, 0, -1):
            # Afficher les murs horizontaux et les pions
            for col in range(1, self.size + 1):
                cell_value = self.board[(row - 1) * 2][(col - 1) * 2]
                if cell_value == self.wall_number:
                    output += " - "
                elif cell_value == self.player_1_number:
                    output += " 1 "
                elif cell_value == self.player_2_number:
                    output += " 2 "
                else:
                    output += "   "
                if col < self.size:
                    output += "+" if self.board[(row - 1) * 2][(col - 1) * 2 + 1] == self.wall_number else " "
            output += "\n"

            # Afficher les murs verticaux et les numéros de ligne
            if row > 1:
                for col in range(1, self.size + 1):
                    output += "|" if self.board[(row - 1) * 2 - 1][(col - 1) * 2] == self.wall_number else " "
                    output += "   "
                output += str(row - 1) + "\n"

        # Afficher les murs restants pour le joueur 1
        output += "   |" * self.wall_left_player_1 + "\n"

        return output

