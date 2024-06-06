import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize("string",[
    '()',
    ' ',
    '((()))',
    '(())()()(())'
])
def test_matching_parenthesis(string):
    x = matching_parentheses(string)
    assert x == True, f"{x} has matching parenthesis"

@pytest.mark.parametrize("string",[
    ')()',
    '())',
    '((((())))((())',
    ')()'
])
def test_non_matching_parenthesis(string):
    x = matching_parentheses(string)
    assert x == False,f"{x} has non matching parenthesis"