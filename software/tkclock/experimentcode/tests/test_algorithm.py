#Setup
from algolib import *

#test adding

#test wrong input
def test_add_wrong_inputtype():
    assert add_values(-1, 2.0) == 0

#test adding
def test_add():
    assert add_values(1.00, 2) == 3.00
    
