# Proyecto-Integrador-Softwaree

Practica del uso y manejo de git para la materia de Ingenieria de Software 2026

## Reto Martin:

Given 3 int values, a b c, return their sum.
However, if one of the values is 13 then it does not count towards
the sum and values to its right do not count. So for example,
if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1

#### Solución

Se guardaron los argumentos en una lista y se recorrió con un `for`.
En cada iteración, si el valor es `13` se rompe el bucle con `break`;
en caso contrario, se suma al resultado.

---
