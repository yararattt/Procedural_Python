class Dog:
    def __init__(self, name: str, breed: str) -> None:
        """Инициализирует собаку с именем и породой.
        :param name: Имя собаки.
        :param breed: Порода собаки.
        """
        self.name = name
        self.breed = breed

    def bark(self) -> str:
        """Издает звук "гав".
        :return: Строка с сообщением о том, что собака лает.
        >>> dog = Dog("Buddy", "Golden Retriever")
        >>> dog.bark()
        'Buddy says woof-woof!'
        """
        return f"{self.name} says woof-woof!"

    def eat(self) -> str:
        """Сообщает, что собака ест.
        :return: Строка с сообщением о том, что собака ест.
        >>> dog = Dog("Buddy", "Golden Retriever")
        >>> dog.eat()
        'Buddy is eating!'
        """
        return f"{self.name} is eating!"

    def sleep(self) -> str:
        """Сообщает, что собака спит.
        :return: Строка с сообщением о том, что собака спит.
        >>> dog = Dog("Buddy", "Golden Retriever")
        >>> dog.sleep()
        'Buddy is sleeping!'
        """
        return f"{self.name} is sleeping!"

    def check_breed(self) -> str:
        """Проверяет породу собаки.
        :return: Строка с информацией о породе собаки.
        >>> dog = Dog("Buddy", "Golden Retriever")
        >>> dog.check_breed()
        'the breed of Buddy is Golden Retriever!'
        """
        return f"the breed of {self.name} is {self.breed}!"

class Cat:
    def __init__(self, name: str, breed: str) -> None:
        """Инициализирует кошку с именем и породой.
        :param name: Имя кошки.
        :param breed: Порода кошки.
        """
        self.name = name
        self.breed = breed

    def meow(self) -> str:
        """Издает звук "мяу".
        :return: Строка с сообщением о том, что кошка мяукает.
        >>> cat = Cat("Whiskers", "Siamese")
        >>> cat.meow()
        'Whiskers says meow-meow!'
        """
        return f"{self.name} says meow-meow!"

    def eat(self) -> str:
        """Сообщает, что кошка ест.
        :return: Строка с сообщением о том, что кошка ест.
        >>> cat = Cat("Whiskers", "Siamese")
        >>> cat.eat()
        'Whiskers is eating!'
        """
        return f"{self.name} is eating!"

    def sleep(self) -> str:
        """Сообщает, что кошка спит.
        :return: Строка с сообщением о том, что кошка спит.
        >>> cat = Cat("Whiskers", "Siamese")
        >>> cat.sleep()
        'Whiskers is sleeping!'
        """
        return f"{self.name} is sleeping!"

    def check_breed(self) -> str:
        """Проверяет породу кошки.
        :return: Строка с информацией о породе кошки.
        >>> cat = Cat("Whiskers", "Siamese")
        >>> cat.check_breed()
        'the breed of Whiskers is Siamese!'
        """
        return f"the breed of {self.name} is {self.breed}!"


class Human:
    def __init__(self, name: str, age: int) -> None:
        """Инициализирует человека с именем и возрастом.
        :param name: Имя человека.
        :param age: Возраст человека.
        """
        self.name = name
        self.age = age

    def eat(self) -> str:
        """Сообщает, что человек ест.
        :return: Строка с сообщением о том, что человек ест.
        >>> human = Human("Alice", 30)
        >>> human.eat()
        'Alice is eating!'
        """
        return f"{self.name} is eating!"
    def sleep(self) -> str:
        """Сообщает, что человек спит.
        :return: Строка с сообщением о том, что человек спит.
        >>> human = Human("Alice", 30)
        >>> human.sleep()
        'Alice is sleeping!'
        """
        return f"{self.name} is sleeping!"

    def check_age(self) -> str:
        """Проверяет возраст человека.
        :return: Строка с информацией о возрасте человека.
        >>> human = Human("Alice", 30)
        >>> human.check_age()
        'the age of Alice is 30!'
        """
        return f"the age of {self.name} is {self.age}!"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
