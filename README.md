# 📘 README.md — Jeu Tic Tac Toe Réseau + IA (DRL)

## 🎯 Objectif du projet

Ce projet consiste à développer un jeu **Tic Tac Toe (Morpion)** en ligne avec :
- **Communication réseau** entre 2 joueurs (client-serveur),
- **Interface graphique** simple (Tkinter),
- **Intelligence Artificielle** via **Deep Reinforcement Learning (DRL)** avec Stable-Baselines3.

Un joueur peut être un humain, l’autre peut être une **IA entraînée** avec PPO.

---

## 🗂️ Structure du projet

```
📁 projet-tictactoe/
│
├── server.py           # Serveur central qui connecte deux clients
├── client.py           # Interface pour un joueur humain (Tkinter)
├── client_ai.py        # Client automatisé (joueur IA)
├── drl_agent.py        # Script pour entraîner l'IA avec Stable-Baselines3
├── game_logic.py       # Logique du jeu + Environnement Gym pour IA
├── requirements.txt    # Liste des bibliothèques Python requises
└── README.md           # Ce fichier
```

---

## ✅ Prérequis

- Python 3.10 ou plus recommandé
- Utilisation de Thonny, VSCode ou terminal

### 📦 Installation des dépendances

Dans le terminal (ou CMD sous Windows) :

```bash
pip install -r requirements.txt
```

Si erreur avec `shimmy`, ajoute :

```bash
pip install "shimmy>=2.0"
```

---

## 🚀 Comment jouer

### 🔁 Mode Joueur vs Joueur (2 humains)

1. **Lancer le serveur** :
```bash
python server.py
```

2. **Lancer 2 fois `client.py`** dans 2 fenêtres séparées (deux joueurs humains) :
```bash
python client.py
```

---

### 🤖 Mode Joueur vs IA (humain vs intelligence artificielle)

1. **Lancer le serveur** :
```bash
python server.py
```

2. **Lancer le joueur humain** :
```bash
python client.py
```

3. **Lancer le joueur IA** :
```bash
python client_ai.py
```

> 🧠 L’IA va jouer automatiquement grâce à un modèle PPO entraîné.

---

## 🧠 Entraîner l'IA (facultatif)

Si tu veux (ré)entraîner le modèle IA toi-même :

```bash
python drl_agent.py
```

✅ Cela créera un fichier `tictactoe_drl_agent.zip` utilisé par `client_ai.py`.

Tu peux modifier le nombre d'étapes d'entraînement dans `drl_agent.py` :

```python
model.learn(total_timesteps=10000)  # augmente ou diminue si nécessaire
```

---

## 🧪 Tests possibles

| Mode | Commandes |
|------|-----------|
| Humain vs Humain | `server.py` + 2× `client.py` |
| Humain vs IA     | `server.py` + `client.py` + `client_ai.py` |
| Entraîner IA     | `drl_agent.py` |

---

## 🧰 Dépendances techniques

- `socket`, `threading` (réseau)
- `tkinter` (interface graphique)
- `stable-baselines3`, `gym`, `shimmy`, `numpy`, `torch` (IA DRL)

---

## 📌 Notes

- Le serveur **doit être lancé en premier**.
- Les clients doivent se connecter **dans l’ordre** (le joueur humain puis l’IA).
- Le jeu ne démarre **que quand 2 clients sont connectés**.

---

## 🧑‍💻 Auteur

Projet réseau + IA — Université de la Manouba  
A.U 2024-2025 — Cours : Fondements des Réseaux  
Étudiant : Ahmed chahdoura et youssef chtioui
