cities=['A', 'B', 'C', 'D']

distance=[
    [0,3,7,10],
    [3,0,6,4],
    [7,6,0,3],
    [10,4,3,0]
]

def cost(path):
    total=0
    for i in range(4):
        a=cities.index(path[i])
        b=cities.index(path[(i+1)%4])
        total+=distance[a][b]

    return total

def beam_search():
    beam=[cities]

    for step in range(5):
        paths=[]
        for path in beam:
            for i in range(1,4):
                for j in range(i+1,4):
                    new=path.copy()
                    new[i],new[j]=new[j],new[i]
                    paths.append(new)

        paths.sort(key=cost)
        beam=paths[:2]

    return beam[0]

best=beam_search()
print("best path:" ,best)
print("cost:" ,cost(best))
