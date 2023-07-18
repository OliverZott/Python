from datetime import datetime
from functools import wraps


def log(fn):
    @wraps(fn)
    def logger(*args, **kwargs):
        """Custom logger

        Returns
        -------
        result of function and loggs to console

        """

        time_str = datetime.utcnow().strftime("%H:%M:%S")
        fn_result = 0
        try:
            print(f"Function {fn.__name__} was called at {time_str}")
            fn_result = fn(*args, **kwargs)
        except ZeroDivisionError as z:
            print(f"ZeroDivisionError: '{z}'")
        except Exception as e:
            print(f"Exception: {e}")

        return fn_result

    return logger


@log
def divide_integers(a: int, b: int) -> float:
    result = a / b
    return result


if __name__ == "__main__":
    res = divide_integers(1, 0)
    print(res)
