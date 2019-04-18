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
