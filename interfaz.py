# Python Inicial [Python]
# Ejercicio integrador

# Autor: Inove Coding School
# Version: 2.0

imagenes = [
    '''    
    |   |
        |
        |
        |
        |
        =''',
    '''
    
    |   |
    O   |
        |
        |
        |
        =''',
    '''
    
    |   |
    O   |
    |   |
        |
        |
        =''',
    '''
    
    |   |
    O   |
   /|   |
        |
        |
        =''',
    '''
    
    |   |
    O   |
   /|\  |
        |
        |
        =''',
    '''
   
    |   |
    O   |
   /|\  |
    |   |
        |
        =''',
    '''
    
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =''',
    '''
    
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ='''
]

def dibujar(palabra_secreta, lista_letras_usadas, intentos_invalidos):
    '''Funcion que dibujar la interfaz del ahorcado
       Argumentos:
       - palabra_secreta [string]: Palabra secreta que debe adivinar el jugador
       - lista_letras_usadas [lista]: Lista de letras usadas hasta el momento
       - intentos_invalidos [int]: Cantidad de intentos invalidos:
                                     - 0 --> no hubo errores
                                     - 7 --> máxima cantidad de intentos inválidos
    '''
    # Armo la palabra oculta a mostrar
    palabra_oculta = ['_.'] * len(palabra_secreta)

    # Analizo si alguna letra utilizada está en la palabra secreta
    for letra in lista_letras_usadas:
        # Si la letra se utiliza en la palabra secreta, busco donde
        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                # Reemplazo en palabra oculta con la letra
                if palabra_secreta[i] == letra:
                    palabra_oculta[i] = letra + "."

    # Usar "min" para evitar dibujar por arriba
    # de lo cantidad de imagenes soportadas
    print(imagenes[min(intentos_invalidos, len(imagenes)-1)])
    print("Palabra secreta:")
    print("".join(palabra_oculta))
    print("Letras utilizadas:")
    print(lista_letras_usadas)
    return palabra_oculta

if __name__ == "__main__":
    # Probar la interfaz
    palabra_secreta = "palabra"
    lista_letras_usadas = ["a", "p", "l", "b", "r"]
    dibujar(palabra_secreta, lista_letras_usadas, 3)

