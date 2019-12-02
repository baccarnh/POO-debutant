# Exercice 2 :
Vous allez reprendre la classe précédemment crée et l’améliorer un peu. En effet, que se
passerait-t-il si notre classe city avait des dizaines d’attributs ? Cela deviendrait vite
chaotique. Impossible d’avoir autant d’attributs ? Réfléchissez 5 minutes à toutes les
caractéristiques d’une ville : nom, département, population, pays, code postal, nom des
habitants, date de création, dirigeant, personnages célèbres etc...
Vous trouverez dans le dossier qui vous a été donné un fichier cities.py qui contient une
liste de dictionnaires. Chaque dictionnaire représente une ville.
A vous de modifier votre classe ville pour que son constructeur accepte un dictionnaire en
argument et hydrate tous les attributs d’un coup.
Vous rajouterez une méthode show_information() qui affiche la carte d’identité complète
de la ville, c’est à dire l’ensemble de ses informations.
Dans votre fichier main.py réalisez ensuite une boucle pour instancier toutes les villes en
une fois et afficher leur carte d’identité
Pour allez plus loin, faites en sorte que si un de vos dictionnaires contient des clés qui ne
doivent pas être présentes dans votre objet alors l’attribut correspondant n’est pas créé.
Un indice, recherchez du côté des méthodes hasattr et setattr.
