import time
import uuid
import random
from threading import Thread
from enum import Enum
import sys
import requests


class DeviceEnum(Enum):
    """
    Tipos de dispositivos para simulação
    """
    TEMPERATURE = 1
    HUMIDITY = 2
    DOOR = 3
    LIGHT = 4

    @staticmethod
    def list():
        """
        Lista todos os dispositivos disponíveis
        :return: Lista de dispositivos
        """
        return list(map(lambda c: c.value, DeviceEnum))

    def random():
        """
        Edscolhe um dos dispositivos de forma aleatória
        :return: A instância de um dispositvo
        """
        return random.choice(DeviceEnum.list())


class DeviceSimulator:
    """ "Simula leituras oriundas de sensores"

    Métodos
    -------
    sensor
        Realiza a leitura de acordo com o tipo de dispositivo informado
    """

    def sensor(type, device_id, stop):
        """
        Simula a leitura de um dispositivo e exibe na tela

        :param type: Um DeviceEnum indicando o tipo do dispositivo
        :param stop: Variável que sinaliza o fim da execução do dispositivo
        """
        serverUrl = "http://127.0.0.1:5000/server"
        #message_id = str(uuid.uuid4())
        if type is DeviceEnum.TEMPERATURE.value:
            while True:
                print("Enviando Mensagem...")
                response = requests.post(serverUrl, json={'device_type': type, 'id': str(uuid.uuid4()), 'ts': time.time(), 'value': random.randrange(5, 40)})
                print("{0} : {1}".format(response.status_code, response.text))
                time.sleep(1)
                if stop():
                    break

        elif type is DeviceEnum.HUMIDITY.value:
            while True:
                print("Enviando Mensagem...")
                response = requests.post(serverUrl, json={'device_type': type, 'id': str(uuid.uuid4()), 'ts': time.time(), 'value': random.randrange(10, 100)})
                print("{0} : {1}".format(response.status_code, response.text))
                time.sleep(4)
                if stop():
                    break

        elif type is DeviceEnum.DOOR.value:
            while True:
                print("Enviando Mensagem...")
                response = requests.post(serverUrl, json={'device_type': type, 'id': str(uuid.uuid4()), 'ts': time.time(), 'value': random.choice(['OPENED', 'CLOSED', 'LOCKED'])})
                print("{0} : {1}".format(response.status_code, response.text))
                time.sleep(9)
                if stop():
                    break

        elif type is DeviceEnum.LIGHT.value:
            while True:
                print("Enviando Mensagem...")
                response = requests.post(serverUrl, json={'device_type': type, 'id': str(uuid.uuid4()), 'ts': time.time(), 'value': random.choice(['ON', 'OFF'])})
                print("{0} : {1}".format(response.status_code, response.text))
                time.sleep(13)
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
    for i in range(numberOfDevices):
        device = Thread(target=DeviceSimulator.sensor, args=(DeviceEnum.random(), i, lambda: stop_threads))
        threads.append(device)
        device.start()

    # threads criadas e inicializadas. Aguardando o tempo de execução definido
    time.sleep(timeExecution)

    # finalização das threads
    stop_threads = True
    for t in threads:
        t.join()
