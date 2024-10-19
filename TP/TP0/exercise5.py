"""This is the game 421"""
from random import randint
import os


class De():
    """Represents a single die."""
    def __init__(self) -> None:
        self.current_face = randint(1, 6)

    def lancer(self) -> None:
        "Rolls the die and updates its current face value."""
        self.current_face = randint(1, 6)

    def valeur(self) -> int:
        "Returns the current face value as an integer."""
        return self.current_face

    def valeur_str(self) -> str:
        """Returns the current face value as a string."""
        return f"{self.current_face}"

class Joueur():
    "Represents a player with a set of dice."""
    def __init__(self, nom: str) -> None:
        self.nom = nom
        self.des = [De(), De(), De()]
        self.score = 0

    def lancer_des(self) -> None:
        "Rolls all the dice and updates their current face values."""
        for de in self.des:
            de.lancer() #On lance les dés

    def afficher_des(self) -> None:
        "Displays the current values of the dice."""
        print("")
        for i, de in enumerate(self.des, start=1):
            print(f"Valeur du dé {i}: {de.valeur_str()}")

class Jeu():
    "Represents a game with a set of players and dice."""
    def __init__(self) -> None:
        self.joueurs = []
        self.gagnant = None

    def ajouter_joueur(self, joueur: Joueur) -> None:
        "Adds a player to the game."""
        self.joueurs.append(joueur)

    def combinaisons(self, des:list) -> int:
        "Computes the score for the given dice combination."""
        sorted_list = [des[0].valeur(),des[1].valeur(),des[2].valeur()]
        #On crée un nouveau tableau de dés car la fonction sort() ne supporte pas la classe De()
        sorted_list.sort()  #On trie les dés pour comparer plus facilement les combinaisons
        if sorted_list == [1, 2, 4]:
            return 10
        if sorted_list[0] == sorted_list[1] == 1: #Si les deux dés sont "un"
            return sorted_list[2]
        if sorted_list[0] + 1 == sorted_list[1] and sorted_list[1] + 1 == sorted_list[2]:
            # Si les dés sont consécutifs
            return 2
        return 0

    def afficher_scores(self) -> None:
        "Displays the current scores of all players."""
        if len(self.joueurs) > 0:
            for joueur in self.joueurs: #On parcourt la liste des joueurs
                print(f"{joueur.nom}: {joueur.score}")
        else:
            print("Aucun joueur dans le jeu.")

    def on_va_jouer(self, joueur : Joueur) -> None:
        """Handles the turn of a player."""
        print(f"=======================\n\033[1m{joueur.nom}\033[0m, vous avez le tour!")
        joueur.lancer_des()
        joueur.afficher_des()

        while True: # On demande si le joueur veut relancer un dé
            nb_des_rejouer = int(input("\nCombien de dés voulez-vous relancer ? "))
            if nb_des_rejouer in (0, 1, 2):
                #On vérifie que le joueur a entré un nombre valide de dés à relancer
                break
            print("Veuillez entrer un nombre compris entre 0 et 2.")

        if nb_des_rejouer == 1:
            while True:
                id_de = int(input("\nQuel dé 1, 2, ou 3? "))
                #On demande au joueur quel dé il veut relancer
                if id_de in (1, 2, 3):
                    break
                print("Veuillez entrer un numéro de dé valide (1, 2, ou 3).")

            joueur.des[int(id_de) - 1].lancer()
            joueur.afficher_des() # On affiche les nouveaux dés
            joueur.score += self.combinaisons(joueur.des)
        elif nb_des_rejouer == 2:

            # Initialisations
            id_de_1 = 0
            id_de_2 = 0
            while True:
                if id_de_1 != id_de_2:
                    #On vérifie que les deux dés choisis sont différents
                    joueur.des[int(id_de_1) - 1].lancer()
                    joueur.des[int(id_de_2) - 1].lancer()
                    joueur.afficher_des()
                    break
                print("Les deux dés doivent être différents.")
                while True:
                    id_de_1 = int(input("\nChoix 1, dé 1, 2, ou 3? "))
                    #On demande au joueur quels dés il veut relancer
                    if id_de_1 in (1, 2, 3):
                        break
                    print("Veuillez entrer un numéro de dé valide (1, 2, ou 3).")

                while True:
                    id_de_2 = int(input("\nChoix 2, dé 1, 2, ou 3? "))
                    if id_de_2 in (1, 2, 3):
                        break
                    print("Veuillez entrer un numéro de dé valide (1, 2, ou 3).")
            joueur.score += self.combinaisons(joueur.des)
         # Calcul du score du joueur
        joueur.score += self.combinaisons(joueur.des)

if __name__ == "__main__":
    joueur1 = Joueur("Vasilis")
    joueur2 = Joueur("Yanis")
    jeu = Jeu()
    jeu.ajouter_joueur(joueur1)
    jeu.ajouter_joueur(joueur2)

    i = 1
    while True:
        if joueur1.score >= 10 or joueur2.score >= 10:
            break
        os.system('clear')
        print(f"********** Round {i} **********")
        print("\033[1m\nScore actuel\033[0m")
        jeu.afficher_scores()
        jeu.on_va_jouer(joueur1)
        jeu.on_va_jouer(joueur2)
        i+=1 # Incrementation du tour
    os.system('clear')
    print("\033[1m\nScore actuel\033[0m")
    jeu.afficher_scores()
    jeu.gagnant = max(jeu.joueurs, key=lambda joueur: joueur.score)
    print(f"\nLe gagnant est {jeu.gagnant.nom} avec un score de {jeu.gagnant.score}.")
