import numpy as np
import gym as g
import random
def main():

    # create Taxi environment
    world = g.make('Taxi-v3')

    # Let's Create a q-table
    # the State Sie
    state_size = world.observation_space.n

    # The action Size
    action_size = world.action_space.n

    # Creating a Q table
    q_table = np.zeros((state_size, action_size))

    # Declaring the hyperparameters

    # Learning Rate
    lr = 0.9

    # Discount Rate
    dr = 0.8

    # Creating Parameters for Exloration-Exploitation Staregy
    epsilon = 1.0
    decay_rate= 0.005

    # training variables
    episodes = 1000
    time_steps = 99 # per episode

    # Loop for training
    for episode in range(episodes):

        # reset the environment
        state = world.reset()
        done = False

        for s in range(time_steps):

            # exploration-exploitation tradeoff
            if random.uniform(0,1) < epsilon:
                # explore
                action = world.action_space.sample()
            else:
                # exploit
                action = np.argmax(q_table[state,:])

            # take action and observe reward

            new_state, reward, done, info = world.step(action)

            # Q-learning algorithm
            q_table[state,action] = q_table[state,action] + lr * (reward + dr * np.max(q_table[new_state,:])-q_table[state,action])

            # Update to our new state
            state = new_state

            # if done, finish episode
            if done == True:
                break

        # Decrease epsilon
        epsilon = np.exp(-decay_rate*episode)

    print(f"Training completed on {episodes} episodes")
    input("Press Enter to watch trained agent...")

    # watch trained agent
    state = world.reset()
    done = False
    rewards = 0

    for s in range(time_steps):

        print(f"TRAINED AGENT")
        print("Step {}".format(s+1))

        action = np.argmax(q_table[state,:])
        new_state, reward, done, info = world.step(action)
        rewards += reward
        world.render()
        print(f"score: {rewards}")
        state = new_state

        if done == True:
            break

    world.close()

if __name__ == "__main__":
    main()
