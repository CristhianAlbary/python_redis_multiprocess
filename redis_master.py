from time import sleep
from redis import Redis
from rq import Queue
from redis_modules import print_as_function

def cria_matriz(linhas, colunas):
  A = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      linha = linha + [random.randint(1, 10)]
    A = A + [linha]
  return A

if __name__ == "__main__":
  print "Initializing redis master"
  redis_conn = Redis(host='127.0.0.1',port=8100)
  queue_jobs = Queue('my_queue', connection=redis_conn)

  matrizA = cria_matriz(linhas, colunas)
  matrizB = cria_matriz(linhas, colunas)
  matrizC = numpy.zeros(shape=(linhas,colunas))

  queue = Queue('my_queue', connection=redis_conn)
  queue_resultados('my_queue_result', connection=redis_conn)

  jobs = []
  for i in range(2):
    job = queue_jobs.enqueue(multiplica_linha_coluna, args=(queue, queue_resultados, matrizA, matrizB), "realizando trabalho {0}".format(i))
    jobs.append(job)

  for i in range(len(matrizA)):
    for j in range(len(matrizA[0])):
      queue.put((i, j))

  queue.join()

  for job in jobs:
    while job.result is None:
      i, j, valor = job.result
      matrizC[i][j] = valor

  print("{}: Resultado:{}".format(time.strftime('%c'), matrizC))
