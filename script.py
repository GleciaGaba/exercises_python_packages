import mon_module

print(mon_module.a)

"""
En Python, on peut créer des modules et les importer à l'intérieur d'un autre fichier.

Il faut faire attention aux noms des modules, car il existe des modules réservés à Python. 
Si on crée un module avec le même nom qu'un module réservé à Python, on va simplement écraser 
le module réservé avec celui qu'on a créé.

"""


def addition(a, b):
    return a + b


print(addition(4, 5))
