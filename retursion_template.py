#!/usr/bin/env python

def recursion(level, param1, param2, ...)
    # recursion terminator
    if level > MAX_LEVEL
        print_result
        return
    
    # process logic in current level
    process_data(level, data...)

    # drill down
    # may one 
    # two lines => DFS, feibonaqie recursion solution
    self.recursion(level + 1, p1, ...)

    # reverse the current level status if needed
    reverse_state(level)

#e.g. fibonaqi
# common ancestor node

#DFS recursion solution
visited = set()
def dfs(node, visited):
    visited.add(node)

    # process current node here.
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
