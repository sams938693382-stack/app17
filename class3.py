class Telefon:
    def __init__(self, brand, model, narx):
        self.brand = brand
        self.model = model
        self.narx = narx

    def get_info(self):
        return f"{self.brand} {self.model} telefoni narxi {self.narx}$"


class TelefonDokon(Telefon):
    def __init__(self, brand, model, narx, dokon_nomi, manzil):
        super().__init__(brand, model, narx)
        self.dokon_nomi = dokon_nomi
        self.manzil = manzil

    def get_info(self):
        return f"{super().get_info()} va {self.dokon_nomi} do'konida {self.manzil}da sotiladi"


tel1 = TelefonDokon(
    "Samsung",
    "S24 Ultra",
    1200,
    "Mobile Market",
    "Toshkent"
)

print(tel1.get_info())