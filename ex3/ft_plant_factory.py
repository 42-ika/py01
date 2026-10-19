#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self) -> None:
        self.height += 2

    def add_age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 13.0, 30)
    tree = Plant("tree", 100.5, 100)
    grass = Plant("grass", 20.3, 30)
    carrot = Plant("carrot", 15.5, 60)
    SunFlower = Plant("SunFlower", 100.5, 30)

    rose.show()
    tree.show()
    grass.show()
    carrot.show()
    SunFlower.show()
