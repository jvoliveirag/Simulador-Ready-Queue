'''
Fist Come First Serve (FCFS/FIFO) - NÃO PREEMPTIVO

Joao Victor de Oliveira Gomes Ribeiro - GES 106
Dessana Siqueira Alves - GEC 1544
'''

import matplotlib.pyplot as plt

#Encontra o tempo de espera
def tempoEspera (qtdProcessos, bustTime, waitingTime):
    waitingTime[0] = 0 #Tempo de espera do primeiro processo definido como 0

    for processo in range(1, qtdProcessos):
        waitingTime[processo] = bustTime[processo - 1] + waitingTime[processo - 1]

#Calculo do tempo medio
def tempoMedio(qtdProcessos, burstTime, tempo):
    waitingTime = [0] * qtdProcessos
    waitingTime_Total = 0

    tempoEspera(qtdProcessos, burstTime, waitingTime) 

    fig, gnt = plt.subplots()

    gnt.set_ylim(0, qtdProcessos+1)     #setando eixo Y
    gnt.set_xlim(0, tempo)              #setando eixo X

    gnt.set_xlabel('Tempo [ms]')
    gnt.set_ylabel('Processo')

    gnt.grid(axis = 'y', color = 'blue', linestyle = '--', linewidth = 0.5)

    print("Processo " + " Burst time " + " Waiting time ")
    #Calculando o tempo total de espera
    for processo in range(qtdProcessos):
        waitingTime_Total = waitingTime_Total + waitingTime[processo]
        print(" " + str(processo + 1) + "\t\t" + str(burstTime[processo]) + "\t    " + str(waitingTime[processo]))

        gnt.broken_barh([(waitingTime[processo], burstTime[processo])], (processo+0.9, 0.2))

    print("Tempo Medio total = " + str(waitingTime_Total/qtdProcessos))
    plt.savefig("gantt_FCFS.png")


#Executando o Scheduling FCFS
if __name__ == "__main__":

    bTime = []
    tempo = 0 #Variavel para usar no grafico (eixo x)

    qtdProcessos = int(input("insira a quantidade de processos desejados: "))

    for processo in range(qtdProcessos):
        burst_time = int(input(f'insira o Burst Time desejado do processo {processo+1}: '))
        bTime.append(burst_time)
        tempo += burst_time

    tempoMedio(qtdProcessos, bTime, tempo)