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
        self.matrix = []
        self.board_matrix = self.board_construction()
        self.play_coordinates = {
            'A1': [2, 3],
            'A2': [2, 9],
            'A3': [2, 15],
            'B1': [5, 3],
            'B2': [5, 9],
            'B3': [5, 15],
            'C1': [8, 3],
            'C2': [8, 9],
            'C3': [8, 15],
        }
        self.lines = [
            {
                'A1': [2, 3],
                'B1': [5, 3],
                'C1': [8, 3]
            },
            {
                'A2': [2, 9],
                'B2': [5, 9],
                'C2': [8, 9]
            },
            {
                'A3': [2, 15],
                'B3': [5, 15],
                'C3': [8, 15]
            }

        ]
        self.rows = [
            {
                'A1': [2, 3],
                'A2': [2, 9],
                'A3': [2, 15]
            },
            {
                'B1': [5, 3],
                'B2': [5, 9],
                'B3': [5, 15]
            },
            {
                'C1': [8, 3],
                'C2': [8, 9],
                'C3': [8, 15]
            }
        ]
        self.diagonals = [

            {
                'A1': [2, 3],
                'B2': [5, 9],
                'C3': [8, 15]
            },
            {
                'A3': [2, 15],
                'B2': [5, 9],
                'C1': [8, 3]
            }

        ]

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
            self.matrix.append(line)
        return self.matrix

    def board_draw(self):

        for row in self.board_matrix:
            print(''.join(row))
