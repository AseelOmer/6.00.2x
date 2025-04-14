from graph_classes import Node, Edge, Digraph

def build_graph():
    g = Digraph()
    nodes = {}

    for name in ['A', 'B', 'C', 'D']:
        node = Node(name)
        g.add_node(node)
        nodes[name] = node

    g.add_edge(Edge(nodes['A'], nodes['B']))
    g.add_edge(Edge(nodes['A'], nodes['C']))
    g.add_edge(Edge(nodes['B'], nodes['C']))
    g.add_edge(Edge(nodes['C'], nodes['D']))

    return g, nodes

g, nodes = build_graph()

print("Graph:")
print(g)

print("\nBFS Result:")
for node in g.bfs(nodes['A']):
    print(node)

print("\nDFS Result:")
for node in g.dfs(nodes['A']):
    print(node)
