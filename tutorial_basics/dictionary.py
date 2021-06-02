def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in belts:
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')


ninja_belts = {}


def ninja_input():
    while True:
        ninja_name = input('Enter a ninja name: ')
        ninja_belt = input('Enter a belt colour: ')
        ninja_belts[ninja_name] = ninja_belt

        again = input('Add another name and belt? [y/n]')

        if (again.lower() == 'y'):
            continue
        else:
            break
        return ninja_belts


def ninja_output():
    print(ninja_belts)
    for key, value in ninja_belts.items():
        # print("{} has belt of colour {}".format(key,  value))
        print(f"{key} has belt of colour {value}")


if __name__ == "__main__":

    belts = ninja_input()
    ninja_output()
    belt_count(belts)
