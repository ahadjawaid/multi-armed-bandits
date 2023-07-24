# multi-armed-bandits
This package contains multi-armed bandit (MAB) environments made using the Gym package.

## Installation 
```
pip install git+https://github.com/ahadjawaid/multi-armed-bandits
```

or 

```
git clone https://github.com/ahadjawaid/multi-armed-bandits.git

cd simple-gridworld

pip install .
```

## Usage
There are 2-10 multi armed bandit environment already regisitered for your use you can make one as shown in the following code.

```python
import gym

env = gym.make("2-Armed-Bandit")
env.reset()
_, reward, _, _, _ = env.step()
```

Similarlly we can create a multi armed bandit with up to 10 arms


```python
import gym

env = gym.make("10-Armed-Bandit")
env.reset()
_, reward, _, _, _ = env.step()
```

And if you want to define your own multi armed bandit with your own configuration you can do it as shown

```python
from multi_armed_bandits.envs import MultiArmedBanditEnv

env = MultiArmedBanditEnv(n_bandits=15, lowerbound_mean=-3, upperbound_mean=3, 
                          lowerbound_std=0.5, upperbound_std=2.5)
env.reset()
_, reward, _, _, _ = env.step()
```