from graph import Graph

graph1 = Graph()

a = graph1.add_node("A")
b = graph1.add_node("B")
c = graph1.add_node("C")
d = graph1.add_node("D")

graph1.add_edge(a,b)
graph1.add_edge(a,c)
graph1.add_edge(c,b)
graph1.add_edge(d,b)
graph1.add_edge(d,c)

print(graph1)