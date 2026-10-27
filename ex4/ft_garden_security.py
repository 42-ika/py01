#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self._height = 0.0
        self._age = 0

        self.set_age(age)
        self.set_height(height)
        print(
            f"Plant created: {self.name}: {self._height}cm, "
            f"{self._age} days old"
        )

    def show(self) -> None:
        print(
            f"Current state: {self.name}: {self._height}cm, "
            f"{self._age} days old"
        )

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"age updated: {self._age} days")

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 13.0, 30)
    rose.set_height(25.0)
    rose.set_height(-10.0)
    rose.set_age(31)
    rose.show()
