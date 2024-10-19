# ############################################################################
# file_input test3.py
# Programmation Orienté Objet (POO) TP0 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Yanis Sadoun - Tous droits réservés.
# ############################################################################

import exercise3
from exercise2 import Vecteur
from math import pi

if __name__ == "__main__":
    # Test the Vecteur class
    vector1 = Vecteur() # by default it is (0, 0, 0)
    
    vector2 = Vecteur()
    vector2.initialisation(1.0, 0.0, 0.0)

    vector3 = Vecteur()
    vector3.initialisation(0.0, 1.0, 0.0)

    # Print the vectors that were created
    print(f"Vecteur v1: {vector1.afficher()}")
    print(f"Vecteur v2: {vector2.afficher()}")
    print(f"Vecteur v3: {vector3.afficher()}")

    triangle1 = exercise3.Triangle(vector1, vector2, vector3)
    print("Triangle 1: ", triangle1.afficher_triangle())

    # Test triangle turn
    print("\n==============================\nTesting triangle turn")
    triangle1.tourner_triangle(pi/2)
    print(f"Triangle 1 rotation by {pi/2} radians (π/2):", triangle1.afficher_triangle())

    # Test triangle displacement
    print("\n==============================\nTesting triangle displacement")
    displacement_vector = Vecteur()
    displacement_vector.initialisation(2.0, 3.0, 4.0)
    triangle1.deplacer_triangle(displacement_vector)
    print(f"Triangle 1 displacement by {displacement_vector.afficher()}:", triangle1.afficher_triangle())
