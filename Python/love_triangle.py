
# n =  int(input())
# edge = list(map(int, input().split()))
# graph =  {}
# for i in range(1, n+1):
#     graph[i] = []
# for i in range(1, n+1):
#     src = i
#     dest = edge[i-1]
#     graph[src].append(dest)
# # print(graph)
# def iscycle(graph, src, traverse):
#     vis = [False for i in  range(len(graph)+1)]
#     queue = []
#     queue.append(src)
#     traverse.append(src)
#     vis[src] = True
#     while len(queue):
#         poppeditem = queue[0][0]
#         parent = queue[0][1]
        
#         for i in graph[poppeditem]:
#             if vis[i] ==  False:
#                 queue.append(i)
#                 # traverse.append(i)
#                 vis[i] = True
#             elif parent != i:
#                 return 1
#     # print(traverse)
#     return 0

# traverse = []
# if iscycle(graph, edge[0], traverse) == 0:
#     print("NO")
# else:
#     print("YES")

# --------------------------------------------------------------

n =  int(input())
edge = list(map(int, input().split()))
graph =  {}
for i in range(1, n+1):
    graph[i] = []
for i in range(1, n+1):
    src = i
    dest = edge[i-1]
    graph[src].append(dest)
# print(graph)

def isCycle(src, vis, adj):
    vis[src] = 1
    q = []
    q.append([src, -1])
    while len(q):
        node = q[0][0]
        par = q[0][1]
        q.pop(0)
        
        for adjnode in adj[node]:
            if not(vis[adjnode]):
                vis[adjnode] = 1
                q.append([adjnode, node])
            elif par != adjnode:
                return True
    return False

vis = [0 for i in range(len(graph)+1)]
if isCycle(edge[0], vis, graph):
    print("YES")
else:
    print("NO")
    
10
4 10 9 5 3 1 5 10 6 4