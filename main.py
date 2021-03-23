
def greet(name: [str, list, None] = None) -> str:
    """ Compose greeting string """

    shouting = ''

    if isinstance(name, list):
        names = []

        for person_name in name:
            if person_name.isupper():
                shouting = f' AND HELLO {person_name}!'
            else:
                names.extend(person_name.split(', '))

        if len(names) > 1:
            name = f'{", ".join(names[:-1])} and {names[-1]}'
        else:
            name = names[0]


    if not name:
        name = 'my friend'

    if name.isupper():
        return f'HELLO {name}!'

    return f'Hello, {name}.{shouting}'
