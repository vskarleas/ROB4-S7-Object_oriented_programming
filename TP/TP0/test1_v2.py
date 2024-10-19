# ############################################################################
# file_input test1_v2.py
# Programmation Orienté Objet (POO) TP0 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Yanis Sadoun - Tous droits réservés.
# ############################################################################

import exercise1
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2: # Checking if the number of arguments is correct
        raise ValueError(f"Usage error: You can pass only one argument. Try again!\n")
    else:
        n = int(sys.argv[1])
        code = exercise1.Algebre() # Creating an instance of Algebre class
        somme_n = code.somme_n_first_numbers(n)
        factoriel_n = code.factoriel(n)
        print(f"La somme des premiers {n} entiers est {somme_n}.")
        print(f"La factorielle de {n} est {factoriel_n}.")
