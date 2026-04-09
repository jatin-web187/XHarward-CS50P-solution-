from fuel import gauge,convert
import pytest
def test_covert():
     assert convert("1/2")==50
     assert convert("100/100")==100
     with pytest.raises(ZeroDivisionError):
          convert("2/0")
     with pytest.raises(ValueError):
          convert("cat/dog")
     with pytest.raises(ValueError):
          convert("-1/2")
def test_gauge():
     assert gauge(100)=="F"
     assert gauge(99)=="F"
     assert gauge(1)=="E"
     assert gauge(23)=="23%"
