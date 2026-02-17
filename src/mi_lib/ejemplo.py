def saluda(nombre):
  print("¡Hola {}!".format(nombre))
  filas = 5
columnas = 5

muro = ((0,1), (0,2), (0,3), (0,4),
        (1,1),
        (2,1), (2,3),
        (3,3),
        (4,0), (4,1), (4,2), (4,3))

laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]

for f, c in muro:
    laberinto[f][c] = 'X'

laberinto[4][4]= 'S'

for fila in laberinto:
    print(fila)
