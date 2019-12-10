import time
import uuid
import random
from threading import Thread
from enum import Enum
import sys
import requests
from DeviceTypeEnum import DeviceTypeEnum


class DeviceSimulator:
    """ "Simula leituras oriundas de sensores"

    Métodos
    -------
    sensor
        Realiza a leitura de acordo com o tipo de dispositivo informado
    """

    def sensor(type, qtdMessage, interval, serverUrl):
        """
        Simula a leitura de um dispositivo e exibe na tela

        :param type: Um DeviceEnum indicando o tipo do dispositivo
        :param qtdMessage: Quantidade de mensagens a serem enviadas
        :param interval: Intervalo para envio das mensagens
        :param stop: Variável que sinaliza o fim da execução do dispositivo
        """

        i = 0
        while(i < qtdMessage):
            response = requests.post(serverUrl, json={'device_type': type, 'id': str(uuid.uuid4()), 'ts': time.time(),
                                                      'value': random.randrange(5, 40)})
            print("{0} : {1}".format(response.status_code, response.text))
            time.sleep(interval)
            i += 1



if __name__ == "__main__":
    """
    "Programa que simula o envio de mensagens a patir de dispositivos IoT."
    
    A utilização do programa segue a seguinte sintaxe: 
        "DeviceSimulator.py NÚMERO DE MENSAGENS""
        
        Ex: DeviceSimulator.py 30"
        
        Distribuição das mensagens
        50% BAIXA
        35% MÉDIA
        15% ALTA
    """

    if len(sys.argv) != 2:
        print("Uso: DeviceSimulator.py NÚMERO DE MENSAGENS")
        sys.exit()

    try:
        qtdMessages = int(sys.argv[1])
    except:
        print("Erro: O parâmetro deve ser um número inteiro")
        sys.exit()

    # Distribuição dos dispositivos
    numberOfDevices = 1
    if qtdMessages >= 10:
        numberOfDevices = qtdMessages // 10

        # Distribuição das mensagens
        qtdLow = int(qtdMessages*0.5)
        qtdMedium = int(qtdMessages*0.35)
        qtdHigh = qtdMessages - (qtdLow + qtdMedium)


    deviceLow = Thread(target=DeviceSimulator.sensor, args=(DeviceTypeEnum.LOW.value, qtdLow, 1*0.15, "http://127.0.0.1:5000/fifo"))
    deviceLow.start()

    deviceMedium = Thread(target=DeviceSimulator.sensor, args=(DeviceTypeEnum.MEDIUM.value, qtdMedium, 1*0.35, "http://127.0.0.1:5000/fifo"))
    deviceMedium.start()

    deviceHigh = Thread(target=DeviceSimulator.sensor, args=(DeviceTypeEnum.HIGH.value, qtdHigh, 1, "http://127.0.0.1:5000/fifo"))
    deviceHigh.start()


    time.sleep(1800)

    deviceLowBin = Thread(target=DeviceSimulator.sensor, args=(DeviceTypeEnum.LOW.value, qtdLow, 1 * 0.15, "http://127.0.0.1:5000/binomial"))
    deviceLowBin.start()

    deviceMediumBin = Thread(target=DeviceSimulator.sensor, args=(DeviceTypeEnum.MEDIUM.value, qtdMedium, 1 * 0.35, "http://127.0.0.1:5000/binomial"))
    deviceMediumBin.start()

    deviceHighBin = Thread(target=DeviceSimulator.sensor, args=(DeviceTypeEnum.HIGH.value, qtdHigh, 1, "http://127.0.0.1:5000/binomial"))
    deviceHighBin.start()


    time.sleep(1800)

    deviceLowFib = Thread(target=DeviceSimulator.sensor,
                       args=(DeviceTypeEnum.LOW.value, qtdLow, 1 * 0.15, "http://127.0.0.1:5000/fib"))
    deviceLowFib.start()

    deviceMediumFib = Thread(target=DeviceSimulator.sensor,
                          args=(DeviceTypeEnum.MEDIUM.value, qtdMedium, 1 * 0.35, "http://127.0.0.1:5000/fib"))
    deviceMediumFib.start()

    deviceHighFib = Thread(target=DeviceSimulator.sensor,
                        args=(DeviceTypeEnum.HIGH.value, qtdHigh, 1, "http://127.0.0.1:5000/fib"))
    deviceHighFib.start()


    time.sleep(1800)

    deviceLowVeb = Thread(target=DeviceSimulator.sensor,
                       args=(DeviceTypeEnum.LOW.value, qtdLow, 1 * 0.15, "http://127.0.0.1:5000/veb"))
    deviceLowVeb.start()

    deviceMediumVeb = Thread(target=DeviceSimulator.sensor,
                          args=(DeviceTypeEnum.MEDIUM.value, qtdMedium, 1 * 0.35, "http://127.0.0.1:5000/veb"))
    deviceMediumVeb.start()

    deviceHighVeb = Thread(target=DeviceSimulator.sensor,
                        args=(DeviceTypeEnum.HIGH.value, qtdHigh, 1, "http://127.0.0.1:5000/veb"))
    deviceHighVeb.start()




    # Criação de threads para simular o comportamento dos dispositivos
    #stop_threads = False
    #threads = list()
    #for i in range(numberOfDevices):
    #device = Thread(target=DeviceSimulator.sensor, args=(j, lambda: stop_threads))
    #threads.append(device)
    #device.start()


    # threads criadas e inicializadas. Aguardando o tempo de execução definido
    #time.sleep(timeExecution)

    # finalização das threads
    #stop_threads = True
    #for t in threads:
        #t.join()
