# TOPSIS分析法

import numpy as np
import pandas as pd


def entropyWeight(data):
    data = np.array(data)
    # 归一化
    P = data / data.sum(axis=0)
    # 计算值
    E = np.nansum(-P * np.log(P) / np.log(len(data)), axis=0)
    # 计算权系数
    return (1 - E) / (1 - E).sum()

newdata = newdata.replace('A', 1)
newdata = newdata.replace('B', 2)
newdata = newdata.replace("c", 3)

newdata=newdata.loc[:,"供货均值":"消耗量"]
entropyWeight(newdata)


def topsis(data, weight=None):
    # 归一化
    data = data / np.sqrt((data ** 2).sum())
    # 最优最劣方案
    Z = pd.DataFrame([data.min(), data.max()], index=['负理想解', '正理想解'])
    # 距离
    weight = entropyWeight(data) if weight is None else np.array(weight)
    Result = data.copy()
    Result['正理想解'] = np.sqrt(((data - Z.loc['正理想解'])** 2 * weight).sum(axis=1))
    Result['负理想解'] = np.sqrt(((data - Z.loc['负理想解'])** 2 * weight).sum(axis=1))
    # 综合得分指数
    Result['综合得分指数'] = Result['负理想解'] / (Result['负理想解'] + Result['正理想解'])
    Result['排序'] = Result.rank(ascending=False)['综合得分指数']
    return Result, Z, weight
