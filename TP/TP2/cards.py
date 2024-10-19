# ############################################################################
# file_input cards.py
# Programmation Orienté Objet (POO) TP2 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Rami Aridi - Tous droits réservés.
# ############################################################################

"""Declarations des classes pour le Joueur et les cartes."""
import random

class Joueur():
    """Classe pour les joueurs du jeu."""
    def __init__(self, nom : str = "Default", score : int = 0):
        self.nom = nom
        self.score = score

    def jouer_carte(self, carte : 'Card'):
        """Joue une carte au joueur."""
        carte.jouer(self)

    def change_name(self, new_nom : str):
        """Change le nom du joueur."""
        self.nom = new_nom


class Card():
    """Classe pour les cartes generiques (abstrait)."""
    def __init__(self):
        self.id = 0
        self.id_str = "NILL"
        self.effet = "NILL"

    def jouer(self, joueur : Joueur):
        """Met a jour le score du joueur en fonction de l'effet de la 
        carte avec un type specifié."""
        raise NotImplementedError("Le type de la carte n'est pas specifie.")

class Normale(Card):
    """Classe pour les cartes normales."""
    def __init__(self):
        super().__init__()
        self.id = 1
        self.id_str = "Normale"


    def jouer(self, joueur):
        points = random.randint(1, 10)
        joueur.score += points
        self.effet = f"Ajoute un nombre aleatoire de points entre 1 et 10.(+{points} points)."

class Bonus(Card):
    """Classe pour les cartes de bonus."""
    def __init__(self):
        super().__init__()
        self.id = 2
        self.id_str = "Bonus"

    def jouer(self, joueur):
        joueur.score *= 2
        self.effet = "Double son score."

class Malus(Card):
    """Classe pour les cartes de malus."""
    def __init__(self):
        super().__init__()
        self.id = 3
        self.id_str = "Malus"

    def jouer(self, joueur):
        joueur.score -= 5
        self.effet = "Retire 5 points."

class Chance(Card):
    """Classe pour les cartes de chance."""
    def __init__(self):
        super().__init__()
        self.id = 4
        self.id_str = "Chance"

    def jouer(self, joueur):
        points = random.randint(-5, 15)
        joueur.score += points
        if points < 0:
            self.effet = f"Ajoute ou retire un nombre aleatoire de points entre -5 et 15.(-{points} points)."
        else:  # points >= 0
            self.effet = f"Ajoute ou retire un nombre aleatoire de points entre -5 et 15.(+{points} points)."


def distribute_card(desk : list) -> Card:
    """Distribue une carte au hasard dans la pile de cartes."""
    choise = random.randint(0, len(desk) - 1)
    card = desk[choise]
    desk.pop(choise)
    return card

class Tricheur(Joueur):
    """Classe pour les joueurs qui sont tricheurs."""
    def __init__(self, joueur : Joueur):
        super().__init__(nom=joueur.nom, score=joueur.score)

    def jouer_carte(self, carte : Card):
        if carte.id != 3:  # Malus
            carte.jouer(self)
        # sinon, on ignore la carte
