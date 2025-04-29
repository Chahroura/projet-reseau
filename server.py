# server.py

import socket
import threading

HOST = 'localhost'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

print(f"[SERVER] En écoute sur {HOST}:{PORT}")

clients = []
symbols = ['X', 'O']

def handle_client(client, player_id):
    client.send(symbols[player_id].encode())

    while True:
        try:
            move = client.recv(1024).decode()
            if move:
                print(f"[SERVER] Reçu du Joueur {player_id}: {move}")
                # Envoyer le mouvement à l'autre joueur
                other_client = clients[1 - player_id]  # 0 devient 1, 1 devient 0
                other_client.send(move.encode())
        except:
            print(f"[SERVER] Joueur {player_id} déconnecté.")
            client.close()
            break

def main():
    while len(clients) < 2:
        client, addr = server.accept()
        print(f"[SERVER] Connecté à {addr}")
        clients.append(client)

    print("[SERVER] 2 joueurs connectés, la partie commence.")

    for i, client in enumerate(clients):
        thread = threading.Thread(target=handle_client, args=(client, i))
        thread.start()

if __name__ == "__main__":
    main()
