
def greet(name: [str, None] = None) -> str:
    """ Compose greeting string """
    if not name:
        name = 'my friend'

    return f'Hello, {name}.'
