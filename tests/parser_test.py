from src import parser


def test_sum():
    a = [*range(9)]
    b = [*range(9)]
    result = [2*x for x in range(9)]
    for c, d, e in zip(a, b, result):
        assert parser.sum(c, d) == e


def test_mull():
    a = 2
    b = 3
    result = 6
    assert parser.mull(a, b) == result