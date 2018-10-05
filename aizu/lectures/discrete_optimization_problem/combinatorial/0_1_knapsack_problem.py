#! python3

n, w = list(map(int, input().split(' ')))
items = [list(map(int, input().split(' '))) for i in range(n)]

table = [[0 for j in range(w+1)] for i in range(n+1)]

for i in range(1, n+1):
    v_i, w_i = items[i-1]
    for j in range(1, w+1):
        if j - w_i < 0:
            table[i][j] = max(table[i][j-1], table[i-1][j])
        else:
            new_val = table[i-1][j-w_i] + v_i
            if new_val > table[i][j-1]:
                table[i][j] = max(new_val, table[i][j-1], table[i-1][j])
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])

print(table[-1][-1])
