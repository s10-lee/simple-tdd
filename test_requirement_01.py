from main import greet
import pytest


@pytest.mark.parametrize('name', ['Clark', 'John', 'Bruce Wayne'])
def test_requirement_01(name):
    """ Test greeting result """
    assert greet(name) == f'Hello, {name}.'
