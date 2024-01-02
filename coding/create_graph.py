import networkx as nx
import matplotlib.pyplot as plt
# 创建空的网格
nf=nx.Graph()

# 添加节点
nf.add_node('JFK')
nf.add_nodes_from(['SFO', 'LAX', 'ATL', 'FLO', 'DFW', 'HNL'])
# nf.number_of_nodes() # 查看节点数，输出结果7

# 添加连线
nf.add_edges_from([('JFK', 'SFO'), ('JFK', 'LAX'), ('LAX','ATL'), ('FLO','ATL'),('ATL', 'JFK'), ('FLO','JFK'), ('DFW', 'HNL')])
nf.add_edges_from([('OKC', 'DFW'), ('OGG', 'DFW'), ('OGG', 'LAX')])
print(nf.number_of_edges()) # 查看连线数，结果输出10

# 绘制网络图
nx.draw(nf ,with_labels=True)
plt.show()

print(nx.info(nf))  # 打印图的基本信息，包括节点数量和边数
print(nx.density(nf))  # 实际边数与可能边数之比
print(nx.diameter(nf))  # 最长最短路径的长度
print(nx.clustering(nf))  # 该节点的邻居节点之间存在连接的概率
print(nx.transitivity(nf))  # 存在三角形连接的概率
print(list(nf.neighbors('OGG')))  # 获取节点 'OGG' 的所有邻居节点
print(nx.degree_centrality(nf))  # 节点的度（与其相连的边的数量）与图中所有节点的度的比值
print(nx.closeness_centrality(nf))  # 节点到其他节点的平均最短路径长度的倒数
print(nx.betweenness_centrality(nf))  # 该节点的最短路径在所有最短路径中的占比
