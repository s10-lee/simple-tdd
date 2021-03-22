from main import greet
import pytest


@pytest.mark.parametrize('name', ['Clark', 'John', 'Bruce Wayne'])
def test_requirement_01(name):
    """ Test greeting result """
    assert greet(name) == f'Hello, {name}.'


@pytest.mark.parametrize('name', [None])
def test_requirement_02(name):
    """ Test greeting result """
    assert greet(name) == 'Hello, my friend.'


@pytest.mark.parametrize('name', ['GORDON', 'LOIS LANE'])
def test_requirement_03(name):
    assert greet(name) == f'HELLO {name}!'


@pytest.mark.parametrize('name', [['Bruce Wayne', 'Selina Kyle'], ['Clark', 'Lois']])
def test_requirement_04(name):
    assert greet(name) == f'Hello, {name[0]} and {name[1]}.'


@pytest.mark.parametrize('name', [['Jean Grey', 'Kurt', 'Hank', 'Charles'], ['Scott Summers', 'Wade Wilson', 'Logan']])
def test_requirement_05(name):
    assert greet(name) == f'Hello, {", ".join(name[:-1])} and {name[-1]}.'


@pytest.mark.parametrize("name,expected", [
    (['Kurt', 'HANK', 'Jean', 'Charles'], 'Hello, Kurt, Jean and Charles. AND HELLO HANK!'),
    (['Scott', 'LOGAN'], 'Hello, Scott. AND HELLO LOGAN!')
])
def test_requirement_06(name, expected):
    assert greet(name) == expected


@pytest.mark.parametrize("name,expected", [
    (['Scott', 'Jean', 'Kurt, Charles'], 'Hello, Scott, Jean, Kurt and Charles.'),
])
def test_requirement_07(name, expected):
    assert greet(name) == expected
