# ############################################################################
# file_input exercise4.py
# Programmation Orienté Objet (POO) TP0 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Yanis Sadoun - Tous droits réservés.
# ############################################################################

"""This is the fourth exercise"""

from exercise2 import Vecteur
from exercise3 import Triangle

class Couleur():
    def __init__(self, r : int = 0, g : int = 0, b : int = 0) -> None:
        self.red = r
        self.green = g
        self.blue = b

class Objet3D():
    def __init__(self, couleur : Couleur, cetre_gravite : Vecteur = (0.0, 0.0, 0.0)) -> None:
        self.liste_triangle = []
        self.couleur = couleur
        self.centre_gravite = cetre_gravite

    def afficher_objet(self) -> str:
        """Displays the coordinates of the object's vertices."""
        n = len(self.liste_triangle)
        if n > 0:
            print("******** Method 1 **********")
            # Methode 1
            for i, triangle in enumerate(self.liste_triangle, start=1):
                print(f"Triangle {i}:")
                print(triangle.afficher_triangle())

            # Methode 2
            print("******** Method 2 **********")
            for i in range(n):
                print(f"Triangle {i+1}:")
                print(self.liste_triangle[i].afficher_triangle())

    def ajouter_triangle(self, triangle : Triangle) -> None:
        """Adds a triangle to the object."""
        self.liste_triangle.append(triangle)

    def deplacer(self, vecteur_translation : Vecteur) -> None:
        """Returns a new object displaced by the given values."""
        n = len(self.liste_triangle)
        self.centre_gravite = self.centre_gravite.addition(vecteur_translation)
        if n > 0:
            for i in range(n):
                self.liste_triangle[i].deplacer_triangle(vecteur_translation)
    
    
