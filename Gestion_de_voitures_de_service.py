class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voiturees = None
        self.voitureService = None
    def afficherInfos(self):
        print(f"L'employé: {self.prenom, self.nom}")
        print(f"Numéro de permis : {self.numeroPermis}")
        if self.voitureService:
            print("La voiture est attribuée: ")
            self.voitureService.afficherInfos()
        else:
            print("Pas de voiture attribuée")
    def affecterVoiture(self, voiture):
        if self.voitureService:
            print("L'employé possède déjà une voiture")
            return
        if self.voiturees:
            print("La voiture est attribuée: ")
            return
        self.voitureService = voiture
        voiture.voiturees = self
    def retirerVoiture(self):
        if self.voitureService == None:
            print("Cet employe n'a pas de voiture")
            return
        self.voitureService.voiturees = None
        self.voitureService = None
class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.voiturees = None
    def afficherInfos(self):
        print(f"Voiture: {self.marque}, Matricule : {self.matricule}, Année : {self.annee}, Kilometrage : {self.kilometrage}")
        if self.voiturees:
            print(f"Le chauffeur est : {self.voiturees.prenom}, {self.voiturees.nom}")
        else:
            print("Aucun chauffeurs")

e1 = Employe("B932BE9W", "JEAN", "MARC")
e2 = Employe("B932034E", "JEANNE", "CHARLES")
v1 = Voiture("BI827389", 2010, "BMW", 60000)
v2 = Voiture("WEIB2923", 2025, "BYD", 600)

e1.afficherInfos()
v1.afficherInfos()
e1.affecterVoiture(v1)
e1.afficherInfos()
e1.retirerVoiture()

