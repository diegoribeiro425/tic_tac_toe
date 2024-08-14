spaces = 5
line_len = (spaces * 3) + 3
col_len = 10

abc = {
    4: 'A',
    10: 'B',
    16: 'C'
}

line_indexes = {
    2: '1 ',
    5: '2 ',
    8: '3 '
}


class Board:
    def __init__(self):
        self.board_matrix = []

    def board_construction(self):
        for i in range(col_len):
            line = []
            for j in range(line_len):
                if i == 0:
                    if j in abc:
                        line.append(abc[j])
                    else:
                        line.append(' ')
                    continue
                elif j == 0:
                    if i in line_indexes:
                        line.append(line_indexes[i])
                    else:
                        line.append('  ')
                elif j == 6 or j == 12:
                    line.append('|')
                elif i == 3 or i == 6:
                    line.append('_')
                else:
                    line.append(' ')
            self.board_matrix.append(line)
        return self.board_matrix

    def board_draw(self):
        self.board_construction()
        for row in self.board_matrix:
            print(''.join(row))
