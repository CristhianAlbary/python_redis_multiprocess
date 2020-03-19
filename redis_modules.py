from time import sleep

# def print_as_function(argument):
#   sleep(2)
#   return argument

def cria_matriz(linhas, colunas):
  A = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      linha = linha + [random.randint(1, 10)]
    A = A + [linha]
  return A

def multiplica_linha_coluna(queue, queue_resultados, matrizA, matrizB):
    while True:
        i, j = queue.get()
        valor = 0
        for k in range(len(matrizB)):
            valor = valor + matrizA[i][k] * matrizB[k][j]
        queue.task_done()
        queue_resultados.put((i, j, valor))