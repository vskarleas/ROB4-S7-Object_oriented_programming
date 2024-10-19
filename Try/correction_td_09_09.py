liste_habitant = ["Alexis", "Alexandre", "Alain", "Abdel", "Aline"] #list

# liste_habitant.append(["Clarisse", "Camille"])
# liste_habitant.append("Clarisse")
# liste_habitant.append("Camille")
liste_habitant += ["Clarisse", "Camille"] # ou liste.extend # list

event_musique = {"Alexis", "Alain", "Aline", "Camille"} #ensmbles
event_danse = {"Alexis", "Alexandre", "Abdel", "Aline", "Clarisse", "Alain"}

print(liste_habitant)
del liste_habitant[2]
print(liste_habitant)

print(len(liste_habitant))

#Age
liste_age = []
for h in range(len(liste_habitant)):
    liste_age.append(h * 3 + 10)

print(liste_age)

for ind in range(len(liste_age)):
    if liste_age[ind] > 18:
        print(liste_habitant[ind])

# for habitant in liste_habitant:
#    liste_age += 30

maisons = [("Alain", "3 place Jussieu", 500),  ("Clarisse", "2 avenue Barbes", 15)] #list of tuples

def affichage_maison(maison):
    print(maison[0], " habite a ", maison[1], " avec ", maison[2], "m2")

for m in maisons:
    affichage_maison(m)

# transformation en liste
for ind in range(len(maisons)):
    maisons[ind] = list(maisons[ind])

maisons[1][1] = "L'Elysee"
maisons[1][2] = 600

for m in maisons:
    affichage_maison(m)

#Ensemble
#participe aux 2
print(event_musique & event_danse)
#au moins 1 des 2
print(event_danse | event_musique)
#uniquement musique
print(event_musique - event_danse)

event_musique.remove("Camille")
event_danse.add("Camille")
