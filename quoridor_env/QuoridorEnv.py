from .Move import MoveWall
from .Move import Move
from .Move import PlayerMove
from .Board import Board
from .Board import PlayerPosition,WallPosition


class QuoridorEnv():
    WIN_REWARD = 1
    player_1_number = 1
    player_2_number = 2
    wall_number = -1

    def __init__(self, player_1_name='player1',player_2_name='player2', size=3):
        self.size = size
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name

    def reset(self, seed=None):
        self.board = Board(self.size,self.wall_number)
        self.last_move_row = None
        self.last_move_col = None
        self.last_move_type = None
        self.player_1_position = PlayerPosition(int((self.size+1)/2), 1)
        self.player_2_position = PlayerPosition(int((self.size+1)/2), self.size)
        self.position_row_player_2 = self.size 
        self.wall_left_player_1 = self.size+1
        self.wall_left_player_2 = self.size+1 
        self.board.set_player_position(self.player_1_position,self.player_1_number)
        self.board.set_player_position(self.player_2_position,self.player_2_number)
        self.invalid_move_has_been_played = False
        self.next_player_to_play = self.player_1_number

    def play(self, move: Move):
        self.playMove(move)

        result, is_finish = self.is_finish()
        
        self.switch_player()
        
        if is_finish:            
            return result, True

        return 0, False

    def is_finish(self):
        #return 0, False if not finish
        #return player_who_won, True if finish
        if self.invalid_move_has_been_played:
            return  self.player_2_number if self.next_player_to_play == self.player_1_number else self.player_1_number, True
        
        # Check if player 1 has reached the last row
        if self.player_1_position.row == self.size:
            return self.player_1_number, True

        # Check if player 2 has reached the first row
        if self.player_2_position.row == 1:
            return self.player_2_number, True
        return 0, False
        
    def is_move_valid(self, move: Move):
        if move.is_pawn_move():
            move:PlayerMove=move
            
            playerPosition = self.player_1_position if self.next_player_to_play == self.player_1_number else self.player_2_position
            newPlayerPosition = playerPosition.move(move)
                        
            if(move.is_diagonal()):
                # Check if there is a player to jump over (two players position is possible)
                player_in_front_1 = PlayerPosition(playerPosition.col+move.col_change, playerPosition.row)
                player_in_front_2 = PlayerPosition(playerPosition.col, playerPosition.row + move.row_change)

                if(not self.board.position_is_player(player_in_front_1) and not self.board.position_is_player(player_in_front_2)):
                    return False
                
                player_in_front = player_in_front_1 if self.board.position_is_player(player_in_front_1) else player_in_front_2
                
                player_if_he_jump = PlayerPosition(player_in_front.col+(player_in_front.col-playerPosition.col), player_in_front.row +(player_in_front.row-playerPosition.row))
                
                if(not self.board.player_position_is_outside(player_if_he_jump) and not self.board.have_wall_between_players(player_if_he_jump,player_in_front)):
                    return False

                # check if there is no wall between second player and new position
                if(self.board.have_wall_between_players(newPlayerPosition,player_in_front)):
                    return False
            
            #jump over player
            if(not move.is_diagonal() and self.board.position_is_player(newPlayerPosition)):
                 #check if wall between 
                if(self.board.have_wall_between_players(playerPosition,newPlayerPosition)):
                    return False
                
                playerPosition = newPlayerPosition
                newPlayerPosition = newPlayerPosition.move(move)
                
                if(self.board.player_position_is_outside(newPlayerPosition)):
                    return False
                
            if(not move.is_diagonal() and self.board.have_wall_between_players(playerPosition,newPlayerPosition)):
                return False
            
            # Check if outside
            if(self.board.player_position_is_outside(newPlayerPosition)):
                return False 
                
        else:#wall
            wall: MoveWall = move
            wall_left = self.wall_left_player_1 if self.next_player_to_play == self.player_1_number else self.wall_left_player_2
            
            # check if there is some wall left
            if(wall_left <= 0):
                return False
            
            #check if wall it not on something else
            if(self.board.wall_is_on_something(WallPosition(wall))):
                 return False
             
             #check if wall is not blocking a player to reach the end
            if(self.board.wall_is_blocking_player_to_reach_end(WallPosition(wall),self.player_1_position,self.player_2_position)):
                 return False
            
        return True
    
    def playMove(self, move: Move):
        
        if(not self.is_move_valid(move)):
            self.invalid_move_has_been_played = True
            return

        if move.is_pawn_move():
            move:PlayerMove=move
            # Gérer le mouvement du pion
            playerPosition = self.player_1_position if self.next_player_to_play == self.player_1_number else self.player_2_position
            newPlayerPosition = playerPosition.move(move)

            #jump over player
            if(self.board.position_is_player(newPlayerPosition)):
                newPlayerPosition = newPlayerPosition.move(move)
            
            self.board.set_player_position(playerPosition,0)
            self.board.set_player_position(newPlayerPosition,self.next_player_to_play)
            
            if(self.next_player_to_play == self.player_1_number):
                self.player_1_position = newPlayerPosition
            else:
                self.player_2_position = newPlayerPosition
        else:  # Gérer le placement du mur
            move:MoveWall=move
            self.board.set_wall_position(WallPosition(move))
            
            if self.next_player_to_play == self.player_1_number:
                self.wall_left_player_1 -= 1
            else:
                self.wall_left_player_2 -= 1
                
    def inverse_player_position(self):
        #todo
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
        new_env = QuoridorEnv(self.player_1_name, self.player_2_name, self.size)
        new_env.size = self.size
        new_env.next_player_to_play = self.next_player_to_play
        new_env.board = self.board.clone()
        new_env.last_move_row = self.last_move_row
        new_env.last_move_col = self.last_move_col
        new_env.last_move_type = self.last_move_type
        new_env.invalid_move_has_been_played = self.invalid_move_has_been_played
        
        new_env.player_1_position = self.player_1_position
        new_env.player_2_position = self.player_2_position 
        
        new_env.wall_left_player_1 = self.wall_left_player_1
        new_env.wall_left_player_2 = self.wall_left_player_2
        
        new_env.player_1_name = self.player_1_name
        new_env.player_2_name = self.player_2_name
                
        return new_env

    def render(self):
        board = self.board.getBoardInTwoDimention()
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
                        elif(board[col][row]==self.wall_number):
                            output+='---'
                        else:
                            output+='   '
                
                else:#isOnPlayerRow==True
                    if(col==-1):
                        output+='|'
                    elif(col==self.size*2-1):
                        output+='|'
                    elif(board[col][row] == self.player_1_number or board[col][row] == self.player_2_number):
                        output+=' '+str(board[col][row])+' '
                    # elif(board[col][row]==self.wall_number):
                    #     output+='---'
                    elif(col%2==1 and board[col][row]==self.wall_number):
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