from Beer_game.beer_game_env import BeerGameEnv
from dqn.deepqn import DQN
from utils.net import simple_net
import numpy as np



eps = 10
batch_size = 32

def demand():
    while True:
        yield np.random.uniform(10)
demand_gen = demand()

env = BeerGameEnv(demand_gen, lag=5)

api = env.start_play()
agents = []

state, r, d = next(api)

shape = np.array(state).flatten().shape

for i in range(4):
    agents.append(DQN(state_shape=shape, n_action=10, net=simple_net))

from Beer_game.utils import chain_wrapper

bg = chain_wrapper(agents, env)


import matplotlib.pyplot as plt


bg.play(episode=10000)

length = len(bg.agents[0].cum_r)
sum_r = np.array(bg.agents[0].cum_r) + np.array(bg.agents[1].cum_r)+np.array(bg.agents[2].cum_r) + np.array(bg.agents[3].cum_r)
plt.plot(range(length), sum_r / np.array(bg.week_his))







