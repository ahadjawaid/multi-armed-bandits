from setuptools import setup

setup(name='multi_armed_bandits',
      version='0.01',
      description='Package contains multi-armed bandit environments',
      url='https://github.com/ahadjawaid/multi-armed-bandits',
      author='Ahad Jawaid',
      packages=['multi_armed_bandits', 'multi_armed_bandits.envs'],
      author_email='',
      license='MIT License',
      install_requires=['gym>=0.2.3', 'numpy'],
)