"""
An undirected unweighted graph is given. It is necessary to count the number of its connected components and output them.

Input Format
The input file contains two numbers N and M (0 < N <= 100000, 0 <= M <= 100000). The next M lines contain two numbers
i and j each (1 <= i, j <= N), which mean that vertices i and j are connected by an edge.

Output Format
In the first line of the output file print the number of connected components.
Next print N integers, i-th of them specifies the number of the connected component for i-th vertex.
The components should be numbered with consecutive integers starting from 1.
The numbering order of the components is arbitrary.

Input
4 2
1 2
3 4
Output
2
1 1 2 2
"""


class Graph:
    def __init__(self, vertex_number, edge_number=0):
        self.vertex_number = vertex_number
        self.edge_number = edge_number
        self.adj = [[] for i in range(vertex_number)]

    def dfs(self, vertex, visited, parent_vertex):
        visited[vertex] = True      # just bounced here
        for i in self.adj[vertex]:  # go for all connected Vs
            if not visited[i]:      # if not visited do the same
                self.dfs(i, visited, vertex)

    def draw_edge(self, i, j):
        self.edge_number += 1
        self.adj[i].append(j)
        self.adj[j].append(i)

    def is_path(self):
        visited = [False] * self.vertex_number  # been nowhere so far
        self.dfs(0, visited, -1)  # mark all accessible vertices

        for vertex in range(self.vertex_number):
            if not visited[vertex]:
                return False
        return True

    def is_tree(self):
        return self.is_path() and self.edge_number == self.vertex_number - 1


params = list(map(int, input().split()))
model = Graph(params[0])

for i in range(int(params[1])):
    params = list(map(int, input().split()))
    model.draw_edge(params[0] - 1, params[1] - 1)

if model.is_tree():
    print('YES')
else:
    print('NO')
