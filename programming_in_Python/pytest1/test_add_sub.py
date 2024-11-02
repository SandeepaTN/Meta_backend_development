import add_sub
import pytest

def test_add():
    assert add_sub.add(5,4)==9

def test_sub():
    assert add_sub.sub(5,4)==1

