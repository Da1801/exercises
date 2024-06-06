import pytest
from mystatistics import average

@pytest.mark.parametrize("ns,expected",[
   ([1],1),
   ([6,4],5),
   ([0.1,0.1,0.1],0.1) 
])

def test_average(ns,expected):
    assert pytest.approx(expected) == average(ns)