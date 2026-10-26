
class FootballPlayer:
    """Represent a football player and their basic statistics."""

    default_team = "Real Madrid"

    def __init__(self, name, goals, matches_played, jersey_number, team=None):
        self.name = name.strip().title()
        self.team = team or self.default_team
        self.goals = goals
        self.matches_played = matches_played
        self.jersey_number = jersey_number

    @property
    def goals(self):
        return self.__goals

    @goals.setter
    def goals(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Goals must be a non-negative integer.")
        self.__goals = value

    @property
    def matches_played(self):
        return self.__matches_played

    @matches_played.setter
    def matches_played(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Matches played must be a positive integer.")
        self.__matches_played = value

    @property
    def jersey_number(self):
        return self.__jersey_number

    @jersey_number.setter
    def jersey_number(self, value):
        if not self.is_valid_jersey(value):
            raise ValueError("Jersey number must be between 1 and 99.")
        self.__jersey_number = value

    def goals_per_match(self):
        return self.goals / self.matches_played

    def display_stats(self):
        print(f"Player: {self.name}")
        print(f"Team: {self.team}")
        print(f"Jersey number: {self.jersey_number}")
        print(f"Goals: {self.goals}")
        print(f"Matches played: {self.matches_played}")
        print(f"Goals per match: {self.goals_per_match():.2f}")

    @classmethod
    def change_default_team(cls, new_team):
        if not isinstance(new_team, str) or not new_team.strip():
            raise ValueError("Team name cannot be empty.")
        cls.default_team = new_team.strip().title()

    @staticmethod
    def is_valid_jersey(number):
        return isinstance(number, int) and not isinstance(number, bool) and 1 <= number <= 99


class Captain(FootballPlayer):
    """Represent a team captain."""

    def __init__(
        self, name, goals, matches_played, jersey_number,
        leadership_level="High", team=None
    ):
        super().__init__(name, goals, matches_played, jersey_number, team)
        self.leadership_level = leadership_level

    def display_stats(self):
        print("=== CAPTAIN REPORT ===")
        super().display_stats()
        print(f"Leadership level: {self.leadership_level}")


def main():
    mbappe = FootballPlayer(
        name="Kylian Mbappe",
        goals=8,
        matches_played=11,
        jersey_number=10
    )

    valverde = Captain(
        name="Federico Valverde",
        goals=5,
        matches_played=12,
        jersey_number=8,
        leadership_level="High"
    )

    print("=== PLAYER REPORT ===")
    mbappe.display_stats()

    print()
    valverde.display_stats()

    print("\n=== VALIDATION ===")
    print(
        "Is jersey number 10 valid?",
        FootballPlayer.is_valid_jersey(10)
    )
    print(
        "Is jersey number 100 valid?",
        FootballPlayer.is_valid_jersey(100)
    )

    FootballPlayer.change_default_team("Paris Saint-Germain")
    print("\nNew default team:", FootballPlayer.default_team)

    new_player = FootballPlayer(
        name="Example Player",
        goals=2,
        matches_played=6,
        jersey_number=7
    )
    print("Team for a new player:", new_player.team)


if __name__ == "__main__":
    main()
