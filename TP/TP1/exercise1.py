# ############################################################################
# file_input exercise1.py
# Programmation Orienté Objet (POO) TP1 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Rami Aridi - Tous droits réservés.
# ############################################################################

"""This is the first exercise"""

from multipledispatch import dispatch

class Point():
    """Represents a 2D point with x, y, and a colour."""
    def __init__(self, x:float=0, y:float=0, couleur:str="black") -> None:
        """
        Initialise un point avec les coordonnées x, y et une couleur.
        Par défaut, x=0, y=0, couleur='noir'.
        """
        self.x = x
        self.y = y
        self.couleur = couleur

    def afficher(self) -> str:
        """
        Affiche les informations du point.
        """
        f"Point(x={self.x:.1f}, y={self.y:.1f}, couleur='{self.couleur}')"


class Vecteur(): # pylint doesn't like 'object' in parenthesis
    """Represents a 2D vector with x and y."""
    def __init__(self, point_depart : Point = Point(),
                 point_arivee : Point = Point(), couleur : str = "black"):
        self.point_1 = point_depart
        self.point_2 = point_arivee
        self.couleur = couleur

    def __add__(self, other_vector : 'Vecteur') -> 'Vecteur':
        """Returns the sum of two vectors."""
        vecteur_res = Vecteur()
        vecteur_res.point_1.x = self.point_1.x + other_vector.point_1.x
        vecteur_res.point_1.y = self.point_1.y + other_vector.point_1.y
        vecteur_res.point_2.x = self.point_2.x + other_vector.point_2.x
        vecteur_res.point_2.y = self.point_2.y + other_vector.point_2.y
        return vecteur_res

    def __sub__(self, other_vector : 'Vecteur') -> 'Vecteur':
        """Returns the difference of two vectors."""
        vecteur_res = Vecteur()
        vecteur_res.point_1.x = self.point_1.x - other_vector.point_1.x
        vecteur_res.point_1.y = self.point_1.y - other_vector.point_1.y
        vecteur_res.point_2.x = self.point_2.x - other_vector.point_2.x
        vecteur_res.point_2.y = self.point_2.y - other_vector.point_2.y
        return vecteur_res

    @dispatch(object)
    def __mul__(self, other_vector: 'Vecteur') -> 'Vecteur':
        """Returns the product of a vector and a scalar."""
        vecteur_res = Vecteur()
        vecteur_res.point_1.x = self.point_1.x * other_vector.point_1.x
        vecteur_res.point_1.y = self.point_1.y * other_vector.point_1.y
        vecteur_res.point_2.x = self.point_2.x * other_vector.point_2.x
        vecteur_res.point_2.y = self.point_2.y * other_vector.point_2.y
        return vecteur_res

    @dispatch(int)
    def __mul__(self, scalar:int) -> 'Vecteur':
        vecteur_res = Vecteur()
        vecteur_res.point_1.x = self.point_1.x * scalar
        vecteur_res.point_1.y = self.point_1.y * scalar
        vecteur_res.point_2.x = self.point_2.x * scalar
        vecteur_res.point_2.y = self.point_2.y * scalar
        return vecteur_res

    def __truediv__(self, other_vector : 'Vecteur') -> 'Vecteur':
        vecteur_res = Vecteur()
        vecteur_res.point_1.x = self.point_1.x / other_vector.point_1.x
        vecteur_res.point_1.y = self.point_1.y / other_vector.point_1.y
        vecteur_res.point_2.x = self.point_2.x / other_vector.point_2.x
        vecteur_res.point_2.y = self.point_2.y / other_vector.point_2.y
        return vecteur_res

    def __str__(self):
        return f"({self.point_1.x:.1f}, {self.point_1.y:.1f},{self.point_2.x:.1f},{self.point_2.y:.1f})"

    def initialisation(self, point_1 : Point, point_2 : Point, ) -> None:
        """
        Initialise un vecteur avec deux points.
        """
        self.point_1.x = point_1.x
        self.point_1.y = point_1.y
        self.point_2.x = point_2.x
        self.point_2.y = point_2.y

    def afficher(self) -> str:
        """
        Affiche les informations du vecteur.
        """
        (f"(point_1={self.point_1.afficher()}, point_2={self.point_2.afficher()}, couleur='{self.couleur}')")
