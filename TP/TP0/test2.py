# ############################################################################
# file_input test2.py
# Programmation Orienté Objet (POO) TP0 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Yanis Sadoun - Tous droits réservés.
# ############################################################################

import exercise2
import sys
from math import pi

if __name__ == "__main__":
    if len(sys.argv) != 4: # Checking if the number of arguments is correct
        raise ValueError(f"Usage error: You can pass only 4 arguments for x, y and z in  order. Try again!\n")
    else:
        # Initializing the vectors
        x1= float(sys.argv[1])
        y1 = float(sys.argv[2])
        z1 = float(sys.argv[3])
        vector1 = exercise2.Vecteur()
        vector1.initialisation(x1, y1, z1)
        print(f"Vector 1: {vector1.afficher()}")

        vector2 = exercise2.Vecteur()
        vector2.initialisation(1.0, 2.0, 3.0)
        print(f"Vector 2: {vector2.afficher()}")

        # vector addition test
        print("\n==============================\nTesting addition (a)")
        vector3 = exercise2.Vecteur()  # Creating a new vector to store the result of addition
        vector3 = vector2.addition(vector1) # Adding the vectors
        print(f"Vector 3: {vector3.afficher()}")

        # vector norm test
        print("\n==============================\nTesting norm")
        print(f"Norm of Vector 1: {vector1.norme()}")

        # vector scalar product test
        print("\n==============================\nTesting scalar product")
        print(f"Scalar product of Vector 1 and Vector 2: {vector1.produit_scalaire(vector2)}")

        # vector rotation test
        print("\n==============================\nTesting rotation")
        vector4 = exercise2.Vecteur()  # Creating a new vector to store the result of rotation
        vector4 = vector1.tourner(pi/2) # Rotating the vector
        print(f"Vector 1 after rotation by {pi/2} radians (π/2): {vector4.afficher()}")
