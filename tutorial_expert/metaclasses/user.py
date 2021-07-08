"""
Problem:
- Maybe no foo method exists --> 

"""

from library import Base


assert hasattr(Base, 'foo1'), "You broke it, no foo method in baseclass"


class Derived(Base):
    def bar1(self):
        """foo1 method has to exist"""
        return self.foo1
        # return self.foo1()

    def bar2(self):
        return 'bar2'


# if __name__ == "__main__":
#     derived_instance = Derived()
#     print(derived_instance.bar1())
