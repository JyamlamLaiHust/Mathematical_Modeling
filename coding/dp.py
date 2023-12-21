# 动态规划例题
def dynamic_p() -> list:
    items = [   # 物品项
        {"name": "水", "weight": 3, "value": 10},
        {"name": "书", "weight": 1, "value": 3},
        {"name": "食物", "weight": 2, "value": 9},
        {"name": "小刀", "weight": 3, "value": 4},
        {"name": "衣物", "weight": 2, "value": 5},
        {"name": "手机", "weight": 1, "value": 10}
   ]

    max_capacity = 6    # 约束条件为 背包最大承重为6
    dp = [[0]*(max_capacity + 1) for _ in range(len(items) + 1)]

    # row 代表行
    for row in range(1, len(items) + 1):    # col 代表列
        for col in range(1, max_capacity + 1):
            weight = items[row - 1]["weight"]   # 获取当前物品重量
            value = items[row - 1]["value"]     # 获取当前物品价值
            if weight > col:    # 判断物品重量是否大于当前背包容量大于直接取上一次最优结果 此时row-1代表上一行
                dp[row][col] = dp[row - 1][col]
            else:
                # 使用内置函数max()，将上一次最优结果 与 当前物品价值+剩余空间可利用价值 做对比取最大值
                dp[row][col] = max(value + dp[row - 1][col - weight], dp[row - 1][col])
    return dp


dp = dynamic_p()
for i in dp:
    print(i)

print(dp[-1][-1])
