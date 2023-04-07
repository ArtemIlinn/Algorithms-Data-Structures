"""
Given an undirected graph of N vertices and M edges. We need to check if the graph is a tree.
A tree is a connected graph without cycles.
Input Format

The first line of the input file contains two integers N and M (1 ≤ N ≤ 100, 1 ≤ M ≤ 1000) separated by a space.
This is followed by M different lines with descriptions of edges, each of which contains two natural numbers Ai and Bi
 (1 ≤ Ai ≤ Bi ≤ N), where Ai and Bi are the numbers of vertices connected by the i-th edge.
Output Format

In the output file print the word "YES" if the graph is a tree, or "NO" otherwise.

Input:
3 2
1 2
1 3
Output
YES

Input
4 3
1 2
1 3
2 3
Output
NO
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
