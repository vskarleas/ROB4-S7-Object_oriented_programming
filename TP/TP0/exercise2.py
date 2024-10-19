"""This is the second exercise"""

from math import sqrt, cos, sin

class Vecteur(): # pylint doesn't like 'object' in parenthesis
    """Represents a 3D vector with x, y, and z coordinates."""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def initialisation(self, x_in : float, y_in : float, z_in : float) -> None:
        """Initializes the vector with given values."""
        self.x = x_in
        self.y = y_in
        self.z = z_in

    def addition(self, other_vector) -> 'Vecteur':
        """Returns the sum of two vectors."""
        vecteur_res = Vecteur()
        vecteur_res.x = self.x + other_vector.x
        vecteur_res.y = self.y + other_vector.y
        vecteur_res.z = self.z + other_vector.z
        return vecteur_res
    def norme(self) -> float:

        """Returns the norm of the vector."""
        # Using the formula for the norm of a vector.
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def produit_scalaire(self, other_vector) -> float:
        """Returns the scalar product of two vectors."""
        return self.x * other_vector.x + self.y * other_vector.y + self.z * other_vector.z

    def tourner(self, angle : float) -> 'Vecteur':
        """Returns a new vector rotated by the given angle around the z-axis."""
        vecteur_res = Vecteur()
        vecteur_res.x = self.x * cos(angle) - self.y * sin(angle)
        vecteur_res.y = self.x * sin(angle) + self.y * cos(angle)
        vecteur_res.z = self.z
        return vecteur_res

    def afficher(self) -> str:
        """Displays the vector's components."""
        return f"({self.x:.1f}, {self.y:.1f}, {self.z:.1f})"
        # Displaying the vector's components with 1 decimal place.
