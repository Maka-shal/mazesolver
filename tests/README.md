# Documentation complémentaire — Projet Python : Générateur et solveur de labyrinthes

## 1. Compréhension générale du projet

### 1.1. Qu'est-ce qu'un labyrinthe informatique ?

Un labyrinthe informatique est une représentation d'un espace composé de plusieurs cases. Certaines cases permettent le déplacement, tandis que d'autres représentent des obstacles.

Dans ce projet, le labyrinthe est représenté sous forme de grille composée de lignes et de colonnes.

Chaque case possède une valeur qui indique sa nature :

| Valeur | Signification |
|---|---|
| 0 | Passage libre |
| 1 | Mur ou obstacle |

Le programme devra progressivement apprendre à reconnaître les passages, éviter les murs et trouver un chemin entre le point de départ et la sortie.

### 1.2. Qu'est-ce qu'un algorithme ?

Un algorithme est une suite d'instructions organisées permettant de résoudre un problème.

Dans notre projet, l'algorithme devra notamment :
- Identifier la position actuelle.
- Examiner les cases voisines.
- Éliminer les positions interdites.
- Choisir les déplacements possibles.
- Rechercher progressivement un chemin vers la sortie.

### 1.3. Qu'est-ce qu'une grille ?

Une grille est une organisation de données en lignes et en colonnes.

Notre labyrinthe comporte :
- 26 lignes.
- 37 colonnes.
- 962 cases au total.

Calcul : 26 × 37 = 962.

---

# 2. Étape 1 — Comprendre le fonctionnement du projet

### 2.1. Objectif

Comprendre le problème que nous souhaitons résoudre avant de commencer la programmation.

### 2.2. Les éléments fondamentaux

**Le départ :** position à partir de laquelle le programme commence à rechercher un chemin.

**La sortie :** position que le programme doit atteindre.

**Les obstacles :** cases interdites qui empêchent le déplacement.

**Les passages :** cases libres permettant de circuler dans le labyrinthe.

**Le chemin :** ensemble de cases successives permettant de rejoindre la sortie depuis le départ.

### 2.3. Qu'est-ce qu'une position ?

Une position représente l'emplacement d'une case dans la grille.

Elle est généralement représentée par deux coordonnées :

`(ligne, colonne)`

Exemple :

```python
position = (3, 5)
```

Cela signifie que la case se trouve à la quatrième ligne et à la sixième colonne.

Attention : Python commence à compter à partir de zéro.

---

# 3. Étape 2 — Préparer l'environnement de développement

### 3.1. Qu'est-ce qu'un environnement de développement ?

Un environnement de développement est l'ensemble des outils utilisés pour écrire, organiser, exécuter et vérifier un programme.

Dans ce projet, nous utilisons notamment Python, Visual Studio Code et Git.

### 3.2. Qu'est-ce que VS Code ?

Visual Studio Code est un éditeur de code qui permet d'écrire et de modifier des programmes.

Il propose notamment :
- Un éditeur pour écrire le code.
- Un terminal pour exécuter les commandes.
- Une exploration des fichiers du projet.
- Des extensions pour faciliter la programmation.

### 3.3. Qu'est-ce que Git ?

Git est un système de gestion de versions.

Il permet de conserver l'historique des modifications effectuées dans un projet.

Quelques commandes importantes :

```bash
git init
```

Initialise un dépôt Git.

```bash
git add .
```

Prépare les fichiers modifiés pour être enregistrés.

```bash
git commit -m "message"
```

Enregistre un ensemble de modifications avec un message explicatif.

### 3.4. Qu'est-ce que GitHub ?

GitHub est une plateforme qui permet d'héberger des projets utilisant Git.

Il permet notamment de :
- Conserver son code en ligne.
- Présenter ses projets.
- Suivre l'évolution du travail.
- Collaborer avec d'autres développeurs.

### 3.5. Qu'est-ce que README.md ?

README.md est un fichier de documentation généralement placé à la racine d'un projet.

Il explique notamment :
- Le but du projet.
- Son fonctionnement.
- Les technologies utilisées.
- Les instructions d'installation et d'exécution.
- Les différentes étapes de développement.

L'extension `.md` signifie Markdown, un langage de balisage léger utilisé pour organiser et mettre en forme des documents.

