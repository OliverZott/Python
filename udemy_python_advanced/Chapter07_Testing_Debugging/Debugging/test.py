"""Test code
"""

from vector import Vector2D


def main():
    v1 = Vector2D(2, -1)
    print(v1)
    v2 = Vector2D(2, 3)
    print(v2)
    v3 = v1 + v2
    print(v3)


if __name__ == "__main__":
    main()
