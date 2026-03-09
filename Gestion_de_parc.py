class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    def affiche_info(self):
        print(f"La matricule: {self.matricule} la marque: {self.marque} la couleur: {self.couleur}")

class Parc:
    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listedevoiture = []
    def entrerVoiture(self, voiture):
        if voiture in self.listedevoiture:
            print("Voiture existe déjà")
        elif len(self.listedevoiture) >= self.capacite:
            print("Pas de [lace dispo")
        else:
            self.listedevoiture.append(voiture)