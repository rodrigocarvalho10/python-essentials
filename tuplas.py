# Atribuir sem parenteses
coord = 140, 200, 9

# atribuir com parenteses
coord = (140, 200, 9)

# desempacotar
x, y, z = coord

# ignorar elementos (ser� atribuito apenas o x)
x, *_ = coord

# pegar apenas o primeiro e o �ltimo elemento
x, *_, y = coord

# Verificar o tamanho
len(coord)
3

# Acessar via subscri��o pelo indice
coord[0]
140

# fatiar
coord[1:]
(200, 9)