from graph import Graph

graph1 = Graph()

a = graph1.add_node("A")
b = graph1.add_node("B")
c = graph1.add_node("C")
d = graph1.add_node("D")
e = graph1.add_node("E")
f = graph1.add_node("F")

graph1.add_edge(a,b)
graph1.add_edge(a,c)
graph1.add_edge(c,b)
graph1.add_edge(d,b)
graph1.add_edge(d,c)

print(graph1)

print(graph1.isolatedVertices())