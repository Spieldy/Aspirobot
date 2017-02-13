# Aspirobot
![alt tag](https://vgy.me/GaNIBk.gif)
- Théo Ménard
- Jérémy Spieldenner

## Instruction d'éxecution
Executer le fichier `Main.py` avec python

## Environnement
L'environnement est défini dans le fichier `Environment.py`. Il contient les classes `Mansion` et `Room`
Le manoir contient un tableau 2D de Room, la position du robot, ainsi que la mesure de performance.
La classe Room est une simple classe Quality-of-Life contenant de la poussière ou un bijou.
La seule logique contenue dans ce fichier est celle du calcul de performance lorsque le robot aspire ou ramasse le contenu d'une pièce.
Il est possible de changer la taille du manoir via son constructeur, et de changer les probabilités d'apparition d'éléments ainsi que les couts en performance pour chaque action.

### Affichage
- `@` Le robot
- `~` Poussière
- `o` Bijou
- `õ` Poussière et bijou

## Agent
L'agent est défini dans le fichier `Agent.py`. Il contient les classes `Robot`, `Actuator` et `Sensor`

### Capacité
Le robot utilise des capteurs et des effecteurs (classe `Sensor` et `Actuator`).
Il est ainsi capable de voir tout le manoir, et récupérer sa mesure de performance.
Il peut également se déplacer (haut bas gauche droite), aspirer une pièce (retire poussière ET bijou de la pièce en cours) et ramasser le contenu d'une pièce (retire uniquement un bijou)
Le robot consomme de l'énergie mais on la considère illimitée.

### Modèle BDI
Le robot implémente le modèle BDI (Belief - Desire - Intentions)
- Les **croyances** sont les mêmes que les percepts. Elles sont donc stockés comme un tableau 2D de room, identique a celui du mansion. Le robot l'initialise depuis son capteur.
- Les **désirs** sont stockés sous forme d'un tableau 2D de booleans représentant le manoir. True signifie qu'il souhaite acceder a cette case pour interagir avec, False que cette case est est ignorée pour le moment.
- Les **intentions** sont stockées dans une chaine de caractère représentant une action queue. Chaque lettre est une action :
  -`u, d, l, r` sont les directions
  -`s` pour aspirer une pièce
  -`p` pour ramasser
  
### Exploration
Périodiquement le robot s'arrête pour réfléchir aux actions qu'il va entreprendre (fonction `think()`)
Il va alors planifier un nombre d'action N en fonction de l'environnement autour de lui.
- Le robot parcourt chaque pièce du manoir pour déterminer celle qui contient quelque chose qui est la plus proche de lui (fonction `find_closest()`). Elle est ajoutée dans ses désirs. Si il ne trouve rien, il s'arrête là.
- Une fois trouvé, il va mettre à jour ses intentions pour atteindre cette objectif (fonction `update_intentions()`)
- Répete jusqu'à ce que l'action queue soit pleine. La prochaine salle la plus proche est déterminée depuis la dernière salle ajoutée à ses désirs.

L'exploration consomme une action dans la simulation, ainsi un robot peu confiant qui prend plus de temps pour réfléchir sera plus lent.

### Mesure de performance
Elle impacte directement la longueur de l'action queue : plus elle est élevée, plus le robot va déterminer un grand nombre d'action à l'avance.
- Faible perte de performance à chaque mouvement et action (cout de l'énergie)
- Gain dès qu'un objet est correctement aspiré ou ramassé
- Grande perte dès qu'un bijou est aspiré

Ainsi, plus le robot ramasse d'objet sans erreur, plus il planifiera à l'avance (= prise de confiance et minimisation du temps passé à réfléchir), plus il augmente ses chances d'aspirer un bijou.
