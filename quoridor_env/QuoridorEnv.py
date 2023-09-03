import numpy as np

from .Move import MoveWall
from .Move import Move
from .Move import PlayerMove

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
        self.position_col_player_1 = int((self.size+1)/2)
        self.position_row_player_1 = 1
        self.position_col_player_2 = int((self.size+1)/2)
        self.position_row_player_2 = self.size 
        self.wall_left_player_1 = self.size+1
        self.wall_left_player_2 = self.size+1 
        self.set_board_case_with_player_notation(self.position_col_player_1, self.position_row_player_1, self.player_1_number)
        self.set_board_case_with_player_notation(self.position_col_player_2, self.position_row_player_2, self.player_2_number)
        self.invalid_move_has_been_played = False

        self.next_player_to_play = self.player_1_number
        return self.board, {}
    
    def play(self, move: Move):
        self.playMove(move)

        result, is_finish = self.is_finish()
        
        self.switch_player()
        
        if is_finish:            
            return result, True

        return 0, False
    
    def maxBoardSize(self):
        return (self.size*2)-1



    def is_finish(self):
        #return 0, False if not finish
        #return player_who_won, True if finish
        if self.invalid_move_has_been_played:
            return  self.player_2_number if self.next_player_to_play == self.player_1_number else self.player_1_number, True
        
        # Check if player 1 has reached the last row
        if self.position_row_player_1 == self.size:
            return self.player_1_number, True

        # Check if player 2 has reached the first row
        if self.position_row_player_2 == 1:
            return self.player_2_number, True
        return 0, False
    
    def get_board_case_with_player_notation(self, col, row):
        return (col-1)*2, (row-1)*2
    
    def set_board_case_with_player_notation(self, col, row, value):
        x,y = self.get_board_case_with_player_notation(col, row)
        self.board[x][y] = value
        
    def insert_wall(self, wall: MoveWall):
        if(wall.move_type=='v'):
            x = (wall.col-1)*2 +1
            y = (wall.row-1)*2
            self.board[x][y] = self.wall_number
            self.board[x][y+1] = self.wall_number
            self.board[x][y+2] = self.wall_number
        else: # wall.move_type=='h'
            x = (wall.col-1)*2
            y = (wall.row-1)*2 +1
            self.board[x][y] = self.wall_number
            self.board[x+1][y] = self.wall_number
            self.board[x+2][y] = self.wall_number
            
        if self.next_player_to_play == self.player_1_number:
            self.wall_left_player_1 -= 1
        else:
            self.wall_left_player_2 -= 1
    
    def board_position_is_player(self, col, row):
        return self.board[col][row] == self.player_1_number or self.board[col][row] == self.player_2_number
     
    def is_move_valid(self, move: Move):
        if move.is_pawn_move():
            if(self.next_player_to_play == self.player_1_number):
                position_col = self.position_col_player_1
                position_row = self.position_row_player_1
            else:
                position_col = self.position_col_player_2
                position_row = self.position_row_player_2
            
            row_change, col_change = move.row_change, move.col_change
            new_row = position_row + row_change
            new_col = position_col + col_change
           
            is_diagonal = row_change != 0 and col_change != 0
           
            old_x,old_y = self.get_board_case_with_player_notation(position_col,position_row )
            x,y = self.get_board_case_with_player_notation(new_col,new_row )
                        
            if(is_diagonal):
                # Check if there is a player to jump over
                front_row_1 = position_row + row_change
                front_col_1 = position_col
                front_row_2 = position_row
                front_col_2 = position_col + col_change
                
                front_x1, front_y1 = self.get_board_case_with_player_notation(front_col_1, front_row_1)
                front_x2, front_y2 = self.get_board_case_with_player_notation(front_col_2, front_row_2)
                
                if (not self.board_position_is_player(front_x1,front_y1) and not self.board_position_is_player(front_x2,front_y2)):
                    return False

                # Check if there is a wall behind the player
                front_x,front_y = (front_x1, front_y1) if self.board_position_is_player(front_x1,front_y1) else (front_x2, front_y2)
                
                back_x = front_x + int((front_x - old_x)/2)
                back_y = front_y + int((front_y - old_y)/2)
                
                back_is_outside = back_x <= 0 or back_x >= self.maxBoardSize() or back_y <= 0 or back_y >= self.maxBoardSize()

                if(not back_is_outside and self.board[back_x][back_y] != self.wall_number):
                    return False
            
                # check if there is no wall between second player and new position
                wall_x = int((x+front_x)/2)
                wall_y = int((y+front_y)/2)
                if(self.board[wall_x][wall_y] == self.wall_number):
                    return False
            
            #jump over player
            if(not is_diagonal and self.board_position_is_player(x,y)):
                 #check if wall between 
                if(self.board[int((x+old_x)/2)][int((y+old_y)/2)] == self.wall_number):
                    return False
                #todo check if wall between
                #todo check si a pas de mur derriere
                position_col = new_col
                position_row = new_row
                new_row = position_row + row_change
                new_col = position_col + col_change
                old_x,old_y = self.get_board_case_with_player_notation(position_col,position_row )
                x,y = self.get_board_case_with_player_notation(new_col,new_row )
                
                #check if it s not outside
                if new_row <= 0 or new_row > self.size or new_col <= 0 or new_col > self.size:
                    return False  
                
            if(not is_diagonal) :
                #check if wall between 
                if(self.board[int((x+old_x)/2)][int((y+old_y)/2)] == self.wall_number):
                    return False
            
            # Check if outside
            if new_row <= 0 or new_row > self.size or new_col <= 0 or new_col > self.size:
                return False  
                
                
                
        else:#wall
            #todo check is wall is valide
            #todo verifier si il y a assez de mur
            #todo verifier si y a pas de mur a cet endroit qui bloque
            #todo verifier si ce mur n'empeche pas un joueur d'arriver a la ligne d'arrivée
    
            return True
        return True
    
    def playMove(self, move: Move):
        
        if(not self.is_move_valid(move)):
            self.invalid_move_has_been_played = True
            return

        if move.is_pawn_move():
        
            # Gérer le mouvement du pion
            if(self.next_player_to_play == self.player_1_number):
                position_col = self.position_col_player_1
                position_row = self.position_row_player_1
            else:
                position_col = self.position_col_player_2
                position_row = self.position_row_player_2
            
            row_change, col_change = move.row_change, move.col_change
            
            new_row = position_row + row_change
            new_col = position_col + col_change
           
            #jump over player
            x,y = self.get_board_case_with_player_notation(new_col,new_row )
            if(self.board_position_is_player(x,y)):
                new_row = new_row + row_change
                new_col = new_col + col_change
            
            self.set_board_case_with_player_notation(position_col, position_row, 0)
            self.set_board_case_with_player_notation(new_col, new_row, self.next_player_to_play)
            
            if(self.next_player_to_play == self.player_1_number):
                self.position_col_player_1 = new_col
                self.position_row_player_1 = new_row
            else:
                self.position_col_player_2 = new_col
                self.position_row_player_2 = new_row
        else:
            # Gérer le placement du mur
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
        
        new_env.wall_left_player_1 = self.wall_left_player_1
        new_env.wall_left_player_2 = self.wall_left_player_2
        
        new_env.player_1_name = self.player_1_name
        new_env.player_2_name = self.player_2_name
        
        return new_env

    def render(self):
        output = ""

        # Afficher les murs restants pour le joueur 2
        output+="Player 2 : "+str(self.wall_left_player_2)+" walls left\n"

        # Afficher les lignes du plateau
        for row in range(self.size*2-1, -2, -1):
            # Afficher les murs horizontaux et les pions
            if(row%2==0):
                isOnPlayerRow = True
                PlayerRow = row/2+1
                output+=' '+str(int(PlayerRow))+' '
            else:
                isOnPlayerRow = False
                output+='   '
           
            for col in range(-1, self.size*2):
                isOnPlayerCol = row%2==0
                if(isOnPlayerRow==False):
                    if(row == -1 or row == self.size*2-1):
                        if(col%2==1):
                            output+='+'
                        else:
                            output+='---'
                    else:
                        if(col%2==1):
                            output+='+'
                        elif(self.board[col][row]==self.wall_number):
                            output+='---'
                        else:
                            output+='   '
                
                else:#isOnPlayerRow==True
                    if(col==-1):
                        output+='|'
                    elif(col==self.size*2-1):
                        output+='|'
                    elif(self.board_position_is_player(col,row)):
                        output+=' '+str(self.board[col][row])+' '
                    # elif(self.board[col][row]==self.wall_number):
                    #     output+='---'
                    elif(col%2==1 and self.board[col][row]==self.wall_number):
                        output+='|'
                    elif(col%2==1):
                        output+=' '
                    else:
                        output+='   '
                        
                    
                # output+=str(col)
            output += "\n"

        
        # Afficher les murs restants pour le joueur 1


        # Afficher les numéros de colonne
        output += "  "
        for col in range(1, self.size + 1):
            output += "   " + str(col)
        output += "\n"
        
        output+="Player 1 : "+str(self.wall_left_player_1)+" walls left"
        
        return output