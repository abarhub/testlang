# testlang

Benchmark du trie avec différents langages.

## Intro
La génération du tableau est faite avec un algorithme speudo aléatoire (algorithme de congruence linéaire).
La description de l'algorithme est [ici](https://en.wikipedia.org/wiki/Linear_congruential_generator)
formule : x = (a * x + c) mod m
Les paramètres sont :
Nom | Valeur
--------------
modulo m | 2^48
multiplicateur a | 25214903917
incrément c | 11

## C
le trie est fait sur un tableau.
La methode de trie est sort de la librairie standard.

## C++
Le trie est fait sur un vector.
Le trie est fait avec la methode sort du vector.

## Java
Le trie est fait sur un ArrayList.
Le trie est fait avec la methode standard Collections.sort().

## Python
Le trie est fait sur une liste.
Le trie est fait avec la methode sort de la liste.
Il n'y a pas de compilation en Python.

## Résultat

Langage | Taille tableau | Durée compilation (en secondes) | Durée execution (en secondes)
---------------------------------------------------------------
C       | 10000000 | 0.04 | 3.49
C++     | 10000000 | 1.36 | 4.38
Java    | 10000000 | 0.57 | 5.14
Python  | 10000000 | 0.0  | 9.09 

C est le plus rapide en execution, et Python est le plus lent.
C++ est le plus long en compilation.

