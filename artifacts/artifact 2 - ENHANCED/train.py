import numpy as np
import matplotlib.pyplot as plt
from environment import TreasureMaze  # My custom maze environment class
from agent import DQNAgent  # My deep Q-learning agent class

#  Maze Setup 
# 1.0 = free cell, 0.0 = wall
maze = [
    [1.0, 1.0, 1.0, 1.0],
    [0.0, 0.0, 1.0, 0.0],
    [1.0, 1.0, 1.0, 1.0]
]

# Training Configuration 
episodes = 500          # Total number of episodes to train the agent
batch_size = 32         # How many experiences to train on at once

# Initialize Environment and Agent 
env = TreasureMaze(maze)
state_size = env.observe().shape[1]  # Flattened grid size
action_size = 4                      # Four possible directions (left, up, right, down)
agent = DQNAgent(state_size, action_size)

#  Metrics for Tracking Progress 
rewards = []
wins = []
epsilons = []

#  Training Loop ------------------------------------------------------------
for ep in range(episodes):
    env.reset((0, 0))  # Start pirate in the top-left corner
    total_reward = 0
    done = False

    while not done:
        state = env.observe()
        action = agent.act(state) #------------------------
        next_state, reward, status = env.act(action)
        done = (status != 'not_over')
        agent.memory.remember([state, action, reward, next_state, done])
        agent.train(batch_size) # ----------------------
        total_reward += reward

    # After episode ends # ----------------------------
    agent.decay_epsilon()

    rewards.append(total_reward)
    epsilons.append(agent.epsilon)
    wins.append(1 if status == 'win' else 0)

    # Print summary of the episode
    print(f"Episode {ep+1}/{episodes} — Reward: {total_reward:.2f}, Status: {status}, Epsilon: {agent.epsilon:.3f}")

# Save Training Visualizations 
import os
if not os.path.exists("plots"):
    os.makedirs("plots")

# Plot 1: Reward per Episode
plt.figure()
plt.plot(rewards)
plt.title("Reward per Episode")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.savefig("plots/reward_per_episode.png")

# Plot 2: Cumulative Wins
plt.figure()
plt.plot(np.cumsum(wins))
plt.title("Cumulative Wins")
plt.xlabel("Episode")
plt.ylabel("Wins")
plt.savefig("plots/wins.png")

# Plot 3: Epsilon Decay
plt.figure()
plt.plot(epsilons)
plt.title("Epsilon Decay")
plt.xlabel("Episode")
plt.ylabel("Epsilon")
plt.savefig("plots/epsilon_decay.png")

print(" Training complete! Plots saved to the 'plots/' folder.")
