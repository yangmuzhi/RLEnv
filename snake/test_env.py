#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from snake_env import Snakes_subsonic
import numpy as np
import time
env = Snakes_subsonic()
state = env.reset()

actions = np.array([1,0,0,0,1,0,0,0,0,1])
for a in actions:
    env.render()
    _,reward,done,_ = env.step(a)
    print(a)
    print("{}".format(reward), "\t {}".format(done))
    print(env.ground)
    time.sleep(1)
env.close()
