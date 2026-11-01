


from importlib.resources import path


def Bfs(start,goal):
    queue=[(start,[start])]
    visited=[]
    
    while queue:
        state , path = queue.pop(0)
        
        if state==goal:
            return path
        
        if state in visited:
            continue
        
        visited.append(state)
        
        for i in range(len(state)):
            new=list(state)
            block=new.pop(i)
            for j in range(len(new)):
                next_state=new.copy()
                next_state.insert(j, block)
                next_state=tuple(next_state)
                
                if next_state not in visited:
                    queue.append((next_state,path+[next_state]))
    return None               
    
    
    
start=('A','B','C')
goal=('C','B','A')

result= Bfs(start,goal)
if result:
    print("step to reach goal")
    for step in result:
        print(step)
else:
    print("no solution found")