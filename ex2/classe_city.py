class City:
    """Classe définissant une ville caractérisée par :
    - son nom
    - son numero de departement"""

    def __init__(self,dico):
        """Constructeur de notre classe"""
        self.name = None
        self.department = None
        self.country= None
        self.population= None
        self.mayor=None
        self.capital=None
        self.hydratation(dico)

    def hydratation(self, dico):
        for key_name, value_name in dico.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)

    def show_information(self):
        text="------------------\n \
        name: {}\n \
        department: {}\n \
        country: {}\n \
        population: {}\n \
        mayor: {}\n \
        capital: {}\n"

        print(text.format(self.name, self.department, self.country, self.population, self.mayor, self.capital))
