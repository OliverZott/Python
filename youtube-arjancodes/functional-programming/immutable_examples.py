"""
Immutables
- e.g. haskell: variables immutable by default!

REMARKS:
- sorted()  ... works on various types
- random.sample
- itertools.chain
"""
import itertools
import random


def main() -> None:
    """"
    Sort example
    """
    test_list = [120, 68, -20, 0, 5, 67, 14, 99]
    test_tuple = (120, 68, -20, 0, 5, 67, 14, 99)

    # built-in immutable sort
    sorted_list = sorted(test_list)
    print(f"Sorted list: {sorted_list}")
    print(f"Original list: {test_list}")

    # built-in mutable sort for list
    test_list.sort()
    print(f"Original list after mutable sort: {test_list}")
    # tuples are immutable --> no sort function
    "test_tuple.sort()"

    """"
    Shuffle  example
    """
    cards = list(itertools.chain([i for i in range(2, 11)], "J", "Q", "K"))

    # immutable
    shuffled_cards = random.sample(cards, k=len(cards))
    print(f"Immutable Shuffled cards: {shuffled_cards}")
    print(f"Original cards: {cards}")

    # mutable
    random.shuffle(cards)
    print(f"Mutable shuffled cards: {cards}")
    print(f"Original cards: {cards}")


if __name__ == "__main__":
    main()
