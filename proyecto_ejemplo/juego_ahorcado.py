PALABRAS = []


def ahorcado(palabra):
    pass


def palabra_aleatoria(PALABRAS):
    from random import choice

    PALABRAS = PALABRAS
    palabra = choice(PALABRAS)

    ahorcado(palabra)
    


def archivo():
    with open("./files/palabras.txt", "r", encoding="utf-8") as f:
        for palabra in f:
            PALABRAS.append(palabra.rstrip())
    palabra_aleatoria(PALABRAS)


if __name__ == "__main__":
    archivo()