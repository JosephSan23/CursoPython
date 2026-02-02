En python el codigo se ejecuta de arriba hacia abajo, Objeto y referencia.
```python
puntaje = 100
```
100 es un objeto de tipo entero que vive en la memoria del PC, y puntaje es el nombre que apunta hacia el. Si luego haces puntaje = "Excelente", la etiqueta se despega del numero y se pega a un texto. Esto se llama Tipado Dinamico.

- Los 4 pilares de Datos (primitivos):
1. Integers (int) = Numeros enteros (1, -5, 100).
2. floats (float) = Numeros con decimales (3.14, -0.001).
3. Strings (str) = Texto puro. Se definen con comillas simples ' ' o dobles " ".
4. Booleans (bool) = Solo dos valores: True o False. (La primera letra siempre es en mayuscula)

- Operaciones e interaccion basica.
Para que un programa sea util, debe procesar datos y comunicarse.
1. Entrada: Para pedirle datos al usuario debemos usar input("Mensaje"). Importante: Todo lo que entra por input es tratado como texto (str).
2. Conversion (casting): Si pides un numero, debes convertirlo: int(input("Mensaje")).
3. Salida: Usamos print() para que aparezca en consola. La forma mas moderna y limpia de usarlo es con f-strings:
```python
nombre = "Mundo"
print(f"Hola {nombre}") # La 'f' permite meter variables entre llaves
```




