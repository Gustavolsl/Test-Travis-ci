import pytest
from principal import dividir,multiplicar
#import principal

def test_dividir():
    assert dividir(10,2)==5.0
    assert multiplicar(2,4)==8