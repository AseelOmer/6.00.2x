# graph_classes.py
from collections import deque

class Node(object):
    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Node('{self.name}')"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return f"{self.src}->{self.dest}"

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        super().__init__(src, dest)
        self.weight = float(weight)

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"{self.src}->{self.dest} ({self.weight})"

class Digraph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = {}  # Node -> list of destination Nodes

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate node")
        self.nodes.add(node)
        self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def get_children(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += f"{src}->{dest}\n"
        return result.strip()

    def bfs(self, start_node):
        if start_node not in self.nodes:
            raise ValueError("Start node not in graph")

        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        bfs_result = []

        while queue:
            current_node = queue.popleft()
            bfs_result.append(current_node)
            for neighbor in self.get_children(current_node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return bfs_result

    def dfs(self, start_node):
        if start_node not in self.nodes:
            raise ValueError("Start node not in graph")

        visited = set()
        dfs_result = []

        def dfs_helper(node):
            visited.add(node)
            dfs_result.append(node)
            for neighbor in self.get_children(node):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start_node)
        return dfs_result
