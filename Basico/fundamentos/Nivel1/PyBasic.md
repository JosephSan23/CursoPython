## Ejecución y referencia en Python

En Python el código se ejecuta de **arriba hacia abajo**, Objeto y
referencia.

``` python
puntaje = 100
```

100 es un objeto de tipo entero que vive en la memoria del PC, y
**puntaje** es el nombre que apunta hacia él.\
Si luego haces:

``` python
puntaje = "Excelente"
```

la etiqueta se despega del número y se pega a un texto.\
Esto se llama **Tipado Dinámico**.

------------------------------------------------------------------------

## Los 4 pilares de Datos (primitivos)

1.  **Integers (int):** Números enteros (`1`, `-5`, `100`)
2.  **Floats (float):** Números con decimales (`3.14`, `-0.001`)
3.  **Strings (str):** Texto puro. Se define con comillas simples `' '`
    o dobles `" "`
4.  **Booleans (bool):** Solo dos valores: `True` o `False` (siempre con
    mayúscula)

------------------------------------------------------------------------

## Operaciones e interacción básica

Para que un programa sea útil, debe procesar datos y comunicarse.

### 1. Entrada

Para pedir datos al usuario usamos:

``` python
input("Mensaje")
```

Importante: **todo lo que entra por input es texto (`str`)**.

### 2. Conversión (casting)

Si pides un número, debes convertirlo:

``` python
int(input("Mensaje"))
```

### 3. Salida

Usamos `print()` para mostrar texto en consola.\
La forma más moderna y limpia es con **f-strings**:

``` python
nombre = "Mundo"
print(f"Hola {nombre}")  # La 'f' permite meter variables entre llaves
```

La `f` significa *formato en cadenas*.
