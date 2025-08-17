import matplotlib.pyplot as plt
import numpy as np
import os



# === Example data ===
rewards = [np.random.uniform(-5, 1) for _ in range(500)]
wins = [1 if r > 0 else 0 for r in rewards]
epsilons = np.linspace(1.0, 0.1, 500)

# === Ensuring 'plots' folder exists ===
if not os.path.exists("plots"):
    os.makedirs("plots")

# === Save plots ===

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

print("Plots saved in the 'plots/' folder.")
