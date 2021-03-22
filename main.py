
def greet(name: [str, list, None] = None) -> str:
    """ Compose greeting string """
    if isinstance(name, list):
        name = ' and '.join(name)

    if not name:
        name = 'my friend'

    if name.isupper():
        return f'HELLO {name}!'

    return f'Hello, {name}.'
