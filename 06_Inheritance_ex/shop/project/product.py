class Product:
    def __init__(self, name: str, quantity: int):
        self.name= name
        self.quantity = quantity

    def increase(self, quantity: int) -> None:
        pass
    def decrease(self, quantity: int) -> None:
        pass
    def __repr__(self):
        return self.name