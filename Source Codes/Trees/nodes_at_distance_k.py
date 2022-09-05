from bst_hardcoded import *
from collections import defaultdict


def fun(root, parent, graph):
    if root:
        if parent:
            graph[root.data].append(parent.data)
        
        if root.left:
            graph[root.data].append(root.left.data)
            
        if root.right:
            graph[root.data].append(root.right.data)
            
        fun(root.left, root, graph)
        fun(root.right, root, graph)
  
  
def dfs(graph, t, visited, k, ans):
    
    if k == 0:
        ans.append(t)
        return
        
    for i in graph[t]:
        if visited[i]:
            continue

        visited[i] = True
        dfs(graph, i, visited, k-1, ans)
        visited[i] = False
        


graph = defaultdict(list)
fun(bst3, None, graph)
print(graph)

t = 5
k = 2

visited = {}
for i in graph:
    visited[i] = False
    
visited[t] = True

ans = []

dfs(graph, t, visited, k, ans)

print(ans)
