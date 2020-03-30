from src import parser


def test_sum():
    a = 2
    b = 3
    result = 5
    assert parser.sum(a, b) == result
