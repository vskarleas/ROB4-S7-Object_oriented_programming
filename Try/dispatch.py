from multipledispatch import dispatch

class Habitant(object):
    #dict_animal est des animaux possedes par l'habitant
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
    