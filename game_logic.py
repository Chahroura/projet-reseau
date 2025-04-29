# game_logic.py

# ----------- Partie 1 : Logique du jeu Tic Tac Toe (classique) -----------

class TicTacToe:
    def __init__(self):
        # Initialiser le plateau : 9 cases vides
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # Garde en mémoire le gagnant

    def print_board(self):
        # Affiche le plateau dans le terminal
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Retourne une liste des cases disponibles
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # Vérifie s'il reste des cases vides
        return ' ' in self.board

    def num_empty_squares(self):
        # Retourne le nombre de cases vides
        return self.board.count(' ')

    def make_move(self, square, letter):
        # Joue un coup
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Vérifie les lignes
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        # Vérifie les colonnes
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        # Vérifie les diagonales
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        # Pas de gagnant
        return False

# ----------- Partie 2 : Environnement Gym pour l'IA DRL -----------

import gym
import numpy as np
from gym import spaces

class TicTacToeEnv(gym.Env):
    def __init__(self):
        super(TicTacToeEnv, self).__init__()
        self.game = TicTacToe()  # Utilise la classe TicTacToe pour l'état du jeu
        self.action_space = spaces.Discrete(9)  # 9 actions possibles (0 à 8)
        self.observation_space = spaces.Box(low=0, high=2, shape=(9,), dtype=np.int8)

    def reset(self):
        # Réinitialise l'environnement
        self.game = TicTacToe()
        return self._get_obs()

    def _get_obs(self):
        # Convertir le plateau en un vecteur d'observation
        obs = []
        for spot in self.game.board:
            if spot == ' ':
                obs.append(0)   # Case vide
            elif spot == 'X':
                obs.append(1)   # Case joueur X
            else:
                obs.append(2)   # Case joueur O
        return np.array(obs)

    def step(self, action):
        # Appliquer une action
        done = False
        reward = 0

        if self.game.board[action] != ' ':
            reward = -10  # Mauvais coup = grosse pénalité
            done = True
            return self._get_obs(), reward, done, {}

        self.game.make_move(action, 'X')

        if self.game.current_winner == 'X':
            reward = 1  # Gagné
            done = True
        elif not self.game.empty_squares():
            done = True  # Match nul

        return self._get_obs(), reward, done, {}

    def render(self, mode='human'):
        # Affiche le plateau si besoin
        self.game.print_board()
