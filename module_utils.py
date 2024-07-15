def addition(a, b):
    return a + b


if __name__ == "__main__":
    print(addition(4, 5))

"""

L'expression if __name__ == "__main__": est couramment utilisée en Python pour 
indiquer que le bloc de code suivant doit être exécuté uniquement lorsque le fichier 
est exécuté en tant que script principal, et non lorsqu'il est importé en tant que module dans un autre fichier.

Explication de __name__
__name__ :
__name__ est une variable spéciale en Python. Elle est définie par l'interpréteur Python.
Lorsque le fichier Python est exécuté, l'interpréteur assigne la chaîne __main__ à la variable __name__.
Lorsque le fichier Python est importé en tant que module dans un autre fichier, __name__ est assigné au nom du fichier/module.

"""
