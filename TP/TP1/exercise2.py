# ############################################################################
# file_input exercise2.py
# Programmation Orienté Objet (POO) TP1 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Rami Aridi - Tous droits réservés.
# ############################################################################

"""Execute les fonctions de la premiere partie"""

from math import cos, sin
import matplotlib.pyplot as plt
from exercise1 import Point, Vecteur

class Triangle(): # on ne peut pas creer un triangle par defaut
    "Represents a triangle with three vertices."""
    def __init__(self, point_1 : Point,
                 point_2 : Point,
                 point_3 : Point,
                 couleur : str) -> 'Triangle':
        self.point1 = point_1
        self.point2 = point_2
        self.point3 = point_3
        self.couleur = couleur

    def tourner_triangle(self, angle : float) -> None:
        """
        Rotates the triangle by the given angle around the z-axis.

        Args:
            angle: The angle in radians by which to rotate the triangle.
        """
        cos_angle = cos(angle)
        sin_angle = sin(angle)

        # We apply here the rotation transformation to each point of the triangle
        # Rotation du point 1
        x1 = self.point1.x  # Stocker la valeur d'origine de x
        y1 = self.point1.y  # Stocker la valeur d'origine de y
        self.point1.x = x1 * cos_angle - y1 * sin_angle
        self.point1.y = x1 * sin_angle + y1 * cos_angle

        # Rotation du point 2
        x2 = self.point2.x
        y2 = self.point2.y
        self.point2.x = x2 * cos_angle - y2 * sin_angle
        self.point2.y = x2 * sin_angle + y2 * cos_angle

        # Rotation du point 3
        x3 = self.point3.x
        y3 = self.point3.y
        self.point3.x = x3 * cos_angle - y3 * sin_angle
        self.point3.y = x3 * sin_angle + y3 * cos_angle
    def afficher_triangle(self) -> str:
        """Displays the coordinates of the triangle's vertices."""
        return f"{self.point1.afficher()},{self.point2.afficher()}, {self.point3.afficher()}"

    def deplacer(self, vecteur_translation: Vecteur) -> None:
        """
        Displaces the triangle by the given translation vector.

        Args:
            vecteur_translation: The vector representing the translation (shift) amount.
        """
        self.point1.x += (vecteur_translation.point_2.x - vecteur_translation.point_1.x)
        self.point1.y += (vecteur_translation.point_2.y - vecteur_translation.point_1.y)
        self.point2.x += (vecteur_translation.point_2.x - vecteur_translation.point_1.x)
        self.point2.y += (vecteur_translation.point_2.y - vecteur_translation.point_1.y)
        self.point3.x += (vecteur_translation.point_2.x - vecteur_translation.point_1.x)
        self.point3.y += (vecteur_translation.point_2.y - vecteur_translation.point_1.y)

    def plot(self) -> None:
        """plot self"""

        x = [self.point1.x, self.point2.x, self.point3.x, self.point1.x] #fermeture du triangle
        y = [self.point1.y, self.point2.y, self.point3.y, self.point1.y]
        plt.xlim(-5, 5)
        plt.ylim(-5, 5)
        plt.plot(x, y, self.couleur)
        # plt.show()
        # plt.grid(True)

    def fill(self) -> None:
        """fill self"""

        x = [self.point1.x, self.point2.x, self.point3.x, self.point1.x] #fermeture du triangle
        y = [self.point1.y, self.point2.y, self.point3.y, self.point1.y]
        plt.xlim(-5, 5)
        plt.ylim(-5, 5)
        plt.fill(x, y, self.couleur)
        # plt.show()
        # plt.grid(True)
        
