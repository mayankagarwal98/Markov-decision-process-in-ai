import copy
from math import ceil, floor


def float_round(num, places=0, direction=floor):
    return direction(num * (10**places)) / float(10**places)


def print_value(ANS):
    for i in range(0, n):
        for j in range(0, m):
            ANS[i][j] = float_round(ANS[i][j], 3, round)
            print(ANS[i][j]),
        print("")
    policy = [[0] * m for _ in range(0, n)]
    for i in range(0, n):
        for j in range(0, m):
            highest = -100000000000000000
            if(wall[i][j] == 1):
                policy[i][j] = "W"
                continue
            if(endstates[i][j] == 1):
                if a[i][j] > 0:
                    policy[i][j] = "G"
                else:
                    policy[i][j] = "E"
                continue
            if(i != 0):
                if(wall[i - 1][j] == 0):
                    if(highest <= ANS[i - 1][j]):
                        highest = ANS[i - 1][j]
                        policy[i][j] = "^"
            if(i != n - 1):
                if(wall[i + 1][j] == 0):
                    if(highest <= ANS[i + 1][j]):
                        highest = ANS[i + 1][j]
                        policy[i][j] = "v"
            if(j != 0):
                if(wall[i][j - 1] == 0):
                    if(highest <= ANS[i][j - 1]):
                        highest = ANS[i][j - 1]
                        policy[i][j] = "<"
            if(j != m - 1):
                if(wall[i][j + 1] == 0):
                    if(highest <= ANS[i][j + 1]):
                        highest = ANS[i][j + 1]
                        policy[i][j] = ">"
    for i in range(0, n):
        for j in range(0, m):
            print(policy[i][j]),
        print("")


def VALUE_ITERATION(n, m, matrix, endstates, wall, step_reward):
    iteration_count = 0
    discount_factor = 0.99
    U = copy.deepcopy(matrix)
    U1 = copy.deepcopy(matrix)
    while 1:
        U = copy.deepcopy(U1)
        delta = 0.0
        for i in range(0, n):
            for j in range(0, m):
                if(wall[i][j] or endstates[i][j]):
                    continue
                up = 0
                down = 0
                left = 0
                right = 0
                if i == 0:
                    left += 0.1 * U1[i][j]
                    right += 0.1 * U1[i][j]
                    up += 0.8 * U1[i][j]
                else:
                    if(wall[i - 1][j]):
                        left += 0.1 * U1[i][j]
                        right += 0.1 * U1[i][j]
                        up += 0.8 * U1[i][j]
                    else:
                        left += 0.1 * U1[i - 1][j]
                        right += 0.1 * U1[i - 1][j]
                        up += 0.8 * U1[i - 1][j]
                if i == n - 1:
                    right += 0.1 * U1[i][j]
                    left += 0.1 * U1[i][j]
                    down += 0.8 * U1[i][j]
                else:
                    if(wall[i + 1][j]):
                        right += 0.1 * U1[i][j]
                        left += 0.1 * U1[i][j]
                        down += 0.8 * U1[i][j]
                    else:
                        right += 0.1 * U1[i + 1][j]
                        left += 0.1 * U1[i + 1][j]
                        down += 0.8 * U1[i + 1][j]
                if j == 0:
                    left += 0.8 * U1[i][j]
                    up += 0.1 * U1[i][j]
                    down += 0.1 * U1[i][j]
                else:
                    if(wall[i][j - 1]):
                        left += 0.8 * U1[i][j]
                        up += 0.1 * U1[i][j]
                        down += 0.1 * U1[i][j]
                    else:
                        left += 0.8 * U1[i][j - 1]
                        up += 0.1 * U1[i][j - 1]
                        down += 0.1 * U1[i][j - 1]
                if j == m - 1:
                    right += 0.8 * U1[i][j]
                    up += 0.1 * U1[i][j]
                    down += 0.1 * U1[i][j]
                else:
                    if(wall[i][j + 1]):
                        right += 0.8 * U1[i][j]
                        up += 0.1 * U1[i][j]
                        down += 0.1 * U1[i][j]
                    else:
                        right += 0.8 * U1[i][j + 1]
                        up += 0.1 * U1[i][j + 1]
                        down += 0.1 * U1[i][j + 1]
                U1[i][j] = step_reward + discount_factor * \
                    max(up, left, right, down)
                if(U1[i][j] == 0):
                    continue
                if(abs((U1[i][j] - U[i][j]) / U1[i][j]) > delta):
                    delta = abs((U1[i][j] - U[i][j]) / U1[i][j])
        # print(U)
        iteration_count += 1
        print("Iteration Number->>", iteration_count)
        print("Trace>>")
        print_value(U)
        if delta < 0.01:
            break
    return U


n, m = [int(x) for x in raw_input().split()]

a = [[0] * m for _ in range(0, n)]
for i in range(n):
    a[i] = [float(j) for j in raw_input().strip().split(" ")]
# print(a[0][0])


e, w = [int(x) for x in raw_input().split()]
endstates = []
# initialize the number of rows
for i in range(0, n):
    endstates += [0]
# initialize the matrix
for i in range(0, n):
    endstates[i] = [0] * m
for i in range(0, e):
    a1, b1 = [int(x) for x in raw_input().split()]
    endstates[a1][b1] = 1

wall = []
# initialize the number of rows
for i in range(0, n):
    wall += [0]
# initialize the matrix
for i in range(0, n):
    wall[i] = [0] * m
for i in range(0, w):
    a1, b1 = [int(x) for x in raw_input().split()]
    wall[a1][b1] = 1


initial_x1, initial_y1 = [int(x) for x in raw_input().split()]

step_reward = float(input())

ANS = VALUE_ITERATION(n, m, a, endstates, wall, step_reward)
# print_value(ANS)
