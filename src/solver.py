
from collections import deque
from maze import obtenir_voisins


def reconstruire_chemin(predecesseur, arrivee):

    if arrivee not in predecesseur:
        return None

    chemin = []

    position = arrivee

    while position is not None:

        chemin.append(position)

        position = predecesseur[position]

    chemin.reverse()

    return chemin


def solveur_bfs(labyrinthe, depart, arrivee):

    # 1. Vérifier les positions
    nombre_lignes = len(labyrinthe)
    nombre_colonnes = len(labyrinthe[0])

    for ligne, colonne in (depart, arrivee):

        if not (0 <= ligne < nombre_lignes
                and 0 <= colonne < nombre_colonnes):
            return None

        if labyrinthe[ligne][colonne] != "0":
            return None

    # 2. Initialiser la file
    file = deque([depart])

    # 3. Enregistrer les cases visitées
    visites = {depart}

    # 4. Enregistrer les prédécesseurs
    predecesseur = {depart: None}

    # 5. Explorer le labyrinthe
    while file:

        courant = file.popleft()

        # Vérifier si la sortie est trouvée
        if courant == arrivee:
            return reconstruire_chemin(predecesseur, arrivee)

        # Explorer les voisins accessibles
        voisins = obtenir_voisins(labyrinthe, courant)

        for voisin in voisins:

            if voisin not in visites:

                visites.add(voisin)

                predecesseur[voisin] = courant

                file.append(voisin)

    # Aucun chemin trouvé
    return None
