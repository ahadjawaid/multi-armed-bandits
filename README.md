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
There are two multi-armed bandit environments:

`MultiArmedBanditEnv`, `RandomContextualBandit`

There are 2 up to 10 armed bandit environment already regisitered for you to use and 2 to 10 contextual bandit environments. Here's an example of using a premade registered Multi-armed Bandit environment:

```python
import gym

env = gym.make("2-Armed-Bandit")
env.reset()
_, reward, _, _, _ = env.step()
```

Similarly we can use up to 10 arms for the preregistered environments.

```python
import gym

env = gym.make("10-Armed-Bandit")
env.reset()
_, reward, _, _, _ = env.step()
```

An example with contextual bandit environment:

```python
import gym

env = gym.make("3-Context-5-Armed-Bandit")
env.reset()
_, reward, _, _, _ = env.step()
```



And if you want to define your own customly configured multi-armed bandit you can do it as shown:

```python
from multi_armed_bandits.envs import MultiArmedBanditEnv

env = MultiArmedBanditEnv(n_bandits=15, lowerbound_mean=-3, upperbound_mean=3, 
                          lowerbound_std=0.5, upperbound_std=2.5)
env.reset()
_, reward, _, _, _ = env.step()
```

