import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import arange


def fvdp(t, y):
    '''
    要把y看出一个向量，y = [dyo,dy1,dy2,...]分别表示y的n阶导，那么
    y[o]就是需要求解的函数，y[1]表示一阶导，y[2]表示二阶导，以此类推
    '''
    dy1 = y[1] # y[1]=dy/dt，一阶导
    dy2 = 1000 * (1-y[0]**2) * y[1] - y[0]
    # y[0]是最初始，也就是需要求解的函数
    # 注意返回的顺序是[一阶导， 二阶导]，这就形成了一阶微分方程组
    return [dy1, dy2]


def solve_second_order_ode():
    '''
    求解二阶ODE
    '''

    x = arange(0,0.25,0.01)  # 给x规定范围
    y0 = [0.0, 2.0]  # 初值条件
    # 初值[3.0，-5.01表示y(o)=3,y'()=-5
    # 返回y，其中y[:,@]是y[e]的值，就是最终解，y[:,1]是y’(x)的值
    y = odeint(fvdp, y0, x, tfirst=True)
    y1, = plt.plot(x, y[:, 0], label='y')
    y1_1, = plt.plot(x, y[:, 1], label='y\'')
    plt.legend(handles=[y1, y1_1])  # 创建图例

    plt.show()


solve_second_order_ode()
