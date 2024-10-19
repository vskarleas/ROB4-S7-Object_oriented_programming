# ############################################################################
# file_input test2.py
# Programmation Orienté Objet (POO) TP1 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Rami Aridi - Tous droits réservés.
# ############################################################################

"""Execute les fonctions de la deuxieme partie"""

from math import pi
import matplotlib.pyplot as plt
from exercise2 import Triangle
from exercise1 import Vecteur, Point

if __name__ == "__main__":
    # Test the Vecteur class
    point_1 = Point(0.0, 0.0, "black") # by default it is (0, 0)
    point_2 = Point(1.0, 0.0, "black")
    point_3 = Point(0.0, 1.0, "black")

    # Print the vectors that were created

    print(f"Point 1: {point_1.afficher()}")
    print(f"Point 2: {point_2.afficher()}")
    print(f"Point 3: {point_3.afficher()}")

    triangle1 = Triangle(point_1, point_2, point_3, "red")
    print("Triangle 1: ", triangle1.afficher_triangle())


    # Test triangle turn
    print("\n==============================\nTesting triangle turn")
    ANGLE = pi/2
    print(f"Triangle 1 rotation by {pi/2} radians (π/2):", triangle1.afficher_triangle())

    triangle1.plot()
    plt.show()
    triangle1.tourner_triangle(ANGLE)
    triangle1.plot()
    plt.show()


    # plt.figure()
    # for i in range(int(ANGLE*100)):
    #     plt.cla()
    #     triangle1.tourner_triangle(ANGLE/100)
    #     triangle1.plot()
    #     plt.pause(0.001)

    # Test triangle displacement
    point_1 = Point(0.0, 0.0, "black") # by default it is (0, 0)
    point_2 = Point(1.0, 0.0, "black")
    point_3 = Point(0.0, 1.0, "black")

    print("\n==============================\nTesting triangle displacement")
    displacement_vector = Vecteur()
    displacement_vector.initialisation(point_1, point_2)

    print(f"Triangle 1 displacement by {displacement_vector.afficher()}:",
    triangle1.afficher_triangle())

    triangle2 = Triangle(point_1, point_2, point_3, "blue")
    triangle2.fill()
    plt.show()
    triangle2.deplacer(displacement_vector)
    triangle2.fill()
    plt.show()
