import matplotlib.pyplot as plt
import numpy as np

# DANE Z WYNIKÓW
data = {
    'DQN':            {'wins': 43308, 'losses': 47861, 'draws': 8831},
    'A2C':            {'wins': 42337, 'losses': 48141, 'draws': 9522},
    'Monte Carlo':    {'wins': 42617, 'losses': 48319, 'draws': 9064},
    'Basic Strategy': {'wins': 40800, 'losses': 48700, 'draws': 10500},
    'Q-learning':     {'wins': 42314, 'losses': 48394, 'draws': 9292}
}

#  KONFIGURACJA
STARTING_BUDGET = 10000  # Kapitał początkowy (PLN)
BET_SIZE = 10           # Stawka na grę (PLN)
MAX_GAMES = 100000      # Maksymalna długość testu

plt.figure(figsize=(12, 7))

survival_stats = {}

for name, stats in data.items():
    # Tworzymy pulę wyników
    outcomes = ([BET_SIZE] * stats['wins'] +
                [-BET_SIZE] * stats['losses'] +
                [0] * stats['draws'])

    # Mieszamy wyniki (ustalamy seed dla powtarzalności porównania)
    np.random.seed(42)
    np.random.shuffle(outcomes)

    # Symulacja krok po kroku
    current_balance = STARTING_BUDGET
    history = [current_balance]

    for i, outcome in enumerate(outcomes):
        current_balance += outcome
        history.append(current_balance)

        # WARUNEK BANKRUCTWA
        if current_balance <= 0:
            current_balance = 0 # Żeby wykres nie szedł pod kreskę
            break

    # Zapisujemy ile gier przetrwał
    games_played = len(history) - 1
    survival_stats[name] = games_played

    # Rysowanie linii
    if name == 'DQN':
        plt.plot(history, label=f"{name} (Przetrwał: {games_played} gier)", color='#2ca02c', linewidth=2.5, zorder=5)
    elif name == 'Q-learning':
        plt.plot(history, label=f"{name} (Przetrwał: {games_played} gier)", color='#d62728', linewidth=1.5)
    else:
        plt.plot(history, label=f"{name} (Przetrwał: {games_played} gier)", linewidth=1.5, alpha=0.7)

# Oznaczenie momentu bankructwa
plt.axhline(0, color='black', linewidth=1.5, linestyle='--')
plt.text(0, 50, 'BANKRUCTWO (0 PLN)', color='black', fontsize=10, fontweight='bold')

plt.title(f'Symulacja Ryzyka Ruiny (Start: {STARTING_BUDGET} PLN, Stawka: {BET_SIZE} PLN)', fontsize=14)
plt.xlabel('Liczba rozdań', fontsize=12)
plt.ylabel('Stan konta (PLN)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# Zapisz wykres
plt.savefig('wykres_bankructwo.png', dpi=300)
plt.show()

plt.figure(figsize=(12, 7))

# Generowanie krzywych
for name, stats in data.items():
    # Tworzymy listę wyników (+10, -10, 0)
    outcomes = ([BET_SIZE] * stats['wins'] +
                [-BET_SIZE] * stats['losses'] +
                [0] * stats['draws'])

    # Mieszamy wyniki (seed 42 dla powtarzalności)
    np.random.seed(42)
    np.random.shuffle(outcomes)

    # Liczymy stan konta narastająco (bez przerywania przy 0)
    bankroll = np.cumsum(outcomes)

    if name == 'DQN':
        plt.plot(bankroll, label=f"{name} (Wynik: {bankroll[-1]} PLN)", color='#2ca02c', linewidth=2.5, zorder=5)
    elif name == 'Q-learning':
        plt.plot(bankroll, label=f"{name} (Wynik: {bankroll[-1]} PLN)", color='#d62728', linewidth=1.5)
    elif name == 'Basic Strategy':
        plt.plot(bankroll, label=f"{name} (Wynik: {bankroll[-1]} PLN)", color='black', linestyle='--', linewidth=1.5)
    else:
        plt.plot(bankroll, label=f"{name} (Wynik: {bankroll[-1]} PLN)", linewidth=1.5, alpha=0.7)

plt.title('Symulacja ciągła: Stan konta przy 100 000 rozdaniach (Stawka 10 PLN)', fontsize=14)
plt.xlabel('Liczba rozdań', fontsize=12)
plt.ylabel('Bilans (PLN)', fontsize=12)
plt.axhline(0, color='black', linewidth=1) # Linia zero
plt.grid(True, alpha=0.3)
plt.legend()

# Zapisz jako osobny plik
plt.savefig('wykres_finansowy.png', dpi=300, bbox_inches='tight')
plt.show()