# Proyecto-Integrador-Softwaree

Practica del uso y manejo de git para la materia de Ingenieria de Software 2026

# Reto Martin:

Given 3 int values, a b c, return their sum.
However, if one of the values is 13 then it does not count towards
the sum and values to its right do not count. So for example,
if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1

### Solución

Se guardaron los argumentos en una lista y se recorrió con un `for`.
En cada iteración, si el valor es `13` se rompe el bucle con `break`;
en caso contrario, se suma al resultado.

---

# Reto Owen:

Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3

### Solución

Lo que hice fue crear primero la funcion principal no_teen_sum(a, b, c) que se encarga de sumar los tres numeros, pero pasando cada uno por una funcion ayudante llamada fix_teen
la funcion fix_teen(n) recibe un numero y revisa si esta en el rango entre 13 y 19. Si está en ese rango y no es ni 15 ni 16, lo convierte en 0. Si es cualquier otro numero lo deja tal cual.

---

# Reto Baruch:

You are driving a little too fast, and a police officer stops you.
Write code to compute the result, encoded as an int value:
0=no ticket, 1=small ticket, 2=big ticket.

If speed is 60 or less, the result is 0.
If speed is between 61 and 80 inclusive, the result is 1.
If speed is 81 or more, the result is 2.
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0

### Solución

Se creó la función `caught_speeding`, que recibe la velocidad y un valor booleano que indica si es cumpleaños. Si es cumpleaños, se restan 5 a la velocidad para aplicar la tolerancia adicional. Después, mediante condicionales `if`, `elif` y `else`, se determina el resultado: 0 si no hay multa, 1 si corresponde una multa pequeña y 2 si corresponde una multa grande.
