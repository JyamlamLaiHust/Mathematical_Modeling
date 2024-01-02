import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from([('s', 'v1', {'capacity': 8, 'weight': 20}),
                  ('v1', 'v3', {'capacity': 5, 'weight': 5}),
                  ('v1', 'v2', {'capacity': 9, 'weight': 2}),
                  ('v3', 'v4', {'capacity': 9, 'weight': 3}),
                  ('v3', 'v2', {'capacity': 2, 'weight': 1}),
                  ('v2', 't', {'capacity': 10, 'weight': 7}),
                  ('v4', 't', {'capacity': 5, 'weight': 6}),
                  ('v2', 'v4', {'capacity': 6, 'weight': 4})])

pos = nx.spring_layout(G)
pos['t'][0] = 1
pos['t'][1] = 0
pos['s'][0] = -1
pos['s'][1] = 0
pos['v1'][0] = -0.33
pos['v1'][1] = -1
pos['v3'][0] = -0.33
pos['v3'][1] = -1
pos['v2'][0] = 0.33
pos['v2'][1] = 1
pos['v4'][0] = 0.33
pos['v4'][1] = -1

edge_label1 = nx.get_edge_attributes(G, 'capacity')
edge_label2 = nx.get_edge_attributes(G, 'weight')
edge_label = {}
for i in edge_label1.keys():
    edge_label[i] = f'({edge_label1[i]}, {edge_label2[i]})'

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_label, font_size=15)

mincostFlow = nx.max_flow_min_cost(G, 's', 't')
mincost = nx.cost_of_flow(G, mincostFlow)
for i in mincostFlow.keys():
    for j in mincostFlow[i].keys():
        edge_label[(i, j)] += f', F={mincostFlow[i][j]}'

nx.draw_networkx_edge_labels(G, pos, edge_label, font_size=12)

print(mincostFlow)
print(mincost)

plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.show()
