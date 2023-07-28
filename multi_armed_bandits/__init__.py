from gym.envs.registration import register

def register_environments():
    for n_arms in range(2, 11):
        register(
            id=f'{n_arms}-armed-bandit',
            entry_point='multi_armed_bandits.envs:MultiArmedBanditEnv',
            kwargs={'n_bandits': n_arms, "lowerbound_std": 1, "upperbound_std": 1},
            nondeterministic=True,
        )

        for n_states in range(2, 11):
            register(
                id=f'{n_states}-context-{n_arms}-armed-bandit',
                entry_point='multi_armed_bandits.envs:RandomContextualBandit',
                kwargs={'n_states': n_states, 'n_bandits': n_arms, 
                        "lowerbound_std": 1, "upperbound_std": 1},
                nondeterministic=True,
            )

register_environments()