PyCharm Community edition supports Jupyter notebooks in read-only mode, to get full support for local notebooks download and try PyCharm Professional now!


Try DataSpell — a dedicated IDE for data science,
with full support for local and remote notebooks


Try Datalore — an online environment
for Jupyter notebooks in the browser

Also read more about JetBrains Data Solutions on our website

Step-1
Importing Necessaary Packages and Creating a Taxi Environment
# Importing gym Package

import gym as g

# Importing Numpy

import numpy as np

# Creating a Taxi Environment

world = g.make('Taxi-v3')
Creating an instance of Taxi and giving it the intial state of its environment
# Creating a new instance of Taxi and getting intail state

state = world.reset()
Let me Demonstrate how this envirnment actuallly works
num_steps = 4
for s in range(num_steps+1):
    print(f"<---Step Number: {s}--->")

    # sample a random action from the list of available actions
    action = world.action_space.sample()

    # perform this action on the environment
    world.step(action)

    # print the new state
    world.render()

# end this instance of the taxi environment
world.close()
[2]
import gym as g
import numpy as np
import random 
# create Taxi environment
world = g.make('Taxi-v3')

# initialize q-table
state_size = world.observation_space.n
action_size = world.action_space.n
q_table = np.zeros((state_size, action_size))

# hyperparameters
learning_rate = 0.9
discount_rate = 0.8
epsilon = 1.0
decay_rate= 0.005

# training variables
num_episodes = 1000
max_steps = 99 # per episode

# training
for episode in range(num_episodes):

    # reset the environment
    state = world.reset()
    done = False

    for s in range(max_steps):

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
        q_table[state,action] = q_table[state,action] + learning_rate * (reward + discount_rate * np.max(q_table[new_state,:])-q_table[state,action])

        # Update to our new state
        state = new_state

        # if done, finish episode
        if done == True:
            break

    # Decrease epsilon
    epsilon = np.exp(-decay_rate*episode)

print(f"Training completed over {num_episodes} episodes")
input("Press Enter to watch trained agent...")

# watch trained agent
state = world.reset()
done = False
rewards = 0

for s in range(max_steps):

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
Training completed over 1000 episodes
TRAINED AGENT
Step 1
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (East)
score: -1
TRAINED AGENT
Step 2
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (South)
score: -2
TRAINED AGENT
Step 3
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (East)
score: -3
TRAINED AGENT
Step 4
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (East)
score: -4
TRAINED AGENT
Step 5
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (North)
score: -5
TRAINED AGENT
Step 6
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (East)
score: -6
TRAINED AGENT
Step 7
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (North)
score: -7
TRAINED AGENT
Step 8
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (Pickup)
score: -8
TRAINED AGENT
Step 9
+---------+
|R: | :_:G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (West)
score: -9
TRAINED AGENT
Step 10
+---------+
|R: | : :G|
| : | :_: |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (South)
score: -10
TRAINED AGENT
Step 11
+---------+
|R: | : :G|
| : | : : |
| : : :_: |
| | : | : |
|Y| : |B: |
+---------+
  (South)
score: -11
TRAINED AGENT
Step 12
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : |_: |
|Y| : |B: |
+---------+
  (South)
score: -12
TRAINED AGENT
Step 13
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (South)
score: -13
TRAINED AGENT
Step 14
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
  (Dropoff)
score: 7

