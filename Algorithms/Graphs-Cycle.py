from collections import deque

#node class to create nodes in a graph
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

#DFS function to visit edges of a node
def DFS(n, visited):
    print(n)
    visited.append(n)

    for node in n.edges:
        if node not in visited:
            DFS(node, visited)
#dfs-loop to visit all nodes
def DFS_Loop(graph):
    visited = []
    for node in graph:
        if node not in visited:
            DFS(node, visited)
            print("this is visited:", [node.node for node in visited])


def findCycleLoop(G):
    visited = []
    currStack = []
    cycleplusadj = set()

    for node in G:
        if node not in visited:
            findCycle(node, visited, currStack, cycleplusadj)

    return cycleplusadj

def findCycle(n, visited, currStack, cycleplusadj):

    visited.append(n)
    currStack.append(n)

    for neighbor in n.edges:

        if neighbor in currStack and neighbor in visited:
            for e in currStack:
                cycleplusadj.add(e)
        elif neighbor in cycleplusadj:
            for e in currStack:
                cycleplusadj.add(e)
        else:
            findCycle(neighbor, visited, currStack, cycleplusadj)
    currStack.remove(n)




#create nodes
a = Node('a', 0)
b = Node('b', 0)
c = Node('c', 0)
d = Node('d', 0)
e = Node('e', 0)
f = Node('f', 0)
g = Node('g', 0)
h = Node('h', 0)

#create graph and edge
d.addedge(c)
a.addedge(b)
c.addedge(a)
c.addedge(e)
e.addedge(f)
f.addedge(g)
g.addedge(e)





G = [e,g,f,d,c]


cycles = findCycleLoop(G)

print([node.node for node in cycles])