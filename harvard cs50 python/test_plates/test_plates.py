from plates import is_valid
def test_len():
    assert is_valid("A")==False
    assert is_valid("ASDFGHJ")==False
    assert is_valid("AA")==True
    assert is_valid("asdfgh")==True
def test_letter():
    assert is_valid("a1")==False
    assert is_valid("Aa23we")==False
    assert is_valid("aer1")==True
    assert is_valid("11")==False
def test_onlyletter():
    assert is_valid("Aa!56")==False
    assert is_valid("Ajk@mdk")==False
    assert is_valid("Ar5%$ks")==False
    assert is_valid("As!&uy")==False
def test_zero():
    assert is_valid("aa12")==True
    assert is_valid("aa01")==False

