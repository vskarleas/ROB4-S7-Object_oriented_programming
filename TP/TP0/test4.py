# ############################################################################
# file_input test4.py
# Programmation Orienté Objet (POO) TP0 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Yanis Sadoun - Tous droits réservés.
# ############################################################################

from exercise4 import Couleur, Objet3D
from exercise2 import Vecteur
from exercise3 import Triangle     

if __name__ == "__main__":
    # Create a color object
    couleur1 = Couleur(255, 0, 0)
    print(f"Couleur 1: {couleur1.red}, {couleur1.green}, {couleur1.blue}")

    # Create a 3D object
    centre_gravite = Vecteur()
    obj1 = Objet3D(couleur1, centre_gravite)

    # Create some triangles and add them to the object

    vector1 = Vecteur()
    vector2 = Vecteur()
    vector3 = Vecteur()

    vector2.initialisation(1.0, 0.0, 0.0)
    vector3.initialisation(0.0, 1.0, 0.0)

    # Create the triangles and add them to the object
    triangle1 = Triangle(vector1, vector2, vector3)
    triangle2 = Triangle(vector2, vector1, vector3)
    triangle3 = Triangle(vector3, vector2, vector1)

    # Adding triangles to the object
    # Test adding triangle in object3D
    print("\n==============================\nTesting adding triangle to object\nCheck out debuger logs when executing")
    obj1.ajouter_triangle(triangle1)
    obj1.ajouter_triangle(triangle2)

    # Test printing of the object
    print("\n==============================\nTesting printing of the object")
    # Display the object's vertices (which are the coordinates of the triangles)
    obj1.afficher_objet()

    # Test displacement of the object
    print("\n==============================\nTesting displacement of the object")
    displacement_vector = Vecteur()
    displacement_vector.initialisation(2.0, 3.0, 4.0)
    obj1.deplacer(displacement_vector)
    print(f"Object displaced by {displacement_vector.afficher()}:")
    obj1.afficher_objet()
