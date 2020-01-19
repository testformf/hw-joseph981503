import random
from module import *
import pytest

# target = []

# @pytest.fixture
# def random_tuple():
#     target = [(random.randrange(0, 50), random.randrange(0, 20), random.randrange(0, 30)) for i in range(10)]
#     pass


@pytest.mark.parametrize("input1, input2, output", [(random.randrange(30, 50), random.randrange(0, 20), random.randrange(0, 30)) for i in range(10)])
def test_add(input1, input2, output):
    assert calculate(input1, input2) > output, "failed"
