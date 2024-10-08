from board import Board


class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol
        self.score = 0


class Game:
    def __init__(self, player: Player, board: Board):
        self.player = player
        self.board = board

    def make_a_move(self, board_pos: str):
        i = self.board.play_coordinates[board_pos][0]
        j = self.board.play_coordinates[board_pos][1]
        self.board.board_matrix[i][j] = self.player.symbol

    def move_check(self, board_pos: str) -> bool:
        if board_pos not in self.board.play_coordinates:
            return True
        i = self.board.play_coordinates[board_pos][0]
        j = self.board.play_coordinates[board_pos][1]
        if self.board.board_matrix[i][j] in ['X', 'O']:
            return True

    def game_over(self) -> bool:
        # horizontal
        if self.win_test_possibilities(self.board.lines):
            print(f'{self.player.name} wins!')
            self.player.score += 1
            return True
        # vertical
        elif self.win_test_possibilities(self.board.rows):
            print(f'{self.player.name} wins!')
            self.player.score += 1
            return True
        # diagonal
        elif self.win_test_possibilities(self.board.diagonals):
            print(f'{self.player.name} wins!')
            self.player.score += 1
            return True
        # draw
        elif self.draw():
            print('DRAW!')
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

    def check(self, player_: Player):
        move = input(f'{player_.name} move: ').upper()
        while self.move_check(move):
            print('Invalid move.')
            move = input(f'{player_.name} move: ').upper()
        return move

    def scoreboard(self, player_: Player):
        print(f'\n{self.player.name} {self.player.score} X {player_.score} {player_.name}')
