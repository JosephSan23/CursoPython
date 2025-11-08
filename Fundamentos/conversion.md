# Manipulacion y conversion de tipos numericos

Python permite saber que tipo de dato es el valor de una variable con lo siguient:

```python
print(type(nombre_varible))
# imprime el tipo de dato
```

Para hacer una conversion de variable se le llama casteo.

```python
nueva_variable = float(variable_antigua)
# Si el valor antes era un entero ahora sera un numero decimal

flotante = int(entero)
# Esto lo que hace es quitar el decimal si es 2.5 se convertiria en 2
```

Para los numeros complejos se puede pasar otro tipo de dato a complejo pero no de complejo a otro

Numeros aleatorios

```python
import random

print(random.randrange(1, 10)) # Sale un numero aleatorio entre 1 y 9
```
