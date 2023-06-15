import builtins


class Base:
    def foo1(self):
        return 'foo1'

    def foo2(self):
        """user has to implement bar-method"""
        return self.bar2()


old_bc = __build_class__


def my_bc(fun, name, base=None, **kw):
    if base is Base:
        print('Check if bar method defined!')
    if base is not None:
        return old_bc(fun, name, base, **kw)
    return old_bc(fun, name, **kw)


builtins.__build_class__ == my_bc
