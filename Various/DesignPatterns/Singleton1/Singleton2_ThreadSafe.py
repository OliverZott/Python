from __future__ import annotations
from threading import Lock, Thread
from typing import Optional


class SingletonMeta(type):
    """
    Thread-Safe implementation of Singleton-Pattern
    """

    _instance: Optional[Singleton] = None  # WTF?

    _lock: Lock = Lock()  # WTF? --> Variable annotation: var: str="..."
    """
    Now we have a lock-object that will be used to synchronize threads during 
    first access to the Singleton!
    """

    def __call__(cls, *args, **kwargs):
        """
        Now, imagine that the program has just been launched. Since there's no
        Singleton instance yet, multiple threads can simultaneously pass the
        previous conditional and reach this point almost at the same time. The
        first of them will acquire lock and will proceed further, while the
        rest will wait here.
        """

        with cls._lock:
            """
            The first thread to acquire the lock, reaches this conditional,
            goes inside and creates the Singleton instance. Once it leaves the
            lock block, a thread that might have been waiting for the lock
            release may then enter this section. But since the Singleton field
            is already initialized, the thread won't create a new object.
            """
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    We'll use this property to check if Singleton really works.
    """

    def __init__(self, value: "str") -> None:
        self.value = value

    def some_business_logic(self):
        """
       Finally, any singleton should define some business logic, which can be
       executed on its instance.
       """


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == '__main__':
    # The Client Code

    print("If you see the same values, the Singleton was reused... yaaay!\n"
          "If you see different values, 2 singletons were created... boooooh!\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=('FOO',))
    process2 = Thread(target=test_singleton, args=("BAR",))

    process1.start()
    process2.start()
