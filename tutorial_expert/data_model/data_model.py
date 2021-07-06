# behavior I want to implement  ->  write some __ functions __
# top level function or top level syntax  ->  corresponding __ (dunder methods)
#   x + y   ->  __add__
#   init x  ->  __init__
#   repr(x) ->  __repr__
#   

class Polynomial:
    def __init__(self, *coeffs) -> None:
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        '''
        len is representation of degree 
        '''
        return len(self.coeffs)


if __name__ == "__main__":

    p1 = Polynomial(2, 1, 5)    # 2x^2 + x + 5
    p2 = Polynomial(3, 4, 2)    # 3x^2 + 4x + 2
    p3 = Polynomial(7, 2, 5, 3)    # 7x^3 + 2x^2 + 5x + 3

    print(repr(p1))
    print(repr(p1 + p2))
    print(len(p3))
