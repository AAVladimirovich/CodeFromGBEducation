from tictactoe import Board
from tictactoe.egtb import Generator
import functools, operator
from tictactoe.egtb import Reader


import numpy as np
import matplotlib.pyplot as plt

import pytest


def division(a, b):
     return a / b


def increm(a):
     x = 0
     for i in range(a+1):
          x = x + i
     return x


@pytest.mark.parametrize('a,b, expected_result', [(10,2,5)])
def test_devision_good(a, b, expected_result):
     assert division(a, b) == expected_result


@pytest.mark.parametrize('expected_exception, division_n, divider', [(ZeroDivisionError,100,0),
                                                                (TypeError,100,'2')])
def test_devision_with_error(expected_exception, division_n, divider):
     with pytest.raises(expected_exception):
          division(division_n, divider)

list_for_test = [(3,6), (4,10), (5,15)]
@pytest.mark.parametrize('a, expected_result', list_for_test)
def test_increm_good(a, expected_result):
     assert increm(a) == expected_result

@pytest.mark.parametrize('expected_exception, x', [(TypeError, '2')])
def test_increm_with_error(expected_exception, x):
     with pytest.raises(expected_exception):
          increm(x)




x1 = np.linspace(0, 2.0*np.pi, 101)
y1 = np.sin(x1)

plt.plot(x1, y1)
plt.show()

# board = Board(dimensions=(3, 3), x_in_a_row=3)
# board.push((0, 0))
# print(board)
# board.push((0, 1))
# print(board)
# board.push((0, 1))
# print(board)

dimensions = (3, 3)
total_squares = functools.reduce(operator.mul, dimensions)
for index in reversed(range(total_squares + 1)):
     print(index)
     Generator(dimensions, 3, index)
     print(Generator(dimensions, 3, index))


reader = Reader((3, 3), 3, 2)
board = Board((3, 3), 3)
# board.push((0, 0))
# board.push((0, 1))
print(board)
print(reader.index(board))
print(total_squares)

