class Topping:
    def __init__(self, toppling_type: str, weight: float) -> None:
        self.topping_type = toppling_type
        self.weight = weight


    @property
    def topping_type(self) -> str:
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value) -> None:
        if value == "":
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type = value

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value) -> None:
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value
