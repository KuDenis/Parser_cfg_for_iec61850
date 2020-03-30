from src import parser


def test_sum():
    a = 2
    b = 3
    result = 5
    assert parser.sum(a, b) == result


def test_logical_device():
    expected = 'LogicalDevice full_name = {\n   ' \
               ' LogicalDeviceModelType,\n  ' \
               '  \"name\",\n  ' \
               '  parent,\n   ' \
               ' sibling,\n   ' \
               ' first_child\n' \
               ';}\n  ' \
               ' \n''
    pass


