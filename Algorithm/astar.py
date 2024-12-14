import math
txt=open('grid.txt', 'r')
lines=txt.readlines()
grid=[]
for line in lines:
    row=line.strip().split()
    grid.append([int(x) for x in row])

start=(0,0)
goal=(19,19)

def h(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

open_list=[start]
closed_list=[]

g={start:0}
f={start:h(start,goal)}

directions=[(0,1),(0,-1),(-1,0),(1,0)]

while open_list:
    cell=min(open_list, key=lambda x:f[x])
    if cell==goal:
        print('success!')
        break
    open_list.remove(cell)
    closed_list.append(cell)

    for dircetion in directions:
        neighbor=(cell[0]+dircetion[0],cell[1]+dircetion[1])
        if 0<=neighbor[0]<len(grid) and 0<=neighbor[1]<len(grid[0]) and grid[neighbor[0]][neighbor[1]] != 5:
            if neighbor not in closed_list:
                h_cost=h(neighbor,goal)
                g_cost=g[cell]+1
                f_cost=g_cost+h_cost
                if neighbor not in open_list:
                    open_list.append(neighbor)
                    g[neighbor]=g_cost
                    f[neighbor]=f_cost
                elif f_cost<f[neighbor]:
                    g[neighbor]=g_cost
                    f[neighbor]=f_cost
print(f'it cost: {f[goal]}')


