from Scientific_Programming.Chapter7_ModulesScopesNamespaces import greetings

# in following case, function needs to be called by full path!!!
import Scientific_Programming.Chapter7_ModulesScopesNamespaces.greetings


def main():

    greetings.say_hi('Olli')
    greetings.say_hi('Lenchen', 'fr')

    greetings.add_lang('de2', 'sewas')
    greetings.add_lang2('de3', 'Guten Tag')

    print(greetings.base)


if __name__ == "__main__":
    main()
