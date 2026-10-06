# Proyecto-Integrador-Softwaree
Practica del uso y manejo de git para la materia de Ingenieria de Software 2026
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