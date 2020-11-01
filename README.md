# TP6
### Test & outils de corrections

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: Remise le [15 novembre 23h59](https://www.timeanddate.com/countdown/generic?iso=20201115T235959&p0=165&msg=Remise+TP4&font=cursive)

## Objectifs

## Consignes à respecter
- Indications de type (*Type hints*)
- Aucun ajout de librairie supplémentaires qui altéreraient l'esprit du TP. Cet exercice travaille beaucoup avec les matrices. S'il est vrai que du code très efficace pour gérer les opérations matricielles a déjà été écrit par d'autres (librairie *numpy* par exemple), l'intérêt ici est que vous développiez une compréhension du code, pas simplement d'appeler des fonctions haut niveau qui font tout le travail pour vous.. Par exemple la fonction transposer() doit être implémentée directement, l'utilisation du numpy.T est triviale et ne demande par vraiment de compréhension de votre part.
## Mise en contexte
Ce 4e TP s'orchestre autour du [jeu 2048](https://fr.wikipedia.org/wiki/2048_(jeu_vid%C3%A9o), devenu très populaire lors de sa sortie en 2014. Si vous avez besoin d'un petit rafraîchissement mémoire ou si vous ne connaissez pas dutout le jeu, suivez le lien wikipédia.

L'objectif est donc de "combiner" successivement des tuiles occupées par les mêmes puissances de 2 afin d'obtenir le nombre **2048** et gagner la partie. À chaque tour de jeu, on déplace l'ensemble des tuiles dans une des 4 directions de base (haut, bas, gauche, droite) et une nouvelle tuile **2** apparaît à un emplacement non-occupé aléatoire.  

![grille_2048](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/2048_Monotonicity.png/270px-2048_Monotonicity.png)
> Grille du jeu en cours de partie

Attention! C'est un jeu dangereusement satisfaisant et addictif.  
![grille_2048_victoire](https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/2048_finished_game.png/270px-2048_finished_game.png)
> Victoire, la tuile 2048 est obtenue après de tornitruants efforts!

Vous aurez donc à compléter la logique du jeu (*2048/logique.py)* et implémenter une série de tests (*2048/tests.py* afin de vérifier que les nombreux états limites de votre implémentation sont fonctionnels. Nous avons complété l'interface graphique du jeu (*2048/gui.py*) et vous n'avez pas a y toucher. L'acronyme anglais *GUI* signifie *graphical user interface*.

## Partie 1: Logique du jeu

Le fichier *logique.py* ne contient pas de *main* mais seuelement des fonctions qui seront appelées par le code de l'interface graphique (*gui.py*).
