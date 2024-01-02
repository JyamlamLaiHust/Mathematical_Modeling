import numpy as np
import itertools
import random
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['simHei']


class Solution:
    def __init__(self, X, start_node):
        self.X = X  # 距离矩阵
        self.start_node = start_node  # 开始的节点
        self.array = [[0] * (2 ** (len(self.X) - 1)) for i in range(len(self.X))]  # 记录处于x节点，未经历个节点时，短阵储存x的下一步是M中哪个节点

    def transfer(self, sets):
        su = 0
        for s in sets:
            su = su + 2 ** (s - 1)  # 二进制转换
        return su

    def tsp(self):
        s = self.start_node
        num = len(self.X)
        cities = list(range(num))  # 形成节点的集合
        cities.pop(cities.index(s))  # 构建未经历节点的集合
        node = s  # 初始节点
        return self.solve(node, cities)  # 求解函数

    def solve(self, node, future_sets):
        if len(future_sets) == 0:  # 迭代终止条件，表示没有了未遍历节点，直接连接当前节点和起点即可
            return self.X[node][self.start_node]

        d = 99999
        distance = []  # node如果经过future_sets中节点，最后回到原点的距离

        for i in range(len(future_sets)):  # 遍历未经历的节点
            s_i = future_sets[i]
            copy = future_sets[:]
            copy.pop(i)  # 删除第i个节点，认为已经完成对其的访问
            distance.append(self.X[node][s_i] + self.solve(s_i, copy))  # 动态规划递推方程，利用递归

        d = min(distance)
        next_one = future_sets[distance.index(d)]  # node需要连接的下一个节点
        c = self.transfer(future_sets)  # 未遍历节点集合
        self.array[node][c] = next_one  # 回溯矩阵，(当前节点，未遍历节点集合)->下一个节点

        return d


def distance(vector1, vector2):
    d = 0
    for a, b in zip(vector1, vector2):
        d += (a - b) ** 2
    return d ** 0.5


# 随机生成10个坐标点
n = 10
random_list = list(itertools.product(range(1, n), range(1, n)))
cities = random.sample(random_list, n)

x = []
y = []
for city in cities:
    x.append(city[0])
    y.append(city[1])

fig = plt.figure()
plt.scatter(x, y, label='城市位置', s=30)
plt.xlabel('x')
plt.ylabel('y')
plt.title('TSP问题 随机初始城市')
plt.legend()
plt.show()

distance_matrix = np.zeros([n, n])
for i in range(n):
    for j in range(n):
        dist = distance(cities[i], cities[j])
        distance_matrix[i][j] = dist

s = Solution(distance_matrix, 0)
print("最短距离：" + str(s.tsp()))

M = s.array
lists = list(range(len(s.X)))
start = s.start_node

city_order = []
while len(lists) > 0:
    lists.pop(lists.index(start))
    m = s.transfer(lists)
    next_node = M[start][m]
    print(start, "--->", next_node)
    city_order.append(cities[start])
    start = next_node

x1 = []
y1 = []
for city in city_order:
    x1.append(city[0])
    y1.append(city[1])

x2 = []
y2 = []

plt.plot(x1, y1, label='路线', linewidth=2, marker='o', markersize=8)
plt.plot(x2, y2, label='路线', linewidth=2, color='r', marker='o', markersize=8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('TSP问题 路线图')
plt.legend()
plt.show()
