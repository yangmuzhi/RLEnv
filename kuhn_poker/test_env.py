from kuhn_poker.kuhn_poker_env import Kuhn_Poker
import numpy as np
env = Kuhn_Poker()
api = env.start_play()
next(api)

env.card_in_hand
api.send(0)



h = api.send(1)
env.h_dict.values()
list(env.h_dict.values())[-1]
