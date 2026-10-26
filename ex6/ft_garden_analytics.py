#!/usr/bin/env python3

class Plant():
    class Stats:
        def __init__(self) -> None:
            self._grow_cnt = 0
            self._age_cnt = 0
            self._show_cnt = 0

        def record_grow(self) -> None:
            self._grow_cnt += 1

        def record_age(self) -> None:
            self._age_cnt += 1

        def record_show(self) -> None:
            self._show_cnt += 1

        def show(self) -> None:
            print(
                f"Stats: {self._grow_cnt} grow, "
                f"{self._age_cnt} age, "
                f"{self._show_cnt} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self._stats = self.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self._stats.record_show()

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
        return self._height

    def get_age(self) -> int:
        return self._age

    def age(self) -> None:
        self._age += 1
        self._stats.record_age()

    def grow(self) -> None:
        self._height += 1
        self._stats.record_grow()

    def show_stats(self) -> None:
        self._stats.show()

    @staticmethod
    def is_over_year(age: int) -> bool:
        if (age > 365):
            return True
        else:
            return False

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seed_cnt = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seed_cnt}")

    def bloom(self) -> None:
        super().bloom()
        self.seed_cnt = 42


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_cnt = 0

        def record_shade(self) -> None:
            self._shade_cnt += 1

        def show(self) -> None:
            super().show()
            print(f" {self._shade_cnt} shade")

    _stats: Stats

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of {self._height}cm "
            f"long and {self.trunk_diameter}cm wide."
        )
        self._stats.record_shade()


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


def statistics(plant: Plant) -> None:
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? -> ", Plant.is_over_year(30))
    print("Is 400 days more than a year? -> ", Plant.is_over_year(400))
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[statistics for Rose]")
    statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()

    print("[statistics for Rose]")
    statistics(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5)
    oak.show()
    print("[statistics for Oak]")
    statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    statistics(unknown)
