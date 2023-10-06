# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

from example_functions import my_adder,my_thermo_stat,have_digits

def test_adder():
    assert my_adder(1,2,3) == 6

def test_my_thermo_stat():
    assert my_thermo_stat(4,10) == "Heat"

def test_have_digits():
    assert have_digits('USA2023') == 1
    
 
