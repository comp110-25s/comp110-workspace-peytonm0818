"""Program to help plan a tea party."""

__author__: str = "730573512"


def tea_bags(people: int) -> int:
    """Computes needed teabags based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Computes needed treats based on number of teas each guest drinks"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of teabags and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)
