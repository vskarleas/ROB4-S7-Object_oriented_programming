import exercise1

if __name__ == "__main__":
    n = 10
    code = exercise1.Algebre() # Creating an instance of Algebre class
    somme_n = code.somme_n_first_numbers(n)
    factoriel_n = code.factoriel(n)
    print(f"La somme des premiers {n} entiers est {somme_n}.")
    print(f"La factorielle de {n} est {factoriel_n}.")