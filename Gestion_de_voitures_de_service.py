class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
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
