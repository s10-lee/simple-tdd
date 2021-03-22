
def greet(name: [str, list, None] = None) -> str:
    """ Compose greeting string """
    if isinstance(name, list):
        name = f'{", ".join(name[:-1])} and {name[-1]}'

    if not name:
        name = 'my friend'

    if name.isupper():
        return f'HELLO {name}!'

    return f'Hello, {name}.'
