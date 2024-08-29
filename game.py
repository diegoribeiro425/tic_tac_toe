from board import Board


class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self, player: Player, board: Board):
        self.player = player
        self.board = board

    def make_a_move(self, board_pos: str):
        board_pos.upper()
        i = self.board.play_coordinates[board_pos][0]
        j = self.board.play_coordinates[board_pos][1]
        self.board.board_matrix[i][j] = self.player.symbol

    def is_occupied(self, board_pos) -> bool:
        board_pos.upper()
        i = self.board.play_coordinates[board_pos][0]
        j = self.board.play_coordinates[board_pos][1]
        if self.board.board_matrix[i][j] in ['X', 'O']:
            return True

    def game_over(self) -> bool:
        # horizontal
        if self.win_test_possibilities(self.board.lines):
            return True
        # vertical
        elif self.win_test_possibilities(self.board.rows):
            return True
        # diagonal
        elif self.win_test_possibilities(self.board.diagonals):
            return True
        # draw
        elif self.draw():
            return True
        else:
            return False

    def win_test_possibilities(self, possibilitie_list) -> bool:
        for index in range(len(possibilitie_list)):
            test_list = []
            for key in possibilitie_list[index]:
                i = possibilitie_list[index][key][0]
                j = possibilitie_list[index][key][1]
                test_list.append(self.board.board_matrix[i][j])
            test_set = set(test_list)
            if len(test_set) == 1 and ' ' not in test_set:
                return True
        return False

    def draw(self) -> bool:
        all_board_positions = []
        for key in self.board.play_coordinates:
            i = self.board.play_coordinates[key][0]
            j = self.board.play_coordinates[key][1]
            all_board_positions.append(self.board.board_matrix[i][j])
            if ' ' not in all_board_positions:
                return True
        return False
