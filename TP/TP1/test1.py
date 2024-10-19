"""Execute les fonctions de la deuxieme partie"""

import matplotlib.pyplot as plt
from exercise1 import Point, Vecteur

if __name__ == "__main__":
    vector1 = Vecteur(Point(1, 2, "rouge"), Point(4, 5, "noir"))
    vector2 = Vecteur(Point(3, 4, "bleu"), Point(6, 8, "gris"))

    # Test multiplication between vectors
    vector3 = vector1 * vector2
    print(vector3)

    # Test multiplication between vector and scalar
    vector3 = vector1 * 3
    print(vector3)

    # matplot vector 1
    plt.plot([vector1.point_1.x, vector1.point_2.x],
                [vector1.point_1.y, vector1.point_2.y],
                vector1.couleur)
    plt.show()
