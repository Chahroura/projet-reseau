# client_ai.py

import socket
import threading
import time
import numpy as np
from stable_baselines3 import PPO
from game_logic import TicTacToeEnv

# Config serveur
HOST = 'localhost'
PORT = 5555

# Connexion au serveur
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Recevoir son symbole (X ou O)
symbol = client.recv(1024).decode()
opponent_symbol = 'O' if symbol == 'X' else 'X'

# Charger l'agent DRL
env = TicTacToeEnv()
model = PPO.load("tictactoe_drl_agent")

# Démarrer l'environnement
env.reset()

def receive_moves():
    while True:
        try:
            move_data = client.recv(1024)
            if not move_data:
                print("[AI CLIENT] Déconnecté du serveur.")
                break
            move = int(move_data.decode())
            # Appliquer le mouvement de l'adversaire
            env.game.make_move(move, opponent_symbol)
        except:
            print("[AI CLIENT] Problème de connexion.")
            break

# Thread pour écouter l'adversaire
threading.Thread(target=receive_moves, daemon=True).start()

# Jouer automatiquement
while True:
    if env.game.board.count(' ') % 2 == (0 if symbol == 'X' else 1):
        # C'est à l'IA de jouer
        obs = env._get_obs()
        action, _states = model.predict(obs, deterministic=True)

        if env.game.board[action] == ' ':
            env.game.make_move(action, symbol)
            client.send(str(action).encode())
            time.sleep(0.5)  # Petite pause pour pas spammer
