# ############################################################################
# file_input exercise1.py
# Programmation Orienté Objet (POO) TP0 - Polytech Sorbonne - 2024/2025 - S7
# Auteurs : Vasileios Filippos Skarleas, Yanis Sadoun - Tous droits réservés.
# ############################################################################

"""This is the first exercise"""

class Algebre(): # pylint doesn't like 'object' in parenthesis
    """Implements various mathematical operations"""
    def __init__(self) -> None:
        self.n = 0

    def somme_n_first_numbers(self, m : int) -> int:
        """Returns the sum of n first numbers"""
        self.n = 0 # Neutral element of addition
        if m < 0: # Error handling
            raise ValueError("n has to be a positive number.")
        for i in range(0, m+1):
            self.n += i
        # self.n * (self.n+1) // 2 # Using the formula for the sum of an arithmetic series.
        return self.n

    def factoriel(self, m : int) -> int:
        """Returns the factorial of n."""
        self.n = 1 # Neutral element of multiplication
        if m < 0: # Error handling
            raise ValueError("n has to be a positive number.")
        if m in (0, 1):
            return 1
        for i in range(1, m+1):
            self.n *= i
        return self.n
