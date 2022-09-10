![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

# ¡Proyecto Ahorcado! [Python]
En este repositorio contiene todos los materiales e instrucciones para poder realizar el proyecto de python inicial.

__NOTA__: Recomendamos haber realizado todos los ejercicios de práctica para poder realizar este proyecto.

## Recursos
- Contará con un archivo "palabras.csv" con las palabras secretas que se deben adivinar en el juego. Usted puede quitar/agregar/modificar las palabras secretas cuando ensaye su programa (si lo desea, sino dejar el archivo como está).
- Contará con un script de python "interfaz.py" el cual será el responsable de dibujar la interfaz del juego.

## Como comenzar
- Deberá crear un archivo "main.py" en el cual colocará todo el código necesario para realizar el proyecto.
- Dentro de ese archivo deberá importar las siguientes librerías ni bien comienza el archivo:
- - CSV
- - random
- - interfaz

- Luego deberá crear el bloque principal `if __name__ == "__main__":`. Dentro del bloque principal utilizará sus funciones y desarrollará el proyecto.
- Entre el lugar donde usted importó las librerías y generó el bloque pincipal, ahí irá creando sus funciones.

## Módulo de Interfaz
- En el archivo __interfaz.py__ se encuentra la función "dibujar" para dibujar en consola el ahorcado.
- Argumentos de la función dibujar:
  - palabra_secreta [string]: Palabra secreta que debe adivinar el jugador. Es la palabra que se leyó del CSV.
  - lista_letras_usadas [lista]: Lista de letras usadas hasta el momento, ingresadas por el usuario en cada intento.
  - intentos_invalidos [int]: Cantidad de intentos invalidos.
    - 0 --> no hubo errores
    - 7 --> máxima cantidad de intentos inválidos


## Bloque principal del programa
Dentro del bloque principal del programa deberá colocar la siguiente estructura de código:
```python
if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos = 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')
```

Tener en cuenta que todas las funciones que se utilizan en ese código no están implementadas aún, será usted quien la implemente y de eso se tratará el proyecto de este curso.

## Funciones del sistema
Dentro del archivo __main.py__ deberá implementar las siguientes funciones que utilizará luego el bloque main para armar el proyecto:

### Funcion "leer_palabra_secreta"
Encabezado de la función:
```python
def leer_palabra_secreta(csvfilename):
```

Entrada (argumentos):
- Esta función recibe por parámetro el nombre del archivo CSV que contiene la lista de posibles palabras secretas a adivinar.

Objetivo:
- La función deberá leer el CSV y recorrer todas la filas. Deberá armar una lista de palabras secretas.
- Una vez contenidas todas las palabras en una lista, utilizar la función `random.choice` para seleccionar aleatoriamente alguna de ellas. Almacenar esa palabra seleccionada en una varible.

Salida (return):
- La función deberá retornar la palabra secreta seleccionada por el random.choice.


### Funcion "pedir_letra"
Encabezado de la función:
```python
def pedir_letra(letras_usadas):
```

Entrada (argumentos):
- Esta función recibe por parámetro la lista de palabras utilizadas hastas el momento.

Objetivo:
- Deberá armar un bucle While infinito que se ejecute hasta que el procedimiento de pedir letra se complete exitosamente.
- Deberá pedirle al usuario que ingrese por "input" una letra nueva que no haya utilizado antes. Almacenar esa letra ingresada por "input" en una variable.
- La letra ingresada deberá transformarse a minúscula para evitar problemas.
- Utilizando la variable "letras_usadas" deberá verificar utilizando el operador "in" que esa letra es nueva y no se ha utilizado antes. Si se ha utilizado antes (es decir, existe dentro de "letras_usadas") el sistema no deberá salir del bucle y volverá al comienzo solicitando una letra nueva.
- Deberá verificar que la letra ingresada es solo una letra, es decir, verificar que no se ha ingresado más de una letra a la vez. Para eso utilice la función "len". Si se ha ingresado más de una letra junta, el sistema no deberá salir del bucle y volverá al comienzo solicitando una letra nueva.
- Si todas las condiciones se cumplen, deberá salir del bucle.
- Antes de que finalice la función debe guardar la variable "letra" que validó en la lista "letras_usadas" utilizando append.

Salida (return):
- La función deberá retornar la letra validada (return).


### Funcion "verificar_letra"
Encabezado de la función:
```python
def verificar_letra(letra, palabra_secreta):
```

Entrada (argumentos):
- Esta función recibe por parámetro la letra ingresada por el usuario y la palabra secreta a adivinar.

Objetivo:
- Deberá verificar si la variable "letra" es parte de la palabra secreta a divinar "palabra_secreta". Utilice el operador "in" para llevar a cabo esta verificación.

Salida (return):
- Si la letra pertenece a la palabra secreta a adivinar, esta función debe retornar True.
- Si la letra __no__ pertenece a la palabra secreta a adivinar, esta función debe retornar False.


### Funcion "validar_palabra"
Encabezado de la función:
```python
def validar_palabra(letras_usadas, palabra_secreta):
```

Entrada (argumentos):
- Esta función recibe por parámetro las letras ingresada hasta el momento por el usuario "letras_usadas" y la palabra secreta a adivinar "palabra_secreta".

Objetivo:
- Deberá verificar si todas las letras de la "palabra_secreta" se encuentran contenidas/disponible en la lista de letras usadas "letras_usadas".
- Para esto deberá armar un bucle que recorra todas las letras de "palabra_secreta". Con el operador "in" debe verificar si cada letra de la palabra secreta existe en la lista "letras_usadas".
- Con que una letra de la palabra secreta no exista en las letras usadas, se debe terminar el bucle e indicar que aún no se ha adivinado la palabra secreta.

Salida (return):
- Si se avidinó por completo la palabra secreta, esta función debe retornar True.
- Si __no__ se avidinó por completo la palabra secreta, esta función debe retornar False.


## Puntos extra (bonus track)
En caso que desee mejorar el sistema puede realizar las siguientes optimizaciones. No es necesario realizar esta parte para aprobar, es un plus simplemente ^_^:
- Robustecer la función "pedir_letra" para que no explota en caso de ingresarse un número.
- Robustecer la función "pedir_letra" para validar que el dato ingresado es efecticamente una letra del abecedario (evitar números, símbolos, espacios).
