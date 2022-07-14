import random 

def generar_contrasena():
    ## Genero 4 listas de simbolos
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', 
    '!', '[', '{', '(', ')', '}', ']', ',', ';',
    '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = mayusculas + minusculas + simbolos + numeros 

    contrasena = []
    for i in range(10):
        caracter_random = random.choice(caracteres)   ## with choice I choose a character from the list caracteres
        contrasena.append(caracter_random)
    contrasena = ''.join(contrasena)                  ## convert a list to string 
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contrasena es: ' + contrasena)
    print('Recuerda no decirsela a nadie')
if __name__ == '__main__':
    run()


