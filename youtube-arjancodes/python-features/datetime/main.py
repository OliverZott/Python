'''
Datetime Example

https://www.youtube.com/watch?v=TFa38ONq5PY

- create dates
- compare dates
- Pendulum
    - https://pendulum.eustace.io/
    
'''


from datetime import datetime
import time
from pytz import timezone


def main():

    # Create Datetime
    print(f"UNIX time [s]: {time.time()}")
    print(f"UNIX time [ns]: {time.time_ns()}")

    some_time1 = datetime.fromisoformat("2022-11-05T13:23:53Z")
    some_time2 = datetime(2022, 11, 5, 13, 23, 23)

    print(some_time1.__str__())
    print(some_time1.__repr__())
    print(f"{some_time2}")

    # Compare
    print(some_time2 < datetime.now())

    # Timetones
    my_time = datetime.now()
    utc = timezone("UTC")
    loc = utc.localize(my_time)
    print(loc)

    queensland = timezone("Australia/Queensland")
    print(loc.astimezone(queensland))


if __name__ == "__main__":
    main()