---

# 4. Étape 3 — Représenter le labyrinthe

### 4.1. Qu'est-ce qu'une structure de données ?

Une structure de données est une manière d'organiser et de stocker des informations afin de pouvoir les utiliser facilement dans un programme.

Dans notre projet, nous utilisons une grille représentée par une liste de chaînes de caractères.

### 4.2. Qu'est-ce qu'une liste en Python ?

Une liste est une structure de données permettant de stocker plusieurs éléments dans une seule variable.

Exemple :

```python
nombres = [10, 20, 30, 40]
```

Chaque élément possède un indice permettant de le retrouver.

### 4.3. Qu'est-ce qu'une chaîne de caractères ?

Une chaîne de caractères est une suite de caractères représentée entre guillemets.

Exemple :

```python
ligne = "101001"
```

Cette chaîne contient six caractères.

Dans notre labyrinthe, chaque caractère représente une case.

Pour accéder à un caractère :

```python
ligne[0]
```

Résultat : `"1"`.

### 4.4. Pourquoi utiliser une liste de chaînes de caractères ?

Exemple :

```python
grille = [
    "11111",
    "10001",
    "10101",
    "10001",
    "11111"
]
```

Chaque chaîne représente une ligne du labyrinthe.

La liste contient toutes les lignes.

Pour accéder à une case, nous utilisons :

```python
grille[ligne][colonne]
```

Exemple :

```python
grille[2][2]
```

Cette instruction permet d'accéder au caractère situé à la troisième ligne et à la troisième colonne.

### 4.5. Comprendre la fonction len()

`len()` est une fonction intégrée de Python qui permet de connaître le nombre d'éléments d'une structure.

Exemple :

```python
grille = [
    "11111",
    "10001",
    "10101"
]

print(len(grille))
```

Résultat :

```text
3
```

Cela signifie que la grille possède trois lignes.

Pour connaître le nombre de colonnes :

```python
print(len(grille[0]))
```

Résultat :

```text
5
```

### 4.6. Comprendre les fonctions du Jour 3

**creer_labyrinthe()**

Cette fonction construit ou renvoie la grille utilisée par le programme.

**verifier_dimensions()**

Cette fonction vérifie les dimensions de la grille en comptant les lignes et les colonnes.

**afficher_labyrinthe()**

Cette fonction parcourt les lignes et affiche les caractères du labyrinthe dans le terminal.

### 4.7. Qu'est-ce qu'une boucle imbriquée ?

Une boucle imbriquée est une boucle placée à l'intérieur d'une autre boucle.

Exemple :

```python
for ligne in grille:
    for case in ligne:
        print(case, end="")
    print()
```

La première boucle parcourt les lignes.

La deuxième boucle parcourt les caractères de chaque ligne.

Cela permet d'afficher le labyrinthe ligne par ligne.

---

# 5. Étape 4 — Définir les déplacements

### 5.1. Objectif

Permettre au programme d'identifier les cases accessibles autour d'une position donnée.

À ce stade, le programme ne cherche pas encore le chemin complet vers la sortie. Il apprend uniquement à reconnaître les déplacements autorisés.

### 5.2. Qu'est-ce qu'un voisin ?

Un voisin est une case directement adjacente à la position actuelle.

Dans notre projet, nous autorisons quatre directions :
- Haut.
- Bas.
- Gauche.
- Droite.

Les déplacements diagonaux ne sont pas autorisés.

### 5.3. Comprendre les déplacements avec les coordonnées

Une position est représentée par :

```python
(ligne, colonne)
```

Pour calculer les nouvelles coordonnées :

| Direction | Nouvelle ligne | Nouvelle colonne |
|---|---|---|
| Haut | ligne - 1 | colonne |
| Bas | ligne + 1 | colonne |
| Gauche | ligne | colonne - 1 |
| Droite | ligne | colonne + 1 |

On peut représenter ces déplacements avec une liste :

```python
directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]
```

Chaque couple représente une modification des coordonnées.

### 5.4. Qu'est-ce qu'une boucle for dans les déplacements ?

La boucle `for` permet de parcourir successivement les quatre directions.

```python
for dl, dc in directions:
```

