
def test_requirement_1(name: str):
    """ Test greeting result """
    result = greet(name)
    if result != f'Hello, {name}.':
        print('test_requirement_1 - fail', result)
    else:
        print('test_requirement_1 - ok', result)


def test_requirement_2():
    """ Test None """
    result = greet()
    if result != 'Hello, my friend.':
        print('test_requirement_2 - fail', result)
    else:
        print('test_requirement_2 - ok', result)



def test_requirement_3(name: str):
    """ Test shouting """
    result = greet(name)
    if name.isupper() and result != f'HELLO {name}!':
        print('test_requirement_3 - fail', result)
    else:
        print('test_requirement_3 - ok', result)



def test_requirement_4(name: list):
    """ Test two names """
    result = greet(name)
    if result != f'Hello, {name[0]} and {name[1]}':
        print('test_requirement_4 - fail', result)
    else:
        print('test_requirement_4 - ok', result)






def greet(name: [None, str, list] = None) -> str:

    if not name:
        return 'Hello, my friend.'

    if isinstance(name, str):
        if name.isupper():
            return f'HELLO {name}!'
        return f'Hello, {name}.'

    return 'Hello'


test_requirement_1('Bob')
test_requirement_2()
test_requirement_3('BOB')
test_requirement_4(['Jill', 'Jane'])
