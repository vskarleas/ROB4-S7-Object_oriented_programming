"""Main program for the gane"""
from cards import Joueur, distribute_card
import ui

if __name__ == "__main__":
    # Création des joueurs
    joueur1 = Joueur()
    joueur2 = Joueur()

    # Initialisation de la partie
    part_id  = 1

    end_game = False
    while not end_game:
        cartes = ui.create_deck()
        # Initiliasation of the game

        nb_tours = ui.set_up_players(joueur1, joueur2)
        ui.initial_message(part_id, joueur1, joueur2, nb_tours)

        for i in range (nb_tours):
            ui.print_green(f"\n****** Tour No {i+1} : Nombre de cartes restants {len(cartes)} ******")

            # Joueur 1 joue une carte
            input(f"{joueur1.nom} appui sur n'importe que une touche pour tirer une carte...")
            carte1 = distribute_card(cartes)
            joueur1.jouer_carte(carte1)
            ui.print_light_gray(f"{joueur1.nom} joue {carte1.id_str}\n Effet: {carte1.effet}\n")

            # Joueur 2 joue une carte
            input(f"{joueur2.nom} appui sur n'importe que une touche pour tirer une carte...")
            carte2 = distribute_card(cartes)
            joueur2.jouer_carte(carte2)
            ui.print_light_gray(f"{joueur2.nom} joue {carte2.id_str}\n Effet: {carte2.effet}\n")

            #carte2 = distribute_card(cartes)
            ui.print_red("------------- Scores ---------------------")
            ui.afficher_score(joueur1, joueur2)


            joueur1 = ui.devenir_tricheur(joueur1)
            joueur2 = ui.devenir_tricheur(joueur2)

        ui.who_wins(joueur1, joueur2, joueur1.score, joueur2.score)
        if not ui.continue_playing():
            end_game = True
