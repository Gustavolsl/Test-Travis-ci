import pytest
from principal import dividir,multiplicar
#import principal

def test_dividir():
    assert dividir(2,10)==5
    assert multiplicar(2,4)==8