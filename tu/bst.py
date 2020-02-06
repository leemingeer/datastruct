#!/usr/bin/env python
#describe a 'tu', the intrinsic relationship of 'tu' is data
#https://www.bilibili.com/video/av25763384/?spm_id_from=trigger_reload
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

#breadth first search
def BFS(graph, s):
    # duilie realized by list
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)

    while len(queue) > 0:
        vertex = queue.pop(0) #BFS FIFO
        print(vertex)
        nodes = graph[vertex]
        for n in nodes:
            if n not in seen:
                queue.append(n)
                seen.add(n)     
BFS(graph, "E")
print('*')*20

def DFS(graph, s):
    # zhan realized by list
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)

    while len(stack) > 0:
        #with only difference with BFS
        vertex = stack.pop() #DFS, LIFO
        print(vertex)
        nodes = graph[vertex]
        for n in nodes:
            if n not in seen:
                stack.append(n)
                seen.add(n)
DFS(graph, "E")
print('*')*20

#BFS application
#feng ceng
def BFS_short_path(graph, s):
    # duilie realized by list
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)

    parent = {
        s: None
    }

    while len(queue) > 0:
        vertex = queue.pop(0) #BFS FIFO
        print(vertex)
        nodes = graph[vertex]
        for n in nodes:
            if n not in seen:
                queue.append(n)
                seen.add(n)
                parent[n] = vertex
    return parent
    
parent = BFS_short_path(graph, "E")
#for k in parent:
#    print(k, parent[k])

#walk from B to E
v = 'B'
while v is not None:
    print(v)
    v = parent[v]