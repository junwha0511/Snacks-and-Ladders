import random

N = int(input('How many of you are there?: '))
M = 14

ladder = [[0]+[1, 0]*N for i in range(M)] #01010101 ... 10 
pick = [False]*N 
result = [0]*(2*N+1)

for i in range(2, 2*N, 2): #except columns of both sides
    for j in range(1, M-1):
        if ladder[j][i-2]!=1 and ladder[j][i+2]!=1 and ladder[j-1][i]!=1:
            ladder[j][i] = random.randint(0, 1) 

i = 1
while False in pick:
    select = int(input(str(i) + 'th select ladder number: '))
    pick[select-1] = True

    col = select*2-1 #select the column with 1

    for j in range(M):
        if (col-1) > 0 and ladder[j][col-1] == 1:
            col -= 2
        elif (col+1) < 2*N and ladder[j][col+1] == 1:
            col += 2

    result[col] = i
    i += 1

for i in range(M):
    for j in range(2*N+1):
        print('■' if ladder[i][j] else '□', end=' ')
    print()

for i in range(2*N+1):
    print(result[i] if result[i]!=0 else ' ', end=' ')
print()

input()