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

def get_source(vertex, source):
    while vertex != source[vertex][0]:
        vertex = source[vertex][0]
    return vertex, source[vertex][1]


def get_sources(graph):

    giga_source = {}

    for vertex in graph.keys():
        giga_source[vertex] = (vertex, 0)

    for i in graph:
        for j in graph[i]:
            (source_i, deep_i), (source_j, deep_j) = get_source(i, giga_source), get_source(j, giga_source)

            if source_i != source_j:
                current_min, current_max = source_i, source_j

                if deep_i > deep_j:
                    current_min, current_max = source_j, source_i

                giga_source[current_max] = (current_max, max(giga_source[current_min][1]+1, giga_source[current_max][1]))
                giga_source[current_min] = (giga_source[current_max][0], -1)

    ans = {}
    for i in graph:
        if giga_source[i][0] == i:
            ans[i] = []
    for i in graph:
        ans[get_source(i, giga_source)[0]].append(i)
    return ans


def draw_edge(graph, i, j):
    graph[i].append(j)
    graph[j].append(i)


def components(graph):
    components = list(get_sources(graph).values())
    components_number = len(components)
    print(components_number )

    list_to_print = [0]*vertex_number

    for c in range(components_number):
        for i in components[c]:
            list_to_print[i-1] = c+1

    print(*list_to_print)


params = list(map(int, input().split()))
vertex_number = params[0]

graph = {}
for i in range(vertex_number):
    graph[i + 1] = []

for i in range(int(params[1])):
    ps = list(map(int, input().split()))
    draw_edge(graph, ps[0], ps[1])

components(graph)