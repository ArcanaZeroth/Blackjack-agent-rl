# Porównanie Metod Reinforcement Learning w grze Blackjack 🃏

Projekt badawczy analizujący skuteczność klasycznych algorytmów uczenia ze wzmocnieniem (RL) oraz metod głębokich (Deep RL) w środowisku `Blackjack-v1` z biblioteki Gymnasium.

## 📋 Opis Projektu

Celem projektu było wytrenowanie agentów zdolnych do wypracowania optymalnej strategii gry bez znajomości zasad matematycznych Blackjacka. Badania skupiły się na porównaniu stabilności uczenia metod opartych na pełnych epizodach (Monte Carlo) względem metod różnic czasowych (TD Learning) oraz ich wariantów wykorzystujących sieci neuronowe.

Przeanalizowano cztery podejścia:
1.  **Deep Q-Network (DQN):** Off-policy, aproksymacja sieciami neuronowymi z buforem powtórek.
2.  **Monte Carlo Control:** First-visit MC, uczenie na rzeczywistych zwrotach bez bootstrappingu.
3.  **Q-learning:** Klasyczna metoda tabelaryczna (off-policy) z optymalizacją parametrów.
4.  **Actor-Critic (A2C):** Podejście hybrydowe optymalizujące jednocześnie politykę i funkcję wartości.

## 📊 Wyniki Eksperymentów

Modele trenowano przez **200 000 epizodów**. Ewaluacja została przeprowadzona na próbie **100 000 gier testowych** (bez eksploracji).

| Metoda | Wygrane | Przegrane | Remisy | Skuteczność |
| :--- | :---: | :---: | :---: | :---: |
| **DQN (Deep Q-Network)** | **43 308** | 47 861 | 8 831 | **43.3%** |
| **Monte Carlo Control** | 42 617 | 48 319 | 9 064 | **42.6%** |
| **Q-learning (Optimized)** | 42 314 | 48 394 | 9 292 | **42.3%** |
| **Actor-Critic (A2C)** | 42 337 | 48 141 | 9 522 | **42.3%** |
| *Basic Strategy (Baseline)* | *40 800* | *48 700* | *10 500* | *40.8%* |

## 🔍 Kluczowe Wnioski i Analiza

### 1. Przełom w optymalizacji Q-learningu
Wstępne eksperymenty wykazały dużą wrażliwość metody Q-learning na dobór parametrów, co skutkowało wynikami poniżej strategii bazowej (38.2%). Kluczowe okazało się wprowadzenie **jednoczesnego wygaszania współczynnika uczenia ($\alpha$) oraz parametru eksploracji ($\epsilon$)**. Pozwoliło to algorytmowi na poprawne uśrednienie wyników i osiągnięcie skuteczności **42.3%**, co zrównało go z zaawansowaną metodą A2C.

### 2. Dominacja i stabilność DQN
DQN osiągnął najwyższą skuteczność dzięki zastosowaniu *Experience Replay* oraz sieci docelowej# Porównanie Metod Reinforcement Learning w grze Blackjack 🃏

Projekt badawczy analizujący skuteczność klasycznych algorytmów uczenia ze wzmocnieniem (RL) oraz metod głębokich (Deep RL) w środowisku `Blackjack-v1` z biblioteki Gymnasium.

## 📋 Opis Projektu

Celem projektu było wytrenowanie agentów zdolnych do wypracowania optymalnej strategii gry bez znajomości zasad matematycznych Blackjacka. Badania skupiły się na porównaniu stabilności uczenia metod opartych na pełnych epizodach (Monte Carlo) względem metod różnic czasowych (TD Learning) oraz ich wariantów wykorzystujących sieci neuronowe.

Przeanalizowano cztery podejścia:
1.  **Deep Q-Network (DQN):** Off-policy, aproksymacja sieciami neuronowymi z buforem powtórek.
2.  **Monte Carlo Control:** First-visit MC, uczenie na rzeczywistych zwrotach bez bootstrappingu.
3.  **Q-learning:** Klasyczna metoda tabelaryczna (off-policy) z optymalizacją parametrów.
4.  **Actor-Critic (A2C):** Podejście hybrydowe optymalizujące jednocześnie politykę i funkcję wartości.

## 📊 Wyniki Eksperymentów

Modele trenowano przez **200 000 epizodów**. Ewaluacja została przeprowadzona na próbie **100 000 gier testowych** (bez eksploracji).

| Metoda | Wygrane | Przegrane | Remisy | Skuteczność |
| :--- | :---: | :---: | :---: | :---: |
| **DQN (Deep Q-Network)** | **43 308** | 47 861 | 8 831 | **43.3%** |
| **Monte Carlo Control** | 42 617 | 48 319 | 9 064 | **42.6%** |
| **Q-learning (Optimized)** | 42 314 | 48 394 | 9 292 | **42.3%** |
| **Actor-Critic (A2C)** | 42 337 | 48 141 | 9 522 | **42.3%** |
| *Basic Strategy (Baseline)* | *40 800* | *48 700* | *10 500* | *40.8%* |

## 🔍 Kluczowe Wnioski i Analiza

### 1. Przełom w optymalizacji Q-learningu
Wstępne eksperymenty wykazały dużą wrażliwość metody Q-learning na dobór parametrów, co skutkowało wynikami poniżej strategii bazowej (38.2%). Kluczowe okazało się wprowadzenie **jednoczesnego wygaszania współczynnika uczenia ($\alpha$) oraz parametru eksploracji ($\epsilon$)**. Pozwoliło to algorytmowi na poprawne uśrednienie wyników i osiągnięcie skuteczności **42.3%**, co zrównało go z zaawansowaną metodą A2C.

### 2. Dominacja i stabilność DQN
DQN osiągnął najwyższą skuteczność dzięki zastosowaniu *Experience Replay* oraz sieci docelowej