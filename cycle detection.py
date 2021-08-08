"""
https://www.youtube.com/watch?v=AfSk24UTFS8
MIT OpenCourseWare, 14. DFS, Topological Sort, by Prof Erik Demaine
https://www.algotree.org/algorithms/tree_graph_traversal/depth_first_search/cycle_detection_in_directed_graphs/

Cycle Detection
A Graph has a cycle <--> DFS has a backward edge
"""
from collections import defaultdict

class Graph:
    def __init__(self, nodes):      #nodes:list of all nodes in the graph
        self.adjlist = defaultdict(list)
        self.n = len(nodes)
        self.visited = {node: False for node in nodes}
        self.inpath = {node: False for node in nodes}   #inpath stores the visited nodes in the traversal path, for finding cycle in a directed graph
        self._cycle_present = False

    def add_edge(self, src, dst, bidirectional=False):
        self.adjlist[src].append(dst)
        if bidirectional:
            self.adjlist[dst].append(src)

    def dfs_detect_cycle(self, src):
        self.visited[src] = True
        self.inpath[src] = True     #mark for the vertex visited in traversal path

        for v in self.adjlist[src]:
            if self.inpath[v] == True:
                self._cycle_present = True
                print("Cycle present in the graph, found backward edge: {} --> {}".format(src, v))
                self.inpath[src] = False
                return
            elif self.visited[v] == False:
                self.dfs_detect_cycle(v)

        self.inpath[src] = False    #unmark the vertex while backtracking, as it may be in the next traversal path

    def cycle_present(self):
        return self._cycle_present


nodes = [0, 1, 2, 3, 4, 5, 6]
g1 = Graph(nodes)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 4)
g1.add_edge(2, 3)
g1.add_edge(3, 1)
g1.add_edge(3, 5)
g1.add_edge(4, 6)
g1.add_edge(5, 4)
g1.add_edge(6, 5)

g1.dfs_detect_cycle(0)
if g1.cycle_present() == True:
    print("Cycle found in g1")
else:
    print("Cycle not found in g1")

nodes2 = [0, 1, 2, 3, 4]
g2 = Graph(nodes2)
g2.add_edge(0, 1)
g2.add_edge(0, 2)
g2.add_edge(2, 3)
g2.add_edge(3, 4)
g2.add_edge(4, 1)

g2.dfs_detect_cycle(0)
if g2.cycle_present() == True:
    print("Cycle found in g2")
else:
    print("Cycle not found in g2")

nodes3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
g3 = Graph(nodes3)
g3.add_edge('A', 'B')
g3.add_edge('A', 'H')
g3.add_edge('G', 'H')
g3.add_edge('B', 'C')
g3.add_edge('D', 'B')
g3.add_edge('D', 'E')
g3.add_edge('E', 'F')
g3.add_edge('C', 'F')
g3.dfs_detect_cycle('A')
if g3.cycle_present() == True:
    print("Cycle found in g3")
else:
    print("Cycle not found in g3")
"""
Output:
Cycle present in the graph, found backward edge: 5 --> 4
Cycle found in g1
Cycle not found in g2
Cycle not found in g3

Image of the Graphs: https://www.algotree.org/images/DFS_Cycle_In_Directed_Graph.svg
"""