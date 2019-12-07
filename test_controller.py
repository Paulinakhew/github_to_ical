import pytest
import controller as c


def test_create_event():
    assert c.create_event() == True
