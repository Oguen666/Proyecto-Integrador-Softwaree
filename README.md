# Proyecto-Integrador-Softwaree

Práctica del uso y manejo de git para la materia de Ingeniería de Software 2026

# Reto Rigo:

We want to make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars.
Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2

### Solución

Primero sacamos la mayor cantidad de barras grandes que podemos usar sin pasarnos del objetivo (goal), luego calculamos
lo que falta después de usar las grandes actuales que tenemos actualmente, Y al final, comprobamos si tenemos más o
igual de cantidad de chocolates pequeños para cubrir lo restantes. Si es posible, se regresa la cantidad restante, si no
se regresa un -1.

