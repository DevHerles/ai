import numpy as np
import gym  # pip intall gym
import random

env = gym.make("FrozenLake-v1", is_slippery=False)

action_space_size = env.action_space.n
state_space_size = env.observation_space.n

qtable = np.zeros((state_space_size, action_space_size))
print(qtable)

# Hyper Parameters
total_episodes = 10000
learning_rate = 0.2  # 0-1
max_steps = 100
gamma = 0.99

epsilon = 1  # exploration, exploitation 0 -> 1
max_epsilon = 1
min_epsilon = 0.01
decay_rate = 0.001

rewards = []

for episode in range(total_episodes):
    state = env.reset()
    step = 0
    done = False
    total_rewards = 0

    for step in range(max_steps):
        if random.uniform(0, 1) > epsilon:
            action = np.argmax(qtable[state[0], :])  # Exploit
        else:
            action = env.action_space.sample()  # Explore

        print("action", action)
        new_state, reward, done, x, info = env.step(action)

        max_new_state = np.max(qtable[new_state, :])

        qtable[state[0], action] = qtable[state[0], action] + learning_rate * (
            reward + gamma * max_new_state - qtable[state[0], action]
        )

        total_rewards += reward

        state = [new_state, {}]
        if done:
            break

    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)
    rewards.append(total_rewards)

print("Score:", str(sum(rewards) / total_episodes))
print(qtable)


def main():
    env.reset()

    for episode in range(5):
        state = env.reset()
        step = 0
        done = False

        print("Episode:", episode + 1)

        for step in range(max_steps):
            action = np.argmax(qtable[state[0], :])
            new_state, reward, done, truncanted, info = env.step(action)
            env.render()
            if done:
                print("Number of Steps:", step)
                break
            state = [new_state, info]

    env.close()


if __name__ == "__main__":
    main()
