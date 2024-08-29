# espacos = 5
# line_len = (espacos * 3) + 3
# col_len = 10
# matriz = []
# abc = {
#     4: 'A',
#     10: 'B',
#     16: 'C'
# }
# line_indexes = {
#     2: '1 ',
#     5: '2 ',
#     8: '3 '
# }
#
# for i in range(col_len):
#     linhas = []
#     for j in range(line_len):
#         if i == 0:
#             if j in abc:
#                 linhas.append(abc[j])
#             else:
#                 linhas.append(' ')
#             continue
#         elif j == 0:
#             if i in line_indexes:
#                 linhas.append(line_indexes[i])
#             else:
#                 linhas.append('  ')
#         elif j == 6 or j == 12:
#             linhas.append('|')
#         elif i == 3 or i == 6:
#             linhas.append('_')
#         else:
#             linhas.append(' ')
#     matriz.append(linhas)
#
# # for row in matriz:
# #     print(''.join(row))
#
# matriz[2][3] = 'X'
# matriz[5][9] = 'X'
# matriz[8][15] = 'X'
# matriz[2][15] = 'O'
# matriz[5][3] = 'O'
# matriz[8][3] = 'O'
#
# for row in matriz:
#     print(''.join(row))
# letra = 'a1'
# print(letra.upper())
# print(type(letra))
# -------------------------------------------------------------------------------------------------------------------
from board import Board


class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self, player: Player, board_: Board):
        self.player = player
        self.board = board_
        self.test_set = set()
        self.test_list = []

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
            self.test_list = []
            for key in possibilitie_list[index]:
                i = possibilitie_list[index][key][0]
                j = possibilitie_list[index][key][1]
                self.test_list.append(self.board.board_matrix[i][j])
            self.test_set = set(self.test_list)
            if len(self.test_set) == 1 and ' ' not in self.test_set:
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


board = Board()
p1 = Player('hjsdjhksd', 'X')
p2 = Player('ksiksd', 'O')
game_p1 = Game(p1, board)
game_p2 = Game(p2, board)

game_p1.make_a_move('A2')

if game_p1.game_over():
    print('Game over')
board.board_draw()
game_p1.make_a_move('B2')

if game_p1.game_over():
    print('Game over')
board.board_draw()
game_p1.make_a_move('C2')

board.board_draw()
print(game_p1.game_over())
if game_p1.game_over():
    print('Game over')
print(game_p1.win_test_possibilities(board.lines))
print(board.lines[0]['A1'][1])
print(game_p1.test_set)
print(game_p1.test_list)
print(game_p1.game_over())
# for index in range(len(board.lines)):
#     for key in board.lines[index]:
#         i = board.lines[index][key][0]
#         j = board.lines[index][key][1]
#         print(board.board_matrix[i][j])
#         game_p1.test_list.append(board.board_matrix[i][j])

# --------------------------------------------------------------------------
# num = [1,2,3]
# num_set = set(num)
# num_set.add(3)
# print(num_set)
# test = set()
# print(type(test))
# print(num_set(0))
# -------------------------------------------------------------------------------

