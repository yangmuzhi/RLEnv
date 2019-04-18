"""
Beer game 啤酒游戏
四个agent
action: 每周向上游订单数量
player: F:制造商；D：经销商; W：批发商；R：零售商
demand: 是一个 generator
"""
import numpy as np

class BeerGameEnv:

    def __init__(self, demand):
        self.delay_time = {}
        self.delay_time['slove order'] = 1
        self.delay_time['trans'] = 2
        self.demand_gen = demand


    def _init_chain(self):
        """初始化库存"""
        self.stock = np.zeros(4)
        self.order = np.zeros(4)
        self.trans = [np.zeros(4) for _ in range(self.delay_time['trans'])] # several weeks delay
        self.cost = np.zeros(4)
        self.cost_his = []
        self.week = 0

    def _deal_after_each_week(self):
        """每周结算, 返回 state，r, d"""
        self.cost_his.append(self.cost)
        return self.cost

    def _check_stock_and_trans(self, a):
        trans = np.zeros(4)
        trans[0] = a
        for i in range(4):
            # 库存足够，全部发出,接受库存惩罚
            if self.stock[i] >= self.order[i]:
                if i is not 0:
                    trans[i] = self.stock[i]
                self.stock[i] -= self.order[i]
                assert self.stock[i] >= 0
                self.cost[i] = - self.stock[i]

            else: # 库存不够,把库存全发出，然后接受惩罚
                if i is not 0:
                    trans[i] = self.stock[i]
                self.stock[i] = 0
                assert (self.stock[i] - self.order[i]) < 0
                self.cost[i] = 2 * (self.stock[i] - self.order[i])
            self.trans.append(trans)

    def reset(self):
        self._init_chain()

    def step(self, action):
        """同时决策、结算"""
        demand = next(self.demand_gen)
        self.order[-1] = demand
        self.order[:-1] = action[1:]

        self.stock += self.trans[0]
        self.trans.pop(-1)

        self._check_stock_and_trans(action[0])
        self.week += 1
        return self._deal_after_each_week()
