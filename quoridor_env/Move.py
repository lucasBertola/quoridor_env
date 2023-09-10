from abc import ABC, abstractmethod

    
class Move(ABC):
    @abstractmethod
    def is_pawn_move(self):
        pass
    def is_wall_move(self):
        pass
    
class MoveWall(Move):
    def __init__(self, col, row, move_type, board_size):
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
        
        self._is_diagonal = self.row_change != 0 and self.col_change != 0
            
            
    def is_pawn_move(self):
        return True

    def is_wall_move(self):
        return False
    
    def is_diagonal(self):
        return self._is_diagonal