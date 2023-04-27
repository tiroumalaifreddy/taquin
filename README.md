# Taquin RL
Ce projet est un jeu de taquin jouable avec un agent utilisant l'apprentissage par renforcement (RL).

Le jeu de taquin est un puzzle numérique qui consiste à déplacer des tuiles dans un cadre pour les placer dans l'ordre numérique correct. Dans cette implémentation, le but est de placer les tuiles dans l'ordre croissant, avec la case vide en bas à droite.

Le projet comprend trois fichiers principaux :

+ `agent.py` : Contient la définition de l'agent abstrait, qui doit être implémenté pour créer un agent de taquin utilisant RL.
+ `game.py` : Contient la logique du jeu, y compris la boucle de jeu principale, la gestion des rounds, etc.
+ `grid.py` : Contient la classe Grid, qui définit la grille de taquin, les actions possibles et les vérifications de fin de partie.

## L'agent
Le fichier agent.py définit une classe abstraite Agent, qui doit être héritée pour créer un agent de taquin utilisant RL. L'agent a deux fonctions principales : `choose_action()` et `update()`. `choose_action()` est appelé à chaque tour pour décider de l'action à effectuer. `update()` est appelé après chaque tour pour mettre à jour l'état de l'agent en fonction de l'état actuel de la grille et de la récompense associée à l'action précédente.Dans le fichier `code\Agents` on peut retrouver nos 3 agents disponible: Random, Qlearning et Sarsa

## Le jeu
Le fichier `game.py` contient la logique du jeu, y compris la boucle de jeu principale, la gestion des rounds, etc. La méthode `play_game()` est la méthode principale pour jouer une partie de taquin. Elle prend un agent en entrée et joue des rounds jusqu'à ce que le jeu soit terminé. La méthode retourne `True` si le jeu est gagné, sinon `False`.

## La grille
Le fichier `grid.py` contient la classe Grid, qui définit la grille de taquin, les actions possibles et les vérifications de fin de partie. La classe Grid a des fonctions pour effectuer des actions sur la grille (`take_action()`), vérifier si la grille est terminée (`is_finish()`), et obtenir les actions possibles à partir d'un état donné (`get_possible_actions()`). La grille est initialisée avec une taille donnée et des tuiles placées au hasard, mais vérifiées pour être résolvables.

## Reinforcement learning

### 

### Rewards

Pour nos agents, il y a plusieurs actions qui lui permettent de gagner ou perdre des récompenses :

+ Jouer un round : -1
+ Gagner la partie : +50000
+ 1 élément bien placé : +100
+ 1 élément qui était bien placé et qui a été déplacé : -10

Certains Q-Learners ont également d'autres méthodes :
+ Ligne du haut complétée : +1200
+ Colonne de gauche complétée : +1200

### Résulats 

Avec le Q-learner `QLearner_Alexandre/Adrien_qlearner_500_rounds_99.npy` on obtient :
+ 99 % des win en moins de 500 rounds
+ 95 % des win en moins de 300 rounds
+ 90 % des win en moins de 200 rounds
+ 70 % des win en moins de 100 rounds

![](https://github.com/tiroumalaifreddy/taquin/blob/dev/taquin.gif)