Ici :
- `dl` représente la modification de la ligne.
- `dc` représente la modification de la colonne.

À chaque passage dans la boucle, Python prend une nouvelle direction.

### 5.5. Qu'est-ce qu'une condition ?

Une condition permet à un programme de prendre une décision selon qu'une situation est vraie ou fausse.

Exemple :

```python
if condition:
    instruction
```

Dans notre projet, les conditions servent à vérifier si une case peut être visitée.

### 5.6. Vérifier les limites de la grille

Le programme ne doit pas sortir des limites du labyrinthe.

Pour cela, nous vérifions :

```python
0 <= nouvelle_ligne < nombre_lignes
```

Et :

```python
0 <= nouvelle_colonne < nombre_colonnes
```

L'opérateur `and` permet de vérifier les deux conditions simultanément.

Si l'une des coordonnées dépasse les limites, la position est rejetée.

### 5.7. Vérifier les obstacles

Après avoir vérifié les limites, nous devons vérifier si la case contient un passage ou un mur.

Dans notre grille :

```python
"0" = passage
"1" = mur
```

La vérification s'effectue avec :

```python
if grille[nouvelle_ligne][nouvelle_colonne] == "0":
```

Les guillemets sont nécessaires parce que notre labyrinthe est représenté par des chaînes de caractères.

### 5.8. Qu'est-ce qu'une liste vide ?

Une liste vide est une liste qui ne contient aucun élément.

Exemple :

```python
voisins = []
```

Elle servira à enregistrer les coordonnées des cases accessibles.

### 5.9. Qu'est-ce que append() ?

`append()` est une méthode qui permet d'ajouter un élément à la fin d'une liste.

Exemple :

```python
voisins.append((2, 3))
```

Cette instruction ajoute la position `(2, 3)` dans la liste des voisins.

### 5.10. Qu'est-ce que return ?

`return` est une instruction qui permet de renvoyer une valeur depuis une fonction.

Exemple :

```python
def addition(a, b):
    resultat = a + b
    return resultat
```

La fonction renvoie le résultat du calcul à l'endroit où elle a été appelée.

Dans notre projet :

```python
return voisins
```

La fonction renvoie toutes les coordonnées des cases accessibles qu'elle a trouvées.

### 5.11. Fonctionnement général de obtenir_voisins()

La fonction suit les opérations suivantes :

1. Recevoir le labyrinthe et la position actuelle.
2. Séparer les coordonnées de la position.
3. Définir les quatre directions possibles.
4. Créer une liste vide pour stocker les voisins.
5. Calculer les dimensions de la grille.
6. Examiner chaque direction.
7. Calculer les nouvelles coordonnées.
8. Vérifier que la position reste dans la grille.
9. Vérifier que la case ne contient pas un mur.
10. Ajouter les coordonnées accessibles à la liste.
11. Renvoyer la liste des voisins.

### 5.12. Différence entre les déplacements et la résolution du labyrinthe

Il est important de ne pas confondre ces deux notions.

**Définir les déplacements :**

Le programme identifie les cases accessibles autour d'une position.

**Résoudre le labyrinthe :**

Le programme utilise les déplacements pour rechercher un chemin complet entre le départ et la sortie.

La recherche du chemin sera abordée dans les prochaines étapes du projet.

---

# 6. Bilan des connaissances acquises jusqu'au Jour 4

À la fin de cette quatrième étape, les connaissances suivantes doivent être comprises :

| Notion | Utilité dans le projet |
|---|---|
| Variable | Stocker des informations |
| Fonction | Organiser le programme |
| Liste | Stocker plusieurs éléments |
| Chaîne de caractères | Représenter les lignes |
| Indice | Accéder à une case |
| len() | Calculer les dimensions |
| Boucle for | Parcourir la grille |
| Condition if | Vérifier une situation |
| and | Combiner des conditions |
| append() | Ajouter un voisin |
| return | Renvoyer un résultat |
| Coordonnées | Localiser une case |
| Algorithme | Organiser les opérations |

**État d'avancement :** les étapes 1 à 4 constituent les bases de la représentation du labyrinthe et de la reconnaissance des déplacements accessibles.

Les prochaines étapes permettront d'utiliser ces connaissances pour rechercher et reconstruire un chemin vers la sortie.