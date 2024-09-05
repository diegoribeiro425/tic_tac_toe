from board import Board
from ascii_art import ascii_art
from game import Player, Game

print(ascii_art)
print('-------------------------------------------------------------------------------------------------------------\n')
name1 = input('Type the name of player 1: ')
name2 = input('Type the name of player 2: ')
player1 = Player(name1, symbol='X')
player2 = Player(name2, symbol='O')
board = Board()


def setup_new_game(board_: Board):
    player1_play_ = Game(player1, board_)
    player2_play_ = Game(player2, board_)
    return player1_play_, player2_play_


player1_play, player2_play = setup_new_game(board)
is_gameover = False
player1_play.scoreboard(player2)
board.board_draw()


while not is_gameover:
    # player 1 move
    p1_move = player1_play.check(player1)
    player1_play.make_a_move(p1_move)
    board.board_draw()
    if player1_play.game_over():
        another_round = input('Do you want to play another round (y/n)?: ').upper()
        if another_round == 'Y':
            board = Board()
            player1_play, player2_play = setup_new_game(board)
            player1_play.scoreboard(player2)
            board.board_draw()
            is_gameover = False
            continue
        else:
            is_gameover = True
            break

    # player 2 move
    p2_move = player2_play.check(player2)
    player2_play.make_a_move(p2_move)
    board.board_draw()
    if player2_play.game_over():
        another_round = input('Do you want to play another round (y/n)?: ').upper()
        if another_round == 'Y':
            board = Board()
            player1_play, player2_play = setup_new_game(board)
            player1_play.scoreboard(player2)
            board.board_draw()
            is_gameover = False
            continue
        else:
            is_gameover = True
