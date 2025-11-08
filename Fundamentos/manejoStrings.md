# Manejo de strings

Multiples lineas

```python
multiples = """Hola
Mundo
Desde
Mi
casa"""

# Las triples comillas respetan el salto de linea y asi aparecera en consola
```

Para poder saber cuantas letras tiene una palabra se hace lo siguiente:

```python
palabra = "Murcielago"
print(len(palabra))
#Esto retorna la cantidad de letras en numero entero
```

Para saber si una palabra esta incluida o no en un texto

```python
texto = "Este curso es de python"
estaIncluida = "python" in texto

noEstaIncluida = "JavaScript" not in texto
#Esto retorna un true o un false
```

Convertir un texto de minuscula a mayuscula y viceversa

```python
# todo el texto en mayuscula
mayuscula = texto.upper()
# todo el texto en minuscula
minuscula = texto.lower()

print()
```

Eliminar los espacios del inicio o del final

```python
espacios = "     hola     "

sinEspacios = espacios.strip()
print(sinEspacios)
# Esto nos sirve por si tenemos contraseñas y no queremos que hayan espacios.
```
