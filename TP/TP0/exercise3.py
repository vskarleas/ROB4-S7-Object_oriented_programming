# ############################################################################
# file_input exercise3.py
# Programmation Orienté Objet (POO) TP0 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Yanis Sadoun - Tous droits réservés.
# ############################################################################

"""This is the third exercise"""

from exercise2 import Vecteur

class Triangle():
    "Represents a triangle with three vertices."""
    def __init__(self, vecteur1 : Vecteur,
                 vecteur2 : Vecteur,
                 vecteur3 : Vecteur) -> 'Triangle':
        self.point1 = vecteur1
        self.point2 = vecteur2
        self.point3 = vecteur3

    def tourner_triangle(self, angle : float) -> None:
        """Returns a new triangle rotated by the given angle around the z-axis."""
        self.point1 = self.point1.tourner(angle)
        self.point2 = self.point2.tourner(angle)
        self.point3 = self.point3.tourner(angle)

    def afficher_triangle(self) -> str:
        """Displays the coordinates of the triangle's vertices."""
        return f"Triangle vertices: {self.point1.afficher()},{self.point2.afficher()}, {self.point3.afficher()}"

    def deplacer_triangle(self, vecteur_translation : Vecteur) -> None:
        """Returns a new triangle displaced by the given values."""
        self.point1 = self.point1.addition(vecteur_translation)
        self.point2 = self.point2.addition(vecteur_translation)
        self.point3 = self.point3.addition(vecteur_translation)
