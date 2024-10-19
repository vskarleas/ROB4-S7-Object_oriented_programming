"""User Interface"""


import cards
from random import shuffle, randint


# Colours declaration
def print_red(skk):
    """Prints a string in red."""
    print("\033[91m {}\033[00m".format(skk))

def print_green(skk):
    """Prints a string in green."""
    print("\033[92m {}\033[00m".format(skk))

def print_yellow(skk):
    """Prints a string in yellow."""
    print("\033[93m {}\033[00m".format(skk))

def print_light_purple(skk):
    """Prints a string in light purple."""
    print("\033[94m {}\033[00m".format(skk))

def print_purple(skk):
    """Prints a string in purple."""
    print("\033[95m {}\033[00m".format(skk))

def print_cyan(skk):
    """Prints a string in cyan."""
    print("\033[96m {}\033[00m".format(skk))

def print_light_gray(skk):
    """Prints a string in light gray."""
    print("\033[97m {}\033[00m".format(skk))

def print_black(skk):
    """Prints a string in black."""
    print("\033[98m {}\033[00m".format(skk))

class Question:
    """Classe pour poser des questions a l'utilisateur."""
    def __init__(self, question_text : str):
        self.question_text = question_text

    def ask_user(self) -> str:
        """Demande une reponse utilisateur."""
        user_answer = input(f"{self.question_text} ")
        return user_answer

def set_up_players(joueur1 : cards.Joueur, joueur2 : cards.Joueur) -> int:
    """Demande les noms des joueurs et le nombre de tours."""
    q1 = Question("Combien de tours voulez-vous jouer ?").ask_user()
    nb_tours = int(q1)

    q2_a = Question("Quel est le nom du Jouer 1 ?").ask_user()
    joueur1.change_name(q2_a)

    q2_b = Question("Quel est le nom du Jouer 2 ?").ask_user()
    joueur2.change_name(q2_b)

    return nb_tours

def initial_message(part_id, joueur1 : cards.Joueur, joueur2 : cards.Joueur, nb_tours : int):
    """Affiche le message d'initialisation de la partie."""
    print_cyan(f"\n============= Debut de la partie {part_id} =============")
    print(f"{joueur1.nom} et {joueur2.nom} commencent la partie! Vous avez {nb_tours} tours.\n")
    print("Les regles sont les suivantes : Une carte normale donne un nombre de points aléatoire compris entre 1 et 10. Une carte bonus edouble le score du joueur pour ce tour. La carte malus réduit le score du joueur de 5 points. La carte chance joute un nombre de points aléatoire entre -5 et 15.Il y a 56 cartes au total. Le tirage est aleartoire.")

def afficher_score(joueur1 : cards.Joueur, joueur2 : cards.Joueur):
    """Affiche le score des joueurs."""
    print(f"Score actuel : {joueur1.nom}: {joueur1.score} - {joueur2.nom}: {joueur2.score} \n")

def create_deck() -> list:
    """Crée une liste de cartes avec des instances de la classe Card."""
    cartes_normales = [cards.Normale()] * 30 # 30 normales
    cartes_bonus = [cards.Bonus()] * 6 # 6 bonus
    cartes_malus = [cards.Malus()] * 5 # 5 malus
    cartes_chance = [cards.Chance()] * 15 # 15 chance
    cartes = cartes_bonus + cartes_normales + cartes_malus + cartes_chance # Concatenate all the lists into one
    shuffle(cartes) # Shuffle the deck to ensure randomness
    return cartes

def continue_playing() -> bool:
    """Fonction qui demande au joueur s'il veut rejouer une partie."""
    question = Question("Voulez-vous rejouer une partie ? (O/N) ")
    user_answer = question.ask_user().upper()
    return user_answer == "O"

def who_wins(joueur1 : cards.Joueur, joueur2 : cards.Joueur, score1 : int, score2 : int) -> str:
    """Fonction qui determine qui gagne la partie en fonction des scores de chaque joueur."""
    if score1 > score2:
        print_yellow("Le gagnant est " + joueur1.nom)
    elif score1 < score2:
        print_yellow("Le gagnant est " + joueur2.nom)
    else:
        print_yellow("Egalite!")

def devenir_tricheur(joueur : cards.Joueur) -> cards.Joueur:
    """Fonction qui demande au joueur s'il veut devenir un tricheur."""
    if randint(0, 1) == 0: #50 % chance de recevoir la question devenir tricheur
        question = Question(f"{joueur.nom} voulez-vous devenir un tricheur? (O/N) ")
        user_answer = question.ask_user().upper()

        if user_answer == "O":
            joueur = cards.Tricheur(joueur)
            print(f"{joueur.nom} est devenu un tricheur.\n")
        else :
            joueur = cards.Joueur(joueur.nom, joueur.score)
            print(f"{joueur.nom} est devenu un joueur honnete.\n")

    return joueur
