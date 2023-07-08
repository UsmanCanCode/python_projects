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



def BFS_Loop(Graph):

    queue = deque()

    visited = []


    def BFS(node, queue, visited):

        visited.append(node)


        while queue:
            newnode = queue.popleft()
            for neighbor in newnode.edges:
                if neighbor not in visited:
                    print(f"neighbor of {newnode.node} being visited: {neighbor.node}")
                    queue.append(neighbor)
                    BFS(neighbor, queue, visited)



    for node in Graph:
        if node not in visited:
            print(f"node being visited: {node.node}")
            queue.append(node)
            BFS(node, queue, visited)



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





G = [c,a,g,f,d,e,b]


BFS_Loop(G)