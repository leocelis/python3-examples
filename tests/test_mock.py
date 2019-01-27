from unittest.mock import MagicMock, Mock, patch


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):
        pass

    def closer(self, something):
        something.close()


def some_function():
    instance = Mock()
    return instance.method()


with patch('unittest.mock.Mock') as mock:
    instance = mock.return_value
    instance.method.return_value = 'the result'
    result = some_function()

    assert result == 'the result'

# create class
real = ProductionClass()

# check if the method was called
real.something = MagicMock()
real.method()
real.something.assert_called_once_with(1, 2, 3)

# check if the method closer was called
mock = Mock()
real.closer(mock)
mock.close.assert_called_with()
