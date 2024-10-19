"""Trying out the first steps at the object oriented programming in Python"""

class Habitant(object):
    #dict_animal est des animaux possedes par l'habitant
    def __init__ (self, name:str, age:int, adresse:str, dict_animals:dict) -> None:
        self.name = name
        self.age = age
        self.adresse = adresse
        self.dict_animals = dict_animals

    def affichage_adresse(self): # affichera l'adresse de l'habitant
        print(self.name, "habite à", self.adresse)

    # devra compter le nombre d'animaux de type animal que l'habitant possede
    def compte_animal(self, animal:str): 
        if animal in self.dict_animals:
            return self.dict_animals[animal]
        else:
            return "L'habitant ne possède pas cet animal"
        
class Village(object):
    def __init__(self, name:str, owners:list) -> None:
        self.name = name
        self.owners = owners
    def ajouter_habitant_par(self, habit: Habitant) -> None:
        """
        Ajoute un habitant à la liste des habitants du village.

        Parameters:
        habit (Habitant): L'instance de la classe Habitant à ajouter au village.

        Returns:
        None: La fonction ne renvoie aucune valeur. Elle modifie directement 
        l'attribut 'owners' de l'instance de la classe Village.
        """
        self.owners.append(habit)

    def ajouter_habitant_par(self, habit:Habitant):
        self.owners.append(habit)

class Vilage_pro(object):
    def __init__(self, n) -> None:
        self.name = n
        self.liste_habitants = [] #Δεν το περνάνε από variable. Απλά υπάρχει και η python θα προσθέσει ή αφαιρέσει πράγματα ανάλογα

    def ajouter_habitant_par_composition(self, nom_h, age_h, adresse_h, dict_animals_h):
        h = Habitant(nom_h, age_h, adresse_h, dict_animals_h)
        self.liste_habitants.append(h)

    def ajouter_habitant_par_aggregation(self, habitant: Habitant): # Η μόνη διαφορά με παραπάνω είναι ότι Habitant περνιέται ήδη φτιαγμένο
        self.liste_habitants.append(habitant)

#if __name__ == "__main__":  # exécution uniquement si ce script est exécuté directement
def main():
    habitant_1 = Habitant("John Doe", 30, "123 Main St", {"chien": 1, "chat": 2})
    habitant_1.affichage_adresse()
    print(habitant_1.compte_animal("chat"))
    print(habitant_1.compte_animal("tortue"))

    print("=============================")


    # Création de deux autres habitants
    habitant_2 = Habitant("Jane Doe", 25, "456 Elm St", {"chien": 2, "tortue": 1})
    habitant_3 = Habitant("Alice Doe", 40, "789 Oak St", {"chat": 3, "tortue": 2})

    village_owners = [habitant_1, habitant_2] # liste des habitants du village

    # Création du village et ajout des habitants
    village_1 = Village("Mon Village Test", village_owners)
    print("Nombre d'habitants dans le village:", len(village_1.owners), "| habitant:", end=" ")
    for i in range(len(village_1.owners)):
        if i < len(village_1.owners) - 1:
            print(village_1.owners[i].name, end=", ")
        else:
            print(village_1.owners[i].name, end=".\n")

    village_1.ajouter_habitant_par(habitant_3)
    print("Nombre d'habitants dans le village APRES:", len(village_1.owners), "| habitant:", end=" ")
    for i in range(len(village_1.owners)):
        if i < len(village_1.owners) - 1:
            print(village_1.owners[i].name, end=", ")
        else:
            print(village_1.owners[i].name, end=".\n")

    print("=============================")
    village_2 = Vilage_pro("Mon Village Pro")
    village_2.ajouter_habitant_par_composition("John Doe", 30, "123 Main St", {"chien": 1, "chat": 2})
    village_2.ajouter_habitant_par_aggregation(habitant_2)

    print("Nombre d'habitants dans le village APRES:", len(village_2.liste_habitants), "| habitant:", end=" ") # by default end is at \n, here we say that it should be a SPACE
    for i in range(len(village_2.liste_habitants)):
        if i < len(village_2.liste_habitants) - 1:
            print(village_2.liste_habitants[i].name, end=", ")
        else:
            print(village_2.liste_habitants[i].name, end=".\n")

    print("=============================")
    print(village_2.liste_habitants[0].name, "habite à", village_2.liste_habitants[0].adresse)
    del habitant_2
    print(village_2.liste_habitants[1].name, "habite à", village_2.liste_habitants[1].adresse)
            
main()


