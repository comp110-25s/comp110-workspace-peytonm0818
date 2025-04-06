"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        current_bears: list[Bear] = []
        current_fish: list[Fish] = []
        for bears in self.bears:
            if bears.age <= 5:
                current_bears.append(bears)
        self.bears = current_bears

        for fish in self.fish:
            if fish.age <= 3:
                current_fish.append(fish)
        self.bears = current_bears
        return None

    def bears_eating(self):
        """Removes fish from river is bear is hungry"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Removes starving bears from river"""
        surviving_bears: list[Bear] = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                surviving_bears.append(bears)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Causes fish to reproduce if there are enough"""
        new_fish: int = len(self.fish) // 2 * 4

        while new_fish > 0:
            self.fish.append(Fish())
            new_fish -= 1
        return None

    def repopulate_bears(self):
        """Causes bears to reproduce if there are enough"""
        new_bears: int = len(self.bears) // 2

        while new_bears > 0:
            self.bears.append(Bear())
            new_bears -= 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes amount of fish from the river"""
        remove: int = 0

        while remove <= amount and len(self.fish) > 0:
            self.fish.pop(0)
            remove += 1
        return None
