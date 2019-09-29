from dino import Dino
from DQNAgent import DQNAgent
import numpy as np
import time

episodes = 500

state_size = 4
action_size = 3 # 1. do nothing, 2. jump, 3. lower

agent = DQNAgent(state_size, action_size)

dino = Dino()

for e in range(episodes):
    # start the game
    dino.start()
    
    state = dino.get_obstacles()
    state = np.reshape(state, [1, 4])

    done = False

    while not done:
        state = dino.get_obstacles()
        state = np.reshape(state, [1, 4])
        # decide action
        action = agent.act(state)
        
        if action == 1:
            dino.jump()
        elif action == 2:
            dino.lower()
        next_state = dino.get_obstacles()
        next_state = np.reshape(next_state, [1, 4])

        done = dino.is_game_over()
        reward = -0.1 if done else 0.1
        # remember the previous state, action, reward, and done
        agent.remember(state, action, reward, next_state, done)
        # make next_state the new current state for the next frame.
        state = next_state

    score = dino.get_score()
    print("episode: {}/{}, score: {}".format(e, episodes, score))

    # train the agent with the experience of the episode
    agent.replay(32)
