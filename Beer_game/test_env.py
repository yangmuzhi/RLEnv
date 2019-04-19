from Beer_game.beer_game_env import BeerGameEnv
import numpy as np

def demand():
    while True:
        yield np.random.uniform(10)
demand_gen = demand()


env = BeerGameEnv(demand_gen)
env.reset()

action = np.array([0,0,0,0])
env.stock
env.trans
env.step(action)
env.cost
env.cost_his

env.reset()
for i in range(50):
    action = np.random.uniform(0,10,4)
    env.step(action)



env.cost_his
