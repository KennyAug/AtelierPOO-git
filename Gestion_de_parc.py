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
            print("Voiture ajoiutée dans le parc")
    def sortirVoiture(self, voiture):
        if voiture in self.listedevoiture:
            self.listedevoiture.remove(voiture)
            print("Voiture enlever du parc")
            print(f"Place vides: {self.self.calculerNbrPlaceLibres()}")
        else:
            print("La voiture n'existe pas")
    def calculerNbrPlaceLibres(self):
        self.placeLibres = self.capacite - len(self.listedevoiture)
        print(f"Place libres: {self.placeLibres}")

p1 = Parc(67, "Esplanade", 3)

v1 = Voiture("AVME 2342", "TESLA", "Noir")
v2 = Voiture("EUW 1292", "BMW", "Vert")
v3 = Voiture("WEB 1305", "TOYOTA", "Gris")
