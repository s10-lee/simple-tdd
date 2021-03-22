
def greet(name: [str, None] = None) -> str:
    """ Compose greeting string """
    if not name:
        name = 'my friend'

    if name.isupper():
        return f'HELLO {name}!'

    return f'Hello, {name}.'
