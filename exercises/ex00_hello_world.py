"""My first exercise in COMP110!"""

__author__ = "730573512"


def greet(name: str) -> str:
    """A wecloming first function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
