class City:
    """Classe définissant une ville caractérisée par :
    - son nom
    - son numero de departement"""

    def __init__(self, nom, departement):
        """Constructeur de notre classe"""
        self.nom = str(nom)
        self.departement = int(departement)

    def show_location(self):
        """ elle affiche une string dans le terminal nous indiquant le
        nom de la ville et sa localisation, par exemple elle affiche : « la ville X est dans le
        département Y »"""
        print("la ville de {} est dans le departement {}".format(self.nom, self.departement))

    def change_location(self,new_nom, new_departement):
        """ elle attend deux paramètres, un nom sous forme de
        string et un département sous forme d’integer. Elle assigne à l’objet les nouvelles valeurs
        du nom et du département"""
        self.nom=new_nom
        print("la ville de {} change de nom et prend le {}".format(self.nom, new_nom))
        self.departement=new_departement
        print("la ville de {} change de numero de departement et prend le {}".format(self.nom, new_nom))

Roubaix=City("Roubaix", 59)
Grenoble=City("Grenoble",38)
Antony=City("Antony",92)
