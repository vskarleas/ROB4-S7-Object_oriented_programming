from multipledispatch import dispatch
from abc import ABC

class Habitant(ABC):
    def __init__(self, nom: str, age: int, adresse:str, animaux: dict) -> None:
        self.__age = age
        self.__nom = nom
        self.__adresse = adresse
        self.__animaux = animaux

    @dispatch()
    def affichage_adresse(self):
        print(self.__nom, " habite a ", self.__adresse)

    @dispatch(str)
    def affichage_adresse(self, cp):
        print(self.__nom, " habite a ", self.__adresse, cp)

    def compte_animal(self, animal):
        if animal not in self.__animaux.keys():
            return 0
        else:
            return self.__animaux[animal] 

    @property
    def age(self):
        return self.__age
    
    def get_age(self):
        return self.__age

    @age.setter
    def age(self, a):
        if a < 0:
            print("Error : age is negative")
        else:
            self.__age = a

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, n):
        self.__nom = n

    def calcul_retraite(self): # redefinition ici 
        return

class Adulte(Habitant):
    def __init__(self, nom: str, age: int, adresse:str, animaux: dict) -> None:
        if(age < 18):
            print("Error : Invalid Age ")
            return

        super().__init__(nom, age, adresse, animaux) # it takes the same signature with the classe that is herited from (in our case Habitant)

    def calcul_retraite(self):
        return 70 - self.age
    
class Enfant(Habitant):
    def __init__(self, nom: str, age: int, adresse:str) -> None:
        if(age > 18):
            print("Error : Invalid Age ")
            return

        super().__init__(nom, age, adresse, {}) # we do not pass a dict_animaux so we say by default that is VIDE (NILL)

    def calcul_retraite(self):
        return "You're not even working yet ! "
        

class Village:
    def __init__(self, n) -> None:
        self.nom = n
        self.liste_habitant = []

    def ajouter_compo(self, nom_h, age_h, adr_h, anim_h): # par composition. On cree l'habitant dans la fonction
        h = Habitant(nom_h, age_h, adr_h, anim_h)
        self.liste_habitant.append(h)
    
    def ajouter_agreg(self, h): # par agregation
        self.liste_habitant.append(h)

if __name__ == "__main__":
    animaux_alain = {"vache": 4, "mouton": 80, "chat":1}
    alain = Adulte("Alain", 50, "Cergy", animaux_alain)
    alain.affichage_adresse()
    alain.affichage_adresse('90010')
    print(alain.compte_animal("vache"))
    print(alain.compte_animal("chien"))

    print(f"{alain.nom} a pour le retrait {alain.calcul_retraite()} ans")
    pierre = Enfant("Pierre", 3, "Paris")
    print(pierre.calcul_retraite())
    v = Village("Paris")
    v.ajouter_agreg(alain)
    v.ajouter_agreg(pierre)

