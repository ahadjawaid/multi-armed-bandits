from gym.envs.registration import register

for arms in range(2, 11):
    register(
        id=f'{arms}-Armed-Bandit',
        entry_point='multi_armed_bandits.envs:MultiArmedBanditEnv',
        kwargs={'n_bandits': arms},
        nondeterministic=True,
    )