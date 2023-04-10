"""File to define River class!"""

from exercises.ex11.fish import Fish
from exercises.ex11.bear import Bear


class River:

    day: int
    fish: 'list[Fish]'
    bears: 'list[Bear]' 

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day = 0
        self.fish = []
        self.bears = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        refresh_fish: list[Fish] = []
        refresh_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age < 3:
                refresh_fish.append(fish)
        self.fish = refresh_fish
        for bear in self.bears:
            if bear.age < 5:
                refresh_bears.append(bear)
        self.bears = refresh_bears

        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        refresh_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                refresh_bears.append(bear)
        self.bears = refresh_bears
        return None

    def repopulate_fish(self):
        baby_fish: int = (len(self.fish) // 2) * 4
        for number in range(0, baby_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        baby_bears: int = len(self.bears) // 2
        for number in range(0, baby_bears):
            self.bears.append(Bear())
        return None

    def remove_fish(self, amount: int):
        for index in range(0, amount):
            self.fish.pop(index)
        return None

    def view_river(self):
        print(f"~~~ Day x: {self.day} ~~~")
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
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
