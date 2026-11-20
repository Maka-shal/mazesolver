
import pytest

from src.solver import solveur_bfs


def test_chemin_direct():

    grille = [
        "11111",
        "10001",
        "11111"
    ]

    resultat = solveur_bfs(grille, (1, 1), (1, 3))

    assert resultat == [(1, 1), (1, 2), (1, 3)]


def test_chemin_avec_detour():

    grille = [
        "1111111",
        "1000001",
        "1111101",
        "1000001",
        "1111111"
    ]

    resultat = solveur_bfs(grille, (1, 1), (3, 5))

    assert resultat is not None
    assert resultat[0] == (1, 1)
    assert resultat[-1] == (3, 5)


def test_aucun_chemin():

    grille = [
        "11111",
        "10011",
        "11111",
        "11001",
        "11111"
    ]

    resultat = solveur_bfs(grille, (1, 1), (3, 3))

    assert resultat is None


def test_depart_egal_arrivee():

    grille = [
        "111",
        "101",
        "111"
    ]

    resultat = solveur_bfs(grille, (1, 1), (1, 1))

    assert resultat == [(1, 1)]


def test_coordonnees_invalides():

    grille = [
        "11111",
        "10001",
        "11111"
    ]

    resultat = solveur_bfs(grille, (-1, 1), (1, 3))

    assert resultat is None
