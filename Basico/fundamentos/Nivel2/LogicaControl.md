## Toma de desiciones (Logica de control)
El programa debe pensar. Para eso usamos los operadores de comparacion y las sentencias if.

------------------------------------------------------------------------
## Operadores de Comparacion
`==` (igual a)
`!=` (diferente a)
`>` (mayor que)
`<` (menor que)
`>=` (mayor o igual)
`<=` (menor o igual)

------------------------------------------------------------------------
## La estructura if - elif - else
En Python, la **Identacion** (el espacio al principio de la linea) es obligatoria. Define que el codigo pertenece al "bloque" de la decision.
```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
elif edad > 12:
    print("Eres un adolescente")
else:
    print("Eres un niño")

```

------------------------------------------------------------------------
## Operadores logicos
A veces necesitas evaluar dos cosas a la vez: 
`and`: Ambas deben ser verdad.
`or`: Al menos una debe ser verdad.
`not`: Invierte el valor (lo que es True pasa a False).