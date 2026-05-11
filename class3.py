class Oyinchi:
    def __init__(self, ism, level, coin):
        self.ism = ism
        self.level = level
        self.coin = coin

    def add_coin(self, miqdor):
        self.coin += miqdor
        print(f" {miqdor} coin qoshildi")

    def info(self):
        print(f" {self.ism}")
        print(f" Level: {self.level}")
        print(f" Coin: {self.coin}")


player = Oyinchi("Shoxrux", 5, 100)

player.add_coin(50)
player.add_coin(200)
player.add_coin(500)

player.info()
