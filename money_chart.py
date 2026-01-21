import matplotlib.pyplot as plt
import numpy as np

# DANE Z WYNIKÓW
data = {
    'DQN':            {'wins': 43308, 'losses': 47861, 'draws': 8831, 'Blackjack Wins': 4202},
    'A2C':            {'wins': 42337, 'losses': 48141, 'draws': 9522, 'Blackjack Wins': 4124},
    'Monte Carlo':    {'wins': 42617, 'losses': 48319, 'draws': 9064, 'Blackjack Wins': 4232},
    'Basic Strategy': {'wins': 40800, 'losses': 48700, 'draws': 10500, 'Blackjack Wins': 4124},
    'Q-learning':     {'wins': 42314, 'losses': 48394, 'draws': 9292, 'Blackjack Wins': 4124}
}

#  KONFIGURACJA
STARTING_BUDGET = 10000  # Kapitał początkowy (PLN)
BET_SIZE = 10           # Stawka na grę (PLN)
MAX_GAMES = 100000      # Maksymalna długość testu

# NOWY PARAMETR: Mnożnik za Blackjacka
BJ_PAYOUT_MULTIPLIER = 1.5 # Standardowo 1.5 (czyli 3:2), zmień na 1.0 jeśli chcesz wersję 1:1

plt.figure(figsize=(12, 7))

for name, stats in data.items():
    # OBLICZENIA WYNIKÓW Z UWZGLĘDNIENIEM BLACKJACKA
    bj_wins = stats['Blackjack Wins']
    regular_wins = stats['wins'] - bj_wins

    # Lista zysków/strat:
    # 1. Wygrane przez Blackjacka (np. +15 PLN)
    # 2. Wygrane zwykłe (np. +10 PLN)
    # 3. Przegrane (-10 PLN)
    # 4. Remisy (0 PLN)
    outcomes = (
            [int(BET_SIZE * BJ_PAYOUT_MULTIPLIER)] * bj_wins +
            [BET_SIZE] * regular_wins +
            [-BET_SIZE] * stats['losses'] +
            [0] * stats['draws']
    )

    np.random.seed(42)
    np.random.shuffle(outcomes)

    # --- SYMULACJA 1: RYZYKO RUINY ---
    current_balance = STARTING_BUDGET
    history = [current_balance]

    for outcome in outcomes:
        current_balance += outcome
        history.append(current_balance)
        if current_balance <= 0:
            current_balance = 0
            break

    games_played = len(history) - 1

    # Rysowanie (uproszczone dla czytelności)
    color = '#2ca02c' if name == 'DQN' else ('#d62728' if name == 'Q-learning' else None)
    lw = 2.5 if name == 'DQN' else 1.5
    plt.plot(history, label=f"{name} (Przetrwał: {games_played})", color=color, linewidth=lw)

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