# initialize Graph Class for DFS
from collections import deque


class Node:
    def __init__(self, node, value):
        self.node = node
        self.value = value
        self.edges = []

    def addedge(self, destination):
        return self.edges.append(destination)

    def removeedge(self, node):
        return self.edges.remove(node)

    def __str__(self):
        return f"{self.node}"


def DFS(n, visited):
    print(n)
    visited.append(n)


    for node in n.edges:
        if node not in visited:
            DFS(node, visited)






def DFS_Loop(graph):
    visited = []


    for node in graph:
        if node not in visited:
            DFS(node, visited)
            print("this is visited:", [node.node for node in visited])




def topsort(graph):
    order = deque()
    indegree = {}
    for e in graph:
        indegree[e] = 0
    visited = set()

    for node in graph:      #O(V)
        if node not in visited:
            top_sort_util(node, order, indegree, visited) #O(E)
    return order, indegree

def top_sort_util(n, order, indegree, visited):

    visited.add(n)

    for neighbors in n.edges: #O(E)
        indegree[neighbors] += 1
        if neighbors not in visited:
            top_sort_util(neighbors, order, indegree, visited)

    order.appendleft(n)

def computevalue(order, indegree):
    a=0
    while a < len(order):              # O(V +E)
        for neighbor in order[a].edges:
            neighbor.value += order[a].value
        a+=1

def topoSortBfs(g) :
    indegree = {}
    for e in g:
        indegree[e] = 0             # run time of O(V)
    for node in g:
        for neighbor in node.edges:        # run time of O(V + E)
            indegree[neighbor] += 1  #count the target nodes number
    queue = []
    for e in g:
        if indegree.get(e) == 0: # a source nodes that has no tagert node
            queue.append(e)
    res = []
    while queue:                       #run time O( V + E)
        u = queue.pop()
        res.append(u)
        for neighbor in u.edges:
            indegree[neighbor] -= 1  #decrease indegree by 1
            neighbor.value += u.value
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(res) == len(g):  #complete all nodes... extra nodes == cycle present

        return res
    return None


#create nodes

a = Node('a', 3)
b = Node('b', 0)
c = Node('c', 0)
d = Node('d', 0)
e = Node('e', 0)
f = Node('f', 10)
g = Node('g', 0)
h = Node('h', 0)

#create graph a->b, a->c, c->d, b->

a.addedge(b)
a.addedge(d)
b.addedge(c)
d.addedge(c)

f.addedge(e)
f.addedge(g)
e.addedge(h)
e.addedge(g)
g.addedge(h)



G = [b,a,d,c,f,e,g,h]

for node in G:
    edgelist= []
    for edge in node.edges:
        edgelist.append(f"{edge}")
    print(f"{node} ->: {edgelist} ")

# DFS_Loop(G)
#
# order, indegree = topsort(G)
# print([e.node for e in order])
# computevalue(order, indegree)
#
# for e in G:
#     print((e.node, e.value))

result = topoSortBfs(G)
print([e.node for e in result])
print([e.value for e in result])

