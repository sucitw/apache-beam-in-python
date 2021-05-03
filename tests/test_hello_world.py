import pytest
from beam_examples.hello_world import hello_world

def test_hello_world():
    output = hello_world
    assert output == 'Hello Beam', 'The input test element should contain "Hello Beam"'