from gym.spaces import Discrete
import numpy as np
import gym


class NormalBandit:
    def __init__(self, mean: float, std: float) -> None:
        self.mean = mean
        self.std = std

    def __repr__(self) -> str:
        return f"type: NormalBandit, mean: {round(self.mean, 2)}, std: {round(self.std, 2)}"
    
    def sample(self) -> float:
        return np.random.normal(self.mean, self.std)


class MultiArmedBanditEnv(gym.Env):
    def __init__(self, n_bandits: int, 
                 lowerbound_mean: float = -3., upperbound_mean: float = 3., 
                 lowerbound_std: float = 0.5, upperbound_std: float = 2.5):
        self.action_space = Discrete(n_bandits)
        self.observation_space = Discrete(1)

        self.bandits = [NormalBandit(mean=random_float(lowerbound_mean, upperbound_mean),
                                std=random_float(lowerbound_std, upperbound_std))
                                for _ in range(n_bandits)]

    def step(self, action: int) -> tuple:
        OBSERVATION = 0
        TERMINATED = True
        TRUNCATED = False
        INFO = {}

        reward = self.bandits[action].sample()
        
        return OBSERVATION, reward, TERMINATED, TRUNCATED, INFO

    def reset(self, seed: int = None, options: dict = {}) -> None:
        np.random.seed(seed)

        if "bandits" in options:
            self.bandits = options["bandits"]

        OBSERVATION = 0
        INFO = {}

        return OBSERVATION, INFO

def random_float(lowerbound: float, upperbound: float) -> float:
    return np.random.uniform(lowerbound, upperbound)
