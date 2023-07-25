from multi_armed_bandits.envs.mab_env import NormalBandit, random_float
from gym.spaces import Discrete
from gym import Env
import numpy as np

class RandomContextualBandit(Env):
    def __init__(self, n_states: int = 2, n_bandits: int = 2,
                 lowerbound_mean: float = -3., upperbound_mean: float = 3., 
                 lowerbound_std: float = 0.5, upperbound_std: float = 2.5): 
        self.observation_space = Discrete(n_states)
        self.action_space = Discrete(n_bandits)
        self.current_state = self.start_state = 0

        self.contextual_bandits = []
        for _ in range(n_states):
            bandits = []
            for _ in range(n_bandits):
                bandit = NormalBandit(mean=random_float(lowerbound_mean, upperbound_mean),
                                      std=random_float(lowerbound_std, upperbound_std))
                bandits.append(bandit)

            self.contextual_bandits.append(bandits)
        
    def step(self, action: int):
        TERMINATED = True
        TRUNCATED = False
        INFO = {}

        reward = self.contextual_bandits[self.current_state][action].sample()
        self.current_state = np.random.randint(self.observation_space.n)

        return self.current_state, reward, TERMINATED, TRUNCATED, INFO
    
    def reset(self, seed: int, options: dict):
        np.random.seed(seed)

        if "start_state" in options:
            self.start_state = options["start_state"]

        if "contextual_bandits" in options:
            self.contextual_bandits = options["contextual_bandits"]

        self.current_state = self.start_state
        INFO = {}

        return self.current_state, INFO