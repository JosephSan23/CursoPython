## El poder de la repeticion BUCLES
El verdadero poder de la programacion es hacer tareas repetitivas en milisegundos. En Python hay 2 tipos de bucles:

------------------------------------------------------------------------
## WHILE
Se ejecuta mientras una condicion sea verdadera. Es ideal cuando no sabes cuantas veces se repetira algo
```python
intentos = 0
while intentos = 3:
    print("Intentando conectar...")
    intentos +=1
```

------------------------------------------------------------------------
## FOR
En Python el for se usa para recorrer una secuencia (una lista, una palabra, o un rango de numeros). Para contar numeros usamos la funcion range(inicio, fin).
```python
for i in range(1, 6):
    print(f"Vuelta numero {i}")
```