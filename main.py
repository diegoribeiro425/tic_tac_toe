from board import Board
from ascii_art import ascii_art
from game import Player, Game

print(ascii_art)
print('-------------------------------------------------------------------------------------------------------------\n')
name1 = input('Type the name of player 1: ')
name2 = input('Type the name of player 2: ')
board = Board()
player1 = Player(name1, 'X')
player2 = Player(name2, 'O')
game_player1 = Game(player1, board)
game_player2 = Game(player2, board)
is_gameover = False
board.board_draw()


def check(player: Player, game_player: Game):
    move = input(f'{player.name} move: ').upper()
    while game_player.move_check(move):
        print('Invalid move.')
        move = input(f'{player.name} move: ').upper()
    return move


while not is_gameover:
    # player 1 move
    p1_move = check(player1, game_player1)
    game_player1.make_a_move(p1_move)
    board.board_draw()
    if game_player1.game_over():
        is_gameover = True
        break
    # player 2 move
    p2_move = check(player2, game_player2)
    game_player2.make_a_move(p2_move)
    board.board_draw()
    if game_player2.game_over():
        is_gameover = True
