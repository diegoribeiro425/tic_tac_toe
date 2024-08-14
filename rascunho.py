espacos = 5
line_len = (espacos * 3) + 3
col_len = 10
matriz = []
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

for i in range(col_len):
    linhas = []
    for j in range(line_len):
        if i == 0:
            if j in abc:
                linhas.append(abc[j])
            else:
                linhas.append(' ')
            continue
        elif j == 0:
            if i in line_indexes:
                linhas.append(line_indexes[i])
            else:
                linhas.append('  ')
        elif j == 6 or j == 12:
            linhas.append('|')
        elif i == 3 or i == 6:
            linhas.append('_')
        else:
            linhas.append(' ')
    matriz.append(linhas)

for row in matriz:
    print(''.join(row))
