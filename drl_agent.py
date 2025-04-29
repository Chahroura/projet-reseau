# drl_agent.py

import gym
from stable_baselines3 import PPO
import numpy as np
from game_logic import TicTacToe

class TicTacToeEnv(gym.Env):
    def __init__(self):
        super(TicTacToeEnv, self).__init__()
        self.game = TicTacToe()
        self.action_space = gym.spaces.Discrete(9)
        self.observation_space = gym.spaces.Box(low=0, high=2, shape=(9,), dtype=np.int8)

    def reset(self):
        self.game = TicTacToe()
        return self._get_obs()

    def _get_obs(self):
        obs = []
        for spot in self.game.board:
            if spot == ' ':
                obs.append(0)
            elif spot == 'X':
                obs.append(1)
            else:
                obs.append(2)
        return np.array(obs)

    def step(self, action):
        done = False
        reward = 0

        if self.game.board[action] != ' ':
            reward = -10
            done = True
            return self._get_obs(), reward, done, {}

        self.game.make_move(action, 'X')

        if self.game.current_winner == 'X':
            reward = 1
            done = True
        elif not self.game.empty_squares():
            done = True

        return self._get_obs(), reward, done, {}

    def render(self, mode='human'):
        self.game.print_board()

if __name__ == "__main__":
    env = TicTacToeEnv()

    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=10000)

    model.save("tictactoe_drl_agent")
    print("Modèle IA sauvegardé sous 'tictactoe_drl_agent.zip'")
