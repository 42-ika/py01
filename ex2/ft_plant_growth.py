#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print("=== Garden Plant Growth ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            self.add_age()
            self.add_grow()
            print(f"{self.name}: {self.height}cm, {self.age} days old")

    def add_grow(self) -> None:
        self.height += 2

    def add_age(self) -> None:
        self.age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.show()
