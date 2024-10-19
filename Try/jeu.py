"""Program created to demonstrate the various ways to add items to a list in Python and test out
 different methods as well as respond to different questions on the exercises 
 found on the 1st diaporama of the lecture"""

base = ["George", "Vasilis", "Nick", "Jas", "John"]

# Adding two more people on the list
## Option 1
extra = ["Alexia", "Fin"]
base = base + extra #in order to add two more people in the list

## Option 2
base.extend(["Salome", "Josephine"]) # concantenating the lists

## Option 3
base += ["Olivier", "Sarah"] #in order to add two more people in the list

## Option 4
base.append("Neos")
base.append("Allos") #!!! One argument for append

print(base)


# Printing the length of the list
print(len(base))


# Removing a person
base.pop(len(base)-1) #Deleting the latest item added to the list
del(base[3]) # άλλος τρόπος να το κάνεις
print(base)
print(len(base))


# Age list
ages = []
for l in range(len(base)):
    ages.append(l * 3 + 10) # There is no specific rule here

print(ages)


# Filtering liste
over_18 = []
for l in enumerate(base):
    if ages[l] > 18:
        over_18.append(base[l])

print(over_18)


def new_born(base_list, ages_list):
    if len(base_list) > len(ages_list):
        ages_list.append(1) # we consider that this person is a newborn

# Adding a new born
base.append("new")
print(base)
new_born(base, ages)
print(ages)


# Listes non modifiables
maisons = [("Clarise", "3 place Jussie", 500),
           ("Jas", "5 rue de la paix", 1000), ("John", "10 rue de la paix", 2000)]

for m in enumerate(maisons):
    print(maisons[m][0], "habite au",
          maisons[m][1], "et paye", maisons[m][2], "euros") # THAT IS VERY IMPORTANT SYNTAX

# for k in range(len(maisons)):
#     print(maisons[k])

## Affichage des maisons seulemnt
def affiche_maisons(maisons_list):
    for k in enumerate(maisons_list):
        print(maisons_list[k][0], "habite au", maisons_list[k][1])

affiche_maisons(maisons)

print("======================================")
## Exercise evenement
event_musique ={"Alexis", "Giorgos", "Maria", "Giannis"} # Those are ensembles en egeneral
event_dance = {"Maria", "Giorgos", "John", "Jas"}

#Affichez les habitants qui participent aux deux événements.
print(event_musique.intersection(event_dance))
# ou encore
print(event_musique & event_dance)

#Affichez les habitants qui participent à au moins un des événements.
print(event_musique.union(event_dance))
# ou encore
print(event_musique | event_dance)

#Affichez les habitants qui participent uniquement à l'événement de musique.
print(event_musique.difference(event_dance))
# our encore
print(event_musique - event_dance)

#Un habitant décide de rejoindre l’événement de danse. Ajoutez son nom à event_danse.
event_dance.add("Salome")

#Un autre habitant décide de ne plus participer à l’événement de musique.
# Retirez son nom de event_musique.
event_musique.remove("Alexis")
print("======================================")
