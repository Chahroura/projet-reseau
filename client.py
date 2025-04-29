# client.py

import socket
import threading
import tkinter as tk
from game_logic import TicTacToe

# Config serveur
HOST = 'localhost'
PORT = 5555

# Connexion au serveur
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Jeu
game = TicTacToe()
symbol = client.recv(1024).decode()
opponent_symbol = 'O' if symbol == 'X' else 'X'

# Interface
root = tk.Tk()
root.title(f"Tic Tac Toe - Joueur {symbol}")
buttons = []

def send_move(move):
    try:
        client.send(str(move).encode())
    except OSError:
        print("[CLIENT] Impossible d'envoyer le mouvement. Déconnecté du serveur.")


def button_click(i):
    if game.board[i] == ' ':
        game.make_move(i, symbol)
        update_buttons()
        try:
            send_move(i)
        except:
            print("[CLIENT] Erreur lors de l'envoi du mouvement.")
        if game.current_winner:
            end_game(f"Le joueur {symbol} a gagné!")


def update_buttons():
    for i in range(9):
        buttons[i]["text"] = game.board[i]

def receive_moves():
    while True:
        try:
            move_data = client.recv(1024)
            if not move_data:
                print("[CLIENT] Déconnecté du serveur.")
                root.quit()
                break
            move = int(move_data.decode())
            game.make_move(move, opponent_symbol)
            update_buttons()
            if game.current_winner:
                end_game(f"Le joueur {opponent_symbol} a gagné!")
        except:
            print("[CLIENT] Problème de connexion.")
            root.quit()
            break



def end_game(message):
    popup = tk.Toplevel()
    popup.title("Fin du Jeu")
    label = tk.Label(popup, text=message)
    label.pack(pady=10)
    ok_button = tk.Button(popup, text="OK", command=root.quit)
    ok_button.pack(pady=5)

for i in range(9):
    button = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Thread pour écouter les mouvements de l'adversaire
threading.Thread(target=receive_moves, daemon=True).start()

root.mainloop()
