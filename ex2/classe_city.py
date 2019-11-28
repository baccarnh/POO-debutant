class City:
    """Classe définissant une ville caractérisée par :
    - son nom
    - son numero de departement"""

    def __init__(self,cities):
        """Constructeur de notre classe"""
        self.name = None
        self.departement = None
        self.country= None
        self.population= None
        self.mayor=None
        self.capital=None

        for key_name, value_name in cities.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)

    def show_information(self):
        text ="------------------\n \
        name: {}\n \
        departement: {}\n \
        country: {}\n \
        population: {}\n \
        mayor: {}\n \
        capital: {}\n"

        print(text.format(self.name, self.departement, self.country, self.population, self.mayor, self.capital))
