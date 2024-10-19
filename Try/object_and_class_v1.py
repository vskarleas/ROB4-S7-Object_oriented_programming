class Habitant(object):
    #dict_animal est des animaux possedes par l'habitant
    def __init__ (self, dict_animals:dict) -> None:
        self.__name = "Default"
        self.__age = 0
        self.__adresse = "Default addresse"
        self.__dict_animals = dict_animals

    
    #METHOD 1
    #Getters
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_adresse(self):
        return self.__adresse
    
    #Setters
    def set_name(self, name:str):
        self.__name = name

    def set_age(self, age:int):
        self.__age = age

    def set_adresse(self, adresse:str):
        self.__adresse = adresse

    def affichage_adresse(self): # affichera l'adresse de l'habitant
        print(self.get_name(), "habite à", self.get_adresse())

    # devra compter le nombre d'animaux de type animal que l'habitant possede
    def compte_animal(self, animal:str): 
        if animal in self.__dict_animals:
            return self.__dict_animals[animal]
        else:
            return "L'habitant ne possède pas cet animal"

if __name__ == "__main__":
    h = Habitant({"chien": 1, "chat": 2})

    h.affichage_adresse()

    h.set_name("Jane Doe")
    h.set_age(35)
    h.set_adresse("456 Elm St")

    h.affichage_adresse()
        
