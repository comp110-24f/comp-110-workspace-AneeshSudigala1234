"""The program will ask the user for the number of guests and will calculate the quantity of tea bags needed, the number of treats to accompany the tea, and the expected cost of the party"""

__author__: str = "730744298"


def tea_bags(people: int) -> int:
    """Calculate the amount of tea bags for all the people"""
    return people * 2  # Multiplies by 2


def treats(people: int) -> int:
    """Calculate the amount of treats based on number of tea bags"""
    return int(
        tea_bags(people=people) * 1.5
    )  # Multiplies by 2 and turns into an integer


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of the tea bags and the treats combined"""
    return 0.5 * tea_count + 0.75 * treat_count  # Uses PEMDAS


def main_planner(guests: int) -> None:
    """Calls all these functions and produces printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")  # String concatenation
    print("Tea Bags: " + str(tea_bags(people=guests)))  # String concatenation
    print("Treats: " + str(treats(people=guests)))  # String concatenation
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )  # String concatenation
    )


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # Function that calls everything
