from abc import ABC, abstractmethod #Αυτό είναι απαραίτητο για να δουλεύει το pass

class Habitant(object):
    def __init__ (self):
        self.__name = "Default"
        self.__age = 0
        self.__adresse = "Default addresse"
        self.__dict_animals = {}
        
    #METHOD 2
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name:str):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age:int):
        if age < 0:
            print("L'age ne peut pas être négatif.")
        else:
            self.__age = age
    
    @property
    def adresse(self):
        return self.__adresse
    
    @adresse.setter
    def adresse(self, adresse:str):
        self.__adresse = adresse

    @property
    def dict_animals(self):
        return self.__dict_animals
    
    @dict_animals.setter
    def dict_animals(self, dict_animals:dict):
        self.__dict_animals = dict_animals

    #Things happening here
    def affichage_adresse(self): # affichera l'adresse de l'habitant
        print(self.name, "habite à", self.adresse)

    # devra compter le nombre d'animaux de type animal que l'habitant possede
    def compte_animal(self, animal:str): 
        if animal in self.__dict_animals:
            return self.__dict_animals[animal]
        else:
            return "L'habitant ne possède pas cet animal"
        
    #Εδω πέρα κάνουμε abstraite την fonction calcul_nombre_annee_avant_retraite
    def calcul_nombre_annee_avant_retraite(self):
        pass

        
class Enfant(Habitant):
    def __init__(self):
        super().__init__()

        if (self.age > 18):
            print("Error: Invalid age")
            return

    def calcul_nombre_annee_avant_retraite(self):
        print("L'habitant est encore trop jeune pour la retraite.")


class Adulte(Habitant):
    def __init__(self):
        super().__init__()

    def calcul_nombre_annee_avant_retraite(self):
        if self.age >= 65:
            print("L'habitant est déjà en retraite.")
        else:
            annee_restante = 65 - self.age
            print(f"L'habitant reste {annee_restante} ans avant de retraire.")

def main():
    enfant = Enfant()
    adulte = Adulte()

    #Κάνουμε χρήση της δεύτερης μεθόδου για την ασφάλεια των arguments
    enfant.name = "John"
    enfant.age = 12
    enfant.adresse = "123 Main St"
    enfant.dict_animals = {"chien": 1, "chat": 2}

    adulte.name = "Alice"
    adulte.age = 60
    adulte.adresse = "456 Elm St"
    adulte.dict_animals = {"chien": 2, "chat": 3}

    enfant.affichage_adresse()
    print(enfant.compte_animal("chien"))
    enfant.calcul_nombre_annee_avant_retraite()

    print("=============================")

    adulte.affichage_adresse()
    print(adulte.compte_animal("chat"))
    adulte.calcul_nombre_annee_avant_retraite()

main()
