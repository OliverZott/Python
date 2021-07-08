

def perimeter(length: int):

    thirds = length/3
    return 2*length + 4*length/3


def koch_snowflake(typ: str, length: int, iterations: int):

    thirds = length/3

    base = 3 * length

    for i in range(iterations):
        result = base + thirds
        thirds /= 3

    return result


def koch_snowflake2(typ: str, length: int, iterations: int ):

    smaller = length / 3

    for i in range(iterations):
        result = 3 * length + 3 * smaller
        smaller /= 3

    return result


print(koch_snowflake2("tri", 19683 , 7))
