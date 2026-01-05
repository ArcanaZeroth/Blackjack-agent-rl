# Porównanie Metod Reinforcement Learning w grze Blackjack 🃏

Projekt badawczy mający na celu porównanie skuteczności klasycznych metod tabelarycznych oraz metod głębokiego uczenia ze wzmocnieniem (Deep RL) w środowisku `Blackjack-v1` z biblioteki Gymnasium.

## 📋 Opis Projektu

Celem projektu było zaprojektowanie agentów uczących się optymalnej strategii gry w Blackjacka i porównanie ich wyników ze standardową strategią bazową (Basic Strategy). Przeanalizowano cztery podejścia:
1.  **Monte Carlo Control** (First-visit)
2.  **Q-learning** (Tabelaryczny)
3.  **Deep Q-Network (DQN)** (Aproksymacja sieciami neuronowymi)
4.  **Actor-Critic (A2C)** (Podejście gradientowe z krytykiem)

## 🛠️ Technologie

* **Język:** Python 3.11
* **Środowisko:** [Gymnasium](https://gymnasium.farama.org/) (`Blackjack-v1`)
* **Deep Learning:** PyTorch
* **Obliczenia:** NumPy

## 📂 Struktura Plików

* `DQN.ipynb` - Implementacja Deep Q-Network z buforem powtórek (Replay Buffer) i siecią docelową (Target Network).
* `A2C.ipynb` - Implementacja algorytmu Actor-Critic z dwiema osobnymi sieciami neuronowymi.
* `monte-carlo.ipynb` - Klasyczna metoda Monte Carlo (First-visit MC control).
* `q-learning.ipynb` - Implementacja tabelarycznego Q-learningu.

## 🚀 Jak uruchomić

1.  Sklonuj repozytorium:
    ```bash
    git clone [https://github.com/twoj-nick/blackjack-rl.git](https://github.com/twoj-nick/blackjack-rl.git)
    cd blackjack-rl
    ```

2.  Zainstaluj wymagane biblioteki:
    ```bash
    pip install gymnasium numpy torch jupyter
    ```

3.  Uruchom wybrany notatnik Jupyter (np. `DQN.ipynb`) lub przekonwertuj go do skryptu Python.

## 📊 Wyniki Eksperymentów

Każdy agent był trenowany przez **200 000 epizodów**, a następnie ewaluowany na **100 000 gier testowych** (bez eksploracji).

| Metoda | Wygrane | Przegrane | Remisy | Skuteczność (%) |
| :--- | :---: | :---: | :---: | :---: |
| **DQN (Deep Q-Network)** | **43 308** | 47 861 | 8 831 | **43.3%** |
| Monte Carlo | 42 617 | 48 319 | 9 064 | 42.6% |
| Actor-Critic (A2C) | 42 337 | 48 141 | 9 522 | 42.3% |
| *Basic Strategy (Baseline)* | *~40 800* | *~48 700* | *~10 500* | *40.8%* |
| Q-learning | 38 161 | 53 337 | 8 502 | 38.2% |

> **Uwaga:** W Blackjacku kasyno zawsze ma matematyczną przewagę. Wynik powyżej 42-43% przy naturalnych zasadach jest uważany za zbliżony do optymalnego.

## 🔍 Wnioski i Analiza

1.  **Dominacja DQN:** Sieć neuronowa (DQN) osiągnęła najlepszy wynik, przewyższając "sztywną" strategię bazową. Zastosowanie *Experience Replay* pozwoliło na efektywne wykorzystanie rzadkich zdarzeń w grze.
2.  **Stabilność MC i A2C:** Metoda Monte Carlo oraz Actor-Critic osiągnęły wyniki bardzo zbliżone do teoretycznego optimum, deklasując strategię polegającą tylko na pasowaniu przy sumie 17.
3.  **Wrażliwość Q-learningu:** Algorytm Q-learning osiągnął wynik poniżej oczekiwań (gorszy od strategii bazowej).

## 📝 Autor
[Twoje Imię / Twój Nick]