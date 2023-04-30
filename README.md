# Taquin RL
Ce projet est un jeu de taquin jouable avec un agent utilisant l'apprentissage par renforcement (RL).

Le jeu de taquin est un puzzle numérique qui consiste à déplacer des tuiles dans un cadre pour les placer dans l'ordre numérique correct. Dans cette implémentation, le but est de placer les tuiles dans l'ordre croissant, avec la case vide en bas à droite.

Le projet comprend trois fichiers principaux :

+ `agent.py` : Contient la définition de l'agent abstrait, qui doit être implémenté pour créer un agent de taquin utilisant RL.
+ `game.py` : Contient la logique du jeu, y compris la boucle de jeu principale, la gestion des rounds, etc.
+ `grid.py` : Contient la classe Grid, qui définit la grille de taquin, les actions possibles et les vérifications de fin de partie.

## L'agent
Le fichier agent.py définit une classe abstraite Agent, qui doit être héritée pour créer un agent de taquin utilisant RL. L'agent a deux fonctions principales : `choose_action()` et `update()`. `choose_action()` est appelé à chaque tour pour décider de l'action à effectuer. `update()` est appelé après chaque tour pour mettre à jour l'état de l'agent en fonction de l'état actuel de la grille et de la récompense associée à l'action précédente.Dans le fichier `code\Agents` on peut retrouver nos 4 agents disponible: Random, Qlearning, Sarsa et Monte Carlo.

## Le jeu
Le fichier `game.py` contient la logique du jeu, y compris la boucle de jeu principale, la gestion des rounds, etc. La méthode `play_game()` est la méthode principale pour jouer une partie de taquin. Elle prend un agent en entrée et joue des rounds jusqu'à ce que le jeu soit terminé. La méthode retourne `True` si le jeu est gagné, sinon `False`.

## La grille
Le fichier `grid.py` contient la classe Grid, qui définit la grille de taquin, les actions possibles et les vérifications de fin de partie. La classe Grid a des fonctions pour effectuer des actions sur la grille (`take_action()`), vérifier si la grille est terminée (`is_finish()`), et obtenir les actions possibles à partir d'un état donné (`get_possible_actions()`). La grille est initialisée avec une taille donnée et des tuiles placées au hasard, mais vérifiées pour être résolvables.

## Reinforcement learning

### State space

Dans ce projet, nous nous concentrons sur la résolution d'une grille 3x3. La dimension des grilles possibles est alors 9!. Cependant, la moitié des grilles de Taquin ne sont pas solvables.
Notre state space est donc de dimension 9!/2 (on supprime la moitié des grilles avec la fonction `is_solvable`) soit **181440**. Si on veut une grille 4x4 alors le state space sera de 16!/2 soit 10461394944000

### Rewards

Pour nos agents, il y a plusieurs actions qui lui permettent de gagner ou perdre des récompenses :

+ Jouer un round : -1
+ Gagner la partie : +50000
+ 1 nouvel élément bien placé : +100
+ 1 élément qui était bien placé et qui a été déplacé : -10

Certains Q-Learners ont également d'autres méthodes :
+ Ligne du haut complétée : +1200
+ Colonne de gauche complétée : +1200

### Agents

+ Qlearner : l'agent Qlearner à été entrainé dans le notebook `train_Qlearner.ipynb` comme on a essayé plusieur reward le code de l'implémentation est un peu différent et se trouve dans le notebook.
+ Sarsa : L'entrainement se trouve dans `train_sarsa.ipynb`
+ montecarlo : L'entrainement se trouve dans `train_montecarlo.ipynb`

### Résultats 

Avec le Q-learner `QLearner_models/qlearner_500_rounds_99.npy` on obtient :
+ 99 % de victoire en moins de 500 rounds
+ 95 % de victoire en moins de 300 rounds
+ 90 % de victoire en moins de 200 rounds
+ 70 % de victoire en moins de 100 rounds

Pour SARSA : nous n'avons pas reussi à avoir de bon résultats lors de nos entrainements mais avec le modèle `QLearner_models/sarsa_1000_rounds_65.npy` on obtient:
+ 65 % de victoire en moins de 1000 rounds

Pour MonteCarlo : entrainement  très long car pour qu'ils soit enregistré les états doivent avoir été dans une partie gagnante

### Application

Voici un exemple d'application du jeu de taquin où le but est de retrouver l'image originale.

![](https://github.com/tiroumalaifreddy/taquin/blob/dev/gif/taquin.gif)

![](https://github.com/tiroumalaifreddy/taquin/blob/dev/gif/taquin2.gif)

![](https://github.com/tiroumalaifreddy/taquin/blob/dev/gif/taquin3.gif)
