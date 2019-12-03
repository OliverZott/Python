"""
A module to say hello

Author: Oliver Zott
"""

base = {
    'en': 'Hi {}!',
    'fr': 'Salut {}!',
    'de': 'Moin {}!'
}


def say_hi(name, lang='en'):  # Parameter with default
    """ Greeter method

    Keyword-Argument
    ----------------
        lang : str
            language in which to great
        name : str
            name of the person to be greeted

    Returns
    -------
        none            # not necessary

    Raises
    ------
        nothing         # not necessary
    """

    if lang not in base:
        print('Language unknown: {}'.format(lang))

    print(base[lang].format(name))


def add_lang(key, phrase):
    """ Add a language to base """

    global base  # use global to change global variable (else just can call it)

    base.update({key: phrase})


def add_lang2(key, phrase):
    """ Alternative version to add language to dictionary """

    global base

    base[key] = phrase




