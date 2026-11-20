
from maze import labyrinthe, affiche_labyrinthe
from solver import solveur_bfs

# 1. Construire le labyrinthe
grille = labyrinthe()

# 2. Définir le départ et l'arrivée
depart = (24, 0)
arrivee = (1, 36)

# 3. Exécuter BFS
resultat = solveur_bfs(grille, depart, arrivee)

# 4. Afficher le résultat
if resultat is not None:
    print("Chemin trouvé !")
    print("Nombre de cases :", len(resultat))
    print("Chemin :", resultat)
else:
    print("Aucun chemin trouvé.")
