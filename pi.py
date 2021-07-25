import statistics
import timeit
import threading
global numExct
global nopi
global tempoExct
from time import sleep

nopi = list()
numExct = 5
tempoExct = []


def espace():
    print("\n\n\n")


class calcpi(threading.Thread):
    def __init__(self, numtermos, ninicial):
        self.numtermos = numtermos
        self.ninicial = ninicial
        self.pi = float(0)
        threading.Thread.__init__(self)

    def run(self):
        for n in range(self.ninicial, self.ninicial + self.numtermos, 1):
            self.pi += float(pow(-1, n) / ((2 * n) + 1))
        self.pi *= float(4)

print("---CALCULO DE PI---")
sleep(1)
numtermos = int(input("n: "))
numthreads = int(input("threads: "))

pi = []
divisao = int(numtermos / numthreads)

for i in range(0, numExct):
    inicio = timeit.default_timer()
    threads = []
    ninicial = 0

    for j in range(0, numthreads, 1):
        thread = calcpi(divisao, ninicial)
        threads.append(thread)
        threads[j].start()
        ninicial = ninicial + divisao

    pi.append(0)

    for j in range(0, len(threads), 1):
        threads[j].join()
        pi[i] += float(threads[j].pi)

    fim = timeit.default_timer() - inicio
    print(fim, "s")
    tempoExct.append(fim)

espace()
print(f"Numero de termos {numtermos}")
print(f"Numero de threads {numthreads}")
print("PI: ", pi[4:5])
print(f"Tempo medio: {statistics.mean(tempoExct)} sec")
cv = (statistics.stdev(tempoExct) / statistics.mean(tempoExct)) * 100
print(f"CV: {cv:.5f}%")
print(f"Desvio padrao: {statistics.stdev(tempoExct):.5f}")

print("Final programa")