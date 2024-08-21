from board import Board


class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self, name: str, symbol: str, board: Board):
        self.player = Player(name, symbol)
        self.board = board
        self.play_coordinates = {
            'A1': self.board.board_matrix[2][3],
            'A2': self.board.board_matrix[2][9],
            'A3': self.board.board_matrix[2][15],
            'B1': self.board.board_matrix[5][3],
            'B2': self.board.board_matrix[5][9],
            'B3': self.board.board_matrix[5][15],
            'C1': self.board.board_matrix[8][3],
            'C2': self.board.board_matrix[8][9],
            'C3': self.board.board_matrix[8][15],
        }

    def make_a_play(self, board_pos: str, player_: Player):
        board_pos.upper()
        is_repeated = True
        while is_repeated:
            if self.play_coordinates[board_pos] != ' ':
                print('This position already filled. Try another one.')
            else:
                self.play_coordinates[board_pos] = player_.symbol
                is_repeated = False

    def game_over(self) -> bool:
        # horizontal
        if self.play_coordinates['A1'] == self.play_coordinates['B1'] == self.play_coordinates['C1']:
            return True
        elif self.play_coordinates['A2'] == self.play_coordinates['B2'] == self.play_coordinates['C2']:
            return True
        elif self.play_coordinates['A3'] == self.play_coordinates['B3'] == self.play_coordinates['C3']:
            return True
        # vertical
        elif self.play_coordinates['A1'] == self.play_coordinates['A2'] == self.play_coordinates['A3']:
            return True
        elif self.play_coordinates['B1'] == self.play_coordinates['B2'] == self.play_coordinates['B3']:
            return True
        elif self.play_coordinates['C1'] == self.play_coordinates['C2'] == self.play_coordinates['C3']:
            return True
        # diagonal
        elif self.play_coordinates['A1'] == self.play_coordinates['B2'] == self.play_coordinates['C3']:
            return True
        elif self.play_coordinates['C1'] == self.play_coordinates['B2'] == self.play_coordinates['A3']:
            return True
        else:
            return False



