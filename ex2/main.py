from cities import *
from classe_city import *

for i in cities:
    i=City(i)
    City.show_information(i)
    i.show_information() #second method
