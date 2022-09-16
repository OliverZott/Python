from string import Template
import timeit


def perc_format():
    name = "olli"
    country = "Austria"
    _ = "%s is from %s." % (name, country)


def str_format():
    name = "olli"
    country = "Austria"
    _ = "{} is from {}.".format(name, country)


def f_format():
    name = "olli"
    country = "Austria"
    _ = f"{name} is from {country}."


TEMPLATE = Template("$name is from $country")  # from string library


def template():
    name = "olli"
    country = "Austria"
    _ = TEMPLATE.substitute(name=name, country=country)


def main() -> None:
    print("perc_format: ", timeit.timeit(perc_format, number=1000000))
    print("str_format: ", timeit.timeit(str_format, number=1000000))
    print("f_format: ", timeit.timeit(f_format, number=1000000))
    print("template: ", timeit.timeit(template, number=1000000))


if __name__ == "__main__":
    main()
