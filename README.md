# Le-Prince-Demon

Bonjour et bienvenue dans le dossier du jeu LE PRINCE DEMON en version DEMO,

Ceci signifie que le jeu normal est toujours en travaux (version histoire) mais une version à été crée pour tester les différentes features de notre jeu.

Cette version est appelée DEMO, elle est accessible depuis le menu principal.

Malgré tout, le prologue de l'histoire originale est disponible et fait office de tutoriel complet (comptez 15-20 min).

La démo comporte à ce jour :
- 30 min de durée de vie
- des combats classiques
- des combats de boss
- Un système de magie et de coups spéciaux handicapant l'adversaire
- le système d'inventaire, d'équipement et d'utilisation d'objet
- le système de navigation de map en map
- un système de choix
- une quête nécessitant des objets de l'inventaire
- un nom de héros personnalisable
- Un système de sauvegarde


## INSTALLATION

Il est conseillé de lancer le jeu sur le powershell (il à été testé et développé pour cet outil)

L'installation de l'interpréteur Python (3.9 de préférence) est obligatoire et est disponible à cette adresse https://www.python.org/downloads/

Vous devez ensuite installer la librairie PyGame dont le processus d'installation est résumé ici https://www.pygame.org/wiki/GettingStarted

### VERSION CONSOLE
Une fois tous ces outils installés vous devez ouvrir votre powershell et le configurer de la manière suivante (recommandé) :
- Police > Taille : 22
- Configuration > Taille de la fenêtre : Largeur : 123
- Configuration > Taille de la fenêtre : Hauteur : 42
- Couleurs > Arrière-plan : noir

Pour lancer le jeu, vous devez entrer dans votre powershell le chemin de votre dossier de jeu : 
pour vous y rendre faites cd .\"votre chemin "\ par exemple, sur mon pc j'entre :

          cd .\PycharmProjects\Le-prince-demon-DEMO\

Une fois dans mon dossier de jeu, lancez le script main.py, pour cela entrez:

          py .\main.py

### VERSION .EXE
double cliquez simplement sur "le prince demon.exe"
          
Bon jeu à vous.

## À PROPOS

CECI EST UN TEXT GAME NARRATIF et non un RPG classique, ce qui nous à fait faire le choix de mettre en avant la narration et le confort de jeu, impliquant donc moins de libertés.

### SYSTÈME DE MAGIE
Le système de magie est spécial, la mana se recharge a chaque combat (à l'inverse des pdv) néanmoins, l'utilisation des sorts coûte beaucoup de mana.
Les potions de mana de la démo sont donc à ce jour inutiles. Elles sont présentes par soucis de démonstration.

### SYSTÈME DE COUPS SPECIAUX (ou coups bas dans le mode histoire)
Ces coups sont à double tranchant, d'un côté ils nerfent totalement l'adversaire, jusqu'à la fin du combat.
Mais cet avantage à un prix, les attaques ont beaucoup de chances de rater.

### SYSTÈME DE SAUVEGARDE
La sauvegarde s'écrase à chaque fois que vous selectionnez "Nouvelle Partie".
