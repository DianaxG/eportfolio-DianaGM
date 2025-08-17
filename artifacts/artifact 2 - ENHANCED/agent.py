import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from GameExperience import GameExperience

# This class defines my Deep Q-Learning agent.
# I used this to help my pirate agent learn how to navigate the maze environment and find the treasure.

class DQNAgent:
    def __init__(self, state_size, action_size, learning_rate=0.001, discount=0.95, epsilon=1.0, epsilon_min=0.1, epsilon_decay=0.995): # ---------------------------
        # These parameters help control how the agent learns
        self.state_size = state_size  # The number of features in each state (maze layout)
        self.action_size = action_size  # Number of possible actions: left, right, up, down
        self.discount = discount  # Gamma - how much future rewards are valued
        self.epsilon = epsilon  # Initial exploration rate
        self.epsilon_min = epsilon_min  # Minimum exploration rate
        self.epsilon_decay = epsilon_decay  # How quickly the agent shifts from exploring to exploiting
        self.model = self._build_model(learning_rate)  # Builds the neural network
        self.memory = GameExperience(self.model, max_memory=1000, discount=discount)  # Replay buffer for learning from past experiences

    def _build_model(self, learning_rate):
        # I used a simple feedforward neural network to approximate Q-values
        model = Sequential()
        model.add(Dense(64, input_dim=self.state_size, activation='relu'))  # First hidden layer with ReLU activation
        model.add(Dense(64, activation='relu'))  # Second hidden layer
        model.add(Dense(self.action_size, activation='linear'))  # Output layer for Q-values of each action
        model.compile(loss='mse', optimizer=Adam(learning_rate=learning_rate))  # Mean squared error loss
        return model

    def act(self, state):
        # This function selects an action using an epsilon-greedy policy
        if np.random.rand() <= self.epsilon:
            return np.random.randint(self.action_size)  # Explore: choose random action
        q_values = self.model.predict(state)[0]  # Exploit: choose action with highest predicted reward
        return np.argmax(q_values)

    def train(self, batch_size=32):
        # This trains the model using a batch of experiences from memory
        if len(self.memory.memory) < batch_size:
            return  # Not enough data to train yet
        inputs, targets = self.memory.get_data(batch_size)  # Generate training data from past experiences
        self.model.fit(inputs, targets, epochs=1, verbose=0)  # Train the model

    def decay_epsilon(self):
        # Slowly reduce epsilon after each episode to shift from exploration to exploitation
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
