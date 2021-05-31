# testlang

Benchmark du trie avec différents langages.

## Intro
La génération du tableau est faite avec un algorithme speudo aléatoire (algorithme de congruence linéaire).
La description de l'algorithme est [ici](https://en.wikipedia.org/wiki/Linear_congruential_generator)
formule : x = (a * x + c) mod m
Les paramètres sont :
| Nom              | Valeur      |
| ---------------- | ----------: |
| modulo m         | 2^48        |
| multiplicateur a | 25 214 903 917 |
| incrément c      | 11          |

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

## Go
Le trie est fait sur une liste, avec la methode sort.

## Build
Pour builder, en Python, en mode debug, pour le trie d'un tableau de 10000000 éléments, il faut executer la commande :
```bash
build.py --langage=python --debug --nbop=10000000
```

## Résultat

| Langage     | Taille tableau   | Durée compilation (en secondes) | Durée execution (en secondes) |
| ----------- | ---------------: | ------------------------------: | ----------------------------: |
| C           | 10 000 000       | 0.04                            | 3.49                          |
| C++         | 10 000 000       | 1.36                            | 4.38                          |
| Java        | 10 000 000       | 0.57                            | 5.14                          |
| Python      | 10 000 000       | 0.00                            | 9.09                          |
| Go          | 10 000 000       | 0.19                            | 2.13                          |
| Javascript  | 10 000 000       | 0.00                            | 16.11                         |
| Rust        | 10 000 000       | 0.77                            | 8.37                          |

Go est le plus rapide en execution, et Python est le plus lent.
C++ est le plus long en compilation.

