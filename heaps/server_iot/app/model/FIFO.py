from collections import deque


class FIFO:

    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.queue:
            print('Removendo elemento...')
            return self.queue.popleft()
        return None

    def __str__(self):
        return str(self.queue)


if __name__ == "__main__":

    fila = FIFO()
    fila.push("{'device_id': 9, 'id': '6fb1c8b0-ded1-460f-b582-eedb45ff1b13', 'ts': 1572732196.217073, 'value': 25}")
    print(fila)

    fila.push("{'device_id': 5, 'id': '2a3bbe23-0f72-429d-a886-b13e4b1223c5', 'ts': 1572732196.2146401, 'value': 21}")
    print(fila)

    fila.push("{'device_id': 1, 'id': 'f875048d-0301-432f-a600-055f5c72facd', 'ts': 1572732196.211217, 'value': 63}")
    print(fila)

    print(fila.pop())

    print(fila)