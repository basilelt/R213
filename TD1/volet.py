longueur = 2.4
lame_ferme = 0.036
lame_deploye = 0.04
diametre = 0.06

nb_lame_ferme = longueur / lame_ferme
print(f"{nb_lame_ferme} lames « entières » sont nécessaires pour le tablier en position fermé.")

longueur_enroule = nb_lame_ferme * lame_deploye
print(f"La longueur à enrouler est donc de {round(longueur_enroule, 2)}m")

n_tour = int(input("Nombre de tour: "))
for i in n_tour:
    d = dia