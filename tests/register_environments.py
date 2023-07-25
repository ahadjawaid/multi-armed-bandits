import unittest
import gym
import multi_armed_bandits
from gym.error import NameNotFound

def is_made(test, name):
    try:
        env = gym.make(name)
        test.assertIsInstance(env, gym.Env)
    except NameNotFound:
        test.assertTrue(False)
            
class TestRegisiteredEnvironment(unittest.TestCase):
    def test_registrations_MAB_env(self):
        for n_arms in range(2, 11):
            armed_name = f'{n_arms}-armed-bandit'

            is_made(self, armed_name)
            
            for n_states in range(2, 11):
                contextual_name = f'{n_states}-context-{n_arms}-armed-bandit'

                is_made(self, contextual_name)

