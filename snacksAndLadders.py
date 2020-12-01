import random, time 
from os import system, name
while True: 
    try:
        from colorclass import Color
        from colorclass import disable_all_colors, enable_all_colors, is_enabled
        from colorclass import set_dark_background, set_light_background
        from colorclass import Windows
    except:
        system('pip install colorclass')
    try:
        import cursor
        break
    except:
        system('pip install cursor')


N = int(input('How many of you are there?: '))
M = 14
SPEED = 0.1
clear = None

if  name == 'nt':
    cursor.hide()
    clear = lambda: system('cls')    
    Windows.enable(auto_colors=True, reset_atexit=True)
else:
    clear = lambda: system('clear')
    system('setterm -cursor off')

def printMatrix(matrix):
    clear()
    for i in range(M):
        for j in range(2*N+1):
            print(matrix[i][j], end=' ')
        print()
    time.sleep(SPEED)

def getColor(index, str):
    colors = ['{red}', '{green}', '{yellow}', '{blue}', '{magenta}', '{cyan}']
    return Color(colors[index%6]+str)

ladder = [[0]+[1, 0]*N for i in range(M)] #01010101 ... 10 
matrix = [[Color('{white}□')]*(2*N+1) for i in range(M)] #01010101 ... 10 
pick = [0]*N 
result = [0]*(2*N+1)

for i in range(2, 2*N, 2): #except columns of both sides
    for j in range(1, M-1):
        if ladder[j][i-2]!=1 and ladder[j][i+2]!=1 and ladder[j-1][i]!=1:
            ladder[j][i] = random.randint(0, 1) 

i = 0
while 0 in pick:
    select = int(input(str(i+1) + 'th select ladder number: '))
    pick[i] = select
    i += 1

for i, select in enumerate(pick):
    col = select*2-1 #select the column with 1

    for j in range(M):
        matrix[j][col] = getColor(i, '■')
        printMatrix(matrix)
        if (col-1) > 0 and ladder[j][col-1] == 1:
            matrix[j][col-1] = getColor(i, '■') 
            printMatrix(matrix)
            matrix[j][col-2] = getColor(i, '■')
            col -= 2
        elif (col+1) < 2*N and ladder[j][col+1] == 1:
            matrix[j][col+1] = getColor(i, '■')
            printMatrix(matrix)
            matrix[j][col+2] = getColor(i, '■')
            col += 2
        printMatrix(matrix)    
    result[col] = i+1

print(Color('{white}'), end='')

for i in range(2*N+1):
    print(result[i] if result[i]!=0 else ' ', end=' ')
print()

input()