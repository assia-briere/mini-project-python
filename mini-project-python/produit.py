from abc import ABC, abstractproperty

class ProduitInterface(ABC):
    @abstractproperty
    def ram(self):
        pass

    @abstractproperty
    def disque(self):
        pass

    @abstractproperty
    def processeur(self):
        pass

    @abstractproperty
    def nom(self):
        pass

    @abstractproperty
    def marque(self):
        pass

    @abstractproperty
    def cv(self):
        pass
###############################################################
#classe PC qui implémente l'interface ProduitInterface
class PC(ProduitInterface):
    def __init__(self, nom, processeur, ram, disque):
        self._nom = nom
        self._processeur = processeur
        self._ram = ram
        self._disque = disque

    @property
    def ram(self):
        return self._ram

    @property
    def disque(self):
        return self._disque

    @property
    def processeur(self):
        return self._processeur

    @property
    def nom(self):
        return self._nom

    @property
    def marque(self):
        return "Non spécifiée"

    @property
    def cv(self):
        return 0

#  Voiture qui implémente l'interface ProduitInterface
class Voiture(ProduitInterface):
    def __init__(self, nom, marque, cv):
        self._nom = nom
        self._marque = marque
        self._cv = cv

    @property
    def ram(self):
        return 0

    @property
    def disque(self):
        return 0

    @property
    def processeur(self):
        return "Non spécifié"

    @property
    def nom(self):
        return self._nom

    @property
    def marque(self):
        return self._marque

    @property
    def cv(self):
        return self._cv
#######################################################################################""
class Produit:
    def __init__(self, nom, prix, description, interface):
        self._nom = nom
        self._prix = prix
        self._description = description
        self._interface = interface

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nouveau_nom):
        self._nom = nouveau_nom

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, nouveau_prix):
        if nouveau_prix >= 0:
            self._prix = nouveau_prix
        else:
            print("Le prix ne peut pas être négatif.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, nouvelle_description):
        self._description = nouvelle_description

    @property
    def interface(self):
        return self._interface  # Getter for the interface

    def afficher_info(self):
        print(f"Nom: {self.nom}")
        print(f"Prix: {self.prix}")
        print(f"Description: {self.description}")
        print("Interface:")
        print(f"RAM: {self.interface.ram}")
        print(f"Disque: {self.interface.disque}")
        print(f"Processeur: {self.interface.processeur}")
        print(f"Marque: {self.interface.marque}")
        print(f"CV: {self.interface.cv}")

# Example of creating an interface object and a product with that interface
interface_pc = PC("Ordinateur portable", "Intel Core i7", 16, 512)
produit1 = Produit("PC Portable", 999.99, "Un ordinateur portable puissant", interface_pc)
voiture = Voiture("Toyota Camry", "Toyota", 180)
produit2 = Produit("voiture ", 4, "voiture  puissant", voiture)
# Display product information
produit2.afficher_info()