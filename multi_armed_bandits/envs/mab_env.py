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
    def __init__(self, n_bandits: int, lowerbound_mean=-3, upperbound_mean=3, 
                 lowerbound_std=0.5, upperbound_std=2.5):
        self.action_space = Discrete(n_bandits)
        self.observation_space = Discrete(1)

        self.bandits = [NormalBandit(mean=random_float(lowerbound_mean, upperbound_mean),
                                std=random_float(lowerbound_std, upperbound_std))
                                for _ in range(n_bandits)]

    def step(self, action: int) -> tuple:
        OBSERVATION = 0
        TERMINATED = True
        INFO = {}

        reward = self.bandits[action].sample()
        
        return OBSERVATION, TERMINATED, reward, {"prob": 1}, INFO

    def reset(self) -> None:
        pass

def random_float(lowerbound: float, upperbound: float) -> float:
    return np.random.uniform(lowerbound, upperbound)
