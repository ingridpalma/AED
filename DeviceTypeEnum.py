import random
from enum import Enum


class DeviceTypeEnum(Enum):
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