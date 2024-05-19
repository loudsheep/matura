# Liczenie wartości wyrażenia w ONP (odwrotna notacja polska)
Odwrotna notacja polska w skrócie ONP jest algorytmem stosowanym do zapisu wyrażeń arytmetycznych bez użycia nawiasów. Powstał on na podstawie notacji polskiej stworzonej przez polskiego matematyka Jana Łukasiewicza.

## Algorytm

**Lista kroków**
1. Jeśli wczytane wyrażenie jest liczbą, to wrzuć ją na **stos**.

1. Jeśli wyrażenie jest operatorem, to
    - zdejmij element ze szczytu stosu i zapisz go w zmiennej **a**
    - zdejmij kolejny element ze stosu i zapisz go do zmiennej **b**
    - wykonaj działanie **b operator a** i wrzuć wynik na stos (zwróć uwagę, że pierwszą liczbą działania jest liczba zapisana w zmiennej **b**).

1. Po wykonaniu algorytmu, na stosie pozostanie jedna liczba będąca wynikiem zastosowania algorytmu odwrotnej notacji polskiej.

## Przykład

Wyrażenie ```2 3 5 - 3 * -``` można rozpisać na kroki:

| Kolejna wartość wyrażenia | Operacja | Zawartość stosu |
| --- | --- | --- |
| ```2``` | Wrzuć 2 na stos | ```2``` |
| ```3``` | Wrzuć 3 na stos | ```2 3``` |
| ```5``` | Wrzuć 5 na stos | ```2 3 5``` |
| ```-``` | Zdejmij liczbę 5 ze stosu, następnie zdejmij liczbę 3 ze stosu, następnie wynik działania 3 - 5 wrzuć na stos | ```2 -2``` |
| ```3``` | Wrzuć 3 na stos | ```2 -2 3``` |
| ```*``` | Zdejmij liczbę 3 ze stosu, następnie zdejmij liczbę -2 ze stosu, następnie wynik działania -2 * 3 wrzuć na stos | ```2 -6``` |
| ```-``` | Zdejmij liczbę -6 ze stosu, następnie zdejmij liczbę 2 ze stosu, następnie wynik działania 2 - (-6) wrzuć na stos | ```8``` |

W postaci z nawiasami to wyrażenie można zapisać jako ```2 - (3 - 5) * 3 ```