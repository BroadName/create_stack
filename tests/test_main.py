import pytest
from main import custom_func, using_list_methods


class TestMain:
    @pytest.mark.parametrize(
        'sequence, expected',
        (
            ['(((([{}]))))', True],
            ['[([])((([[[]]])))]{()}', True],
            ['{{[()]}}', True],
            ['}{}', False],
            ['{{[(])]}}', False],
            ['[[{())}]', False],
            ['(', False],
            ['', False]
         )
    )
    def test_custom_func(self, sequence: str, expected: bool):
        assert expected == custom_func(sequence)

    @pytest.mark.parametrize(
        'sequence, expected',
        (
         ['(((([{}]))))', True],
         ['[([])((([[[]]])))]{()}', True],
         ['{{[()]}}', True],
         ['}{}', False],
         ['{{[(])]}}', False],
         ['[[{())}]', False],
         ['(', False],
         ['', False]
         )
    )
    def test_using_list_method(self, sequence: str, expected: bool):
        assert expected == using_list_methods(sequence)


if __name__ == '__main__':
    pytest.main()
