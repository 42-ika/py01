#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print("=== Garden Plant Registry ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 13, 2)
    yura = Plant("yura", 170, 21)
    ika = Plant("ika", 172, 19)
    rose.show()
    yura.show()
    ika.show()
