"""Program to help plan a tea party."""

__author__: str = "730573512"


def main_planner(guests: int) -> None:
    """Plans a tea party using the below functions"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Computes needed teabags based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Computes needed treats based on number of teas each guest drinks"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of teabags and treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)
