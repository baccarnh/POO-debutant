from cities import *
class City:
    """Classe définissant une ville caractérisée par :
    - son nom
    - son numero de departement"""

    def __init__(self, name, cities):
        """Constructeur de notre classe"""
        self.name = (cities[i])['name']
        self.departement = (cities[i])('departement')
        self.country=(cities[i])('country')
        self.population=(cities[i])('population')
        self.mayor=(cities[i])('mayor')
        self.capital=(cities[i])('capital')
        for i in (cities[i])['name']:
            i=City('name')
            for key_name, value_name in (cities[i]).items():
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


    def show_location(self):
        """ elle affiche une string dans le terminal nous indiquant le
        nom de la ville et sa localisation, par exemple elle affiche : « la ville X est dans le
        département Y »"""
        print("la ville de {} est dans le departement {}".format(self.name, self.departement))

    def change_location(self,new_nom, new_departement):
        """ elle attend deux paramètres, un nom sous forme de
        string et un département sous forme d’integer. Elle assigne à l’objet les nouvelles valeurs
        du nom et du département"""
        self.nom=new_nom
        print("la ville de {} change de nom et prend le {}".format(self.nom, new_nom))
        self.departement=new_departement
        print("la ville de {} change de numero de departement et prend le {}".format(self.departement, new_departement))



print(Paris.show_information())
