from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, brand: str, model: str, year: int) -> None:
        self._brand = brand  # Инкапсуляция, так как бренд редко изменяется
        self._model = model  # Инкапсуляция, так как модель редко изменяется
        self.year = year

    def __str__(self) -> str:
        return f"{self._brand} {self._model} ({self.year})"

    def __repr__(self) -> str:
        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self.year})"

    @abstractmethod
    def move(self) -> str:
        pass


class Car(Vehicle):

    def __init__(self, brand: str, model: str, year: int, fuel_type: str) -> None:
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def __str__(self) -> str:
        return f"{self._brand} {self._model} ({self.year}), топливо: {self.fuel_type}"

    def move(self) -> str:
        return f"{self._brand} {self._model} едет по дороге."

    def refuel(self, amount: float) -> str:
        return f"{self._brand} {self._model} заправлен на {amount} литров {self.fuel_type}."


if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2022, "бензин")
    print(my_car)
    print(my_car.move())
    print(my_car.refuel(50))
