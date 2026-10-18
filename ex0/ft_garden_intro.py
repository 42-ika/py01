#!/usr/bin/env python3
class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print("=== Welcome to My Garden ===")
        print(f"Plant: {self.name}")
        print(f"Height: {self.height}cm")
        print(f"Age: {self.age} days")
        print("\n=== End of Program ===")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.show()
