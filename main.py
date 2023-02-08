import time


class Elevador:
    def __init__(self, andar):
        self.andar_atual = 0

    def andar(self):
        return self.andar_atual

    def mover(self, move):
        sentido = self.andar_atual - move
        if sentido < 0:
            sentido = sentido * (-1)
            sentido = sentido + self.andar_atual
            while self.andar_atual < sentido:
                print(f'Você esta no andar {self.andar_atual}\nSubindo...\n')
                time.sleep(1)
                self.andar_atual += 1
            sentido = 0

        if sentido == 0:
            print(f'Você já está no andar {self.andar_atual}\n')
            sentido = 0

        if sentido > 0:
            while sentido == self.andar_atual and self.andar_atual > 0:
                print(f'Você está no andar {self.andar_atual}\nDescendo...\n')
                time.sleep(1)
                self.andar_atual -= 1
                sentido -= 1

            while self.andar_atual > sentido:
                print(f'Você está no andar {self.andar_atual}\nDescendo...\n')
                time.sleep(1)
                self.andar_atual -= 1
            sentido = 0


x = 0
e = Elevador(0)

while x == 0:
    print(f'Você está no andar {e.andar_atual}')
    andar = int(input('Para qual andar você deseja ir?\n'))
    if andar == 's':
        x = 1
    e.mover(andar)
