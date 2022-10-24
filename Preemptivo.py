'''
Round Robin (RR) - Algoritmo PREEMPTIVO

Joao Victor de Oliveira Gomes Ribeiro - GES 106
Dessana Siqueira Alves - GEC 1544
'''

import matplotlib.pyplot as plt

#Função para encontrar o tempo de espera dos processos
def tempoEspera(qtdProcesso, burstTime, waitingTime, quantum):
    waitingTime[0] = 0  # Tempo de espera do primeiro processo definido como 0
    bTime = [0] * qtdProcesso #Lista de cópia do burstTime pra uso posterior
    tempoAtual = 0

    for processo in range(1, qtdProcesso):
        bTime[processo] = burstTime[processo]

    #Os processos serao percorridos ate que todos sejam executados
    while (1):
        pronto = True

        #Percorrendo todos os processos
        for processo in range(qtdProcesso):

            #Se o burstTime de um processo eh > 0 entao continua o processamento
            if (bTime[processo] > 0):

                pronto = False  #Processo em execução

                #Se o burstTime de um processo eh maior que o quantum ele será salvo com o valor que falta e seu processamento será interrompido
                #Dando início ao próximo processo
                if (bTime[processo] > quantum):

                    tempoAtual += quantum #Incrementa o valor do tempoAtual com o valor do quantum
                    bTime[processo] -= quantum #Decrementa do burstTime do processo atual o valor do quantum

                #Se o burstTime eh <= ao quantum a execução eh terminada e o processo eh dado como finalizado
                else:

                    tempoAtual = tempoAtual + bTime[processo] #Incrementa o valor do tempoAtual para encerrar o ciclo de quantum

                    #Calcula o waitingTime pra aquele processo waitingTime = tempoAtual - burstTime do processo
                    waitingTime[processo] = tempoAtual - burstTime[processo]
                    bTime[processo] = 0 #Processo totalmente executado retorna burstTime = 0
                    

        #Se todos os processos foram finalizados pronto = True e o loop eh encerrado
        if (pronto == True):
            break

#Função para calcular o tempo medio
def tempoMedio(qtdProcessos, burstTime, quantum, tempo):
    waitingTime = [0] * qtdProcessos
    waitingTime_Total = 0
    tempoEspera(qtdProcessos, burstTime, waitingTime, quantum) #Chamada da função de tempo de espera dos processos

    print("Processo " + " Burst Time " + " Waiting Time")

    for processo in range(qtdProcessos):
        waitingTime_Total = waitingTime_Total + waitingTime[processo]
        print(" ", str(processo + 1), "\t\t", str(burstTime[processo]), "\t   ", str(waitingTime[processo]))

    print("Tempo Medio total = " + str(waitingTime_Total / qtdProcessos))
    plt.savefig("gantt_RR.png")


#Executando o Scheduling RR
if __name__ == "__main__":

    bTime = []
    tempo = 0 #Variavel para usar no grafico (eixo x)
    quantum = int(input("insira o quantum desejado: "))
    qtdProcessos = int(input("insira a quantidade de processos desejados: "))

    for processo in range(qtdProcessos):
        burst_time = int(input(f'insira o Burst Time desejado do processo {processo+1}: '))
        bTime.append(burst_time)
        tempo += burst_time

    tempoMedio(qtdProcessos, bTime, quantum, tempo)