import time
import uuid
import random
from threading import Thread
from enum import Enum
import sys
import requests


class DeviceEnum(Enum):
    """
    Classes de prioridades para simulação
    """
    HIGH = 1
    MEDIUM = 2
    LOW = 3

    @staticmethod
    def list():
        """
        Lista todas as classes disponíveis
        :return: Lista de dispositivos
        """
        return list(map(lambda c: c.value, DeviceEnum))

    def random():
        """
        Edscolhe uma das classes de forma aleatória
        :return: A instância da classe
        """
        return random.choice(DeviceEnum.list())


class DeviceSimulator:
    """ "Simula leituras oriundas de sensores"

    Métodos
    -------
    sensor
        Realiza a leitura de acordo com o tipo de dispositivo informado
    """

    def sensor(type, stop):
        """
        Simula a leitura de um dispositivo e exibe na tela

        :param type: Um DeviceEnum indicando o tipo do dispositivo
        :param stop: Variável que sinaliza o fim da execução do dispositivo
        """
        serverUrl = "http://127.0.0.1:5000/server"


        if type is DeviceEnum.HIGH.value:
            while True:
                print("Enviando Mensagem...")
                response = requests.post(serverUrl, json={'device_type': type, 'id': str(uuid.uuid4()), 'ts': time.time(), 'value': random.randrange(5, 40)})
                print("{0} : {1}".format(response.status_code, response.text))
                time.sleep(1)
                if stop():
                    break

        elif type is DeviceEnum.MEDIUM.value:
            while True:
                print("Enviando Mensagem...")
                response = requests.post(serverUrl, json={'device_type': type, 'id': str(uuid.uuid4()), 'ts': time.time(), 'value': random.randrange(10, 100)})
                print("{0} : {1}".format(response.status_code, response.text))
                time.sleep(1)
                if stop():
                    break

        elif type is DeviceEnum.LOW.value:
            while True:
                print("Enviando Mensagem...")
                response = requests.post(serverUrl, json={'device_type': type, 'id': str(uuid.uuid4()), 'ts': time.time(), 'value': random.choice(['OPENED', 'CLOSED', 'LOCKED'])})
                print("{0} : {1}".format(response.status_code, response.text))
                time.sleep(1)
                if stop():
                    break

        elif type is DeviceEnum.LIGHT.value:
            while True:
                print("Enviando Mensagem...")
                response = requests.post(serverUrl, json={'device_type': type, 'id': str(uuid.uuid4()), 'ts': time.time(), 'value': random.choice(['ON', 'OFF'])})
                print("{0} : {1}".format(response.status_code, response.text))
                time.sleep(1)
                if stop():
                    break


if __name__ == "__main__":
    """
    "Programa que simula o envio de mensagens a patir de dispositivos IoT."
    
    A utilização do programa segue a seguinte sintaxe: 
        "DeviceSimulator.py [NÚMERO_DE_DISPOSITIVOS] [TEMPO_DE_EXECUÇÃO]""
        
        Ex: DeviceSimulator.py 10 30"
        
    "O tempo de execução é considerado em segundos"
    """

    if len(sys.argv) != 3:
        print("Uso: DeviceSimulator.py [NÚMERO_DE_DISPOSITIVOS] [TEMPO_DE_EXECUÇÃO]")
        sys.exit()

    try:
        numberOfDevices = int(sys.argv[1])
        timeExecution = int(sys.argv[2])
    except:
        print("Erro: Os parâmetros devem seu números inteiros")
        sys.exit()


    # Criação de threads para simular o comportamento dos dispositivos
    stop_threads = False
    threads = list()
    j = 1
    for i in range(numberOfDevices):
        #device = Thread(target=DeviceSimulator.sensor, args=(DeviceEnum.random(), i, lambda: stop_threads))
        device = Thread(target=DeviceSimulator.sensor, args=(j, lambda: stop_threads))
        threads.append(device)
        device.start()
        if j < 3:
            j += 1
        else:
            j = 1

    # threads criadas e inicializadas. Aguardando o tempo de execução definido
    time.sleep(timeExecution)

    # finalização das threads
    stop_threads = True
    for t in threads:
        t.join()
