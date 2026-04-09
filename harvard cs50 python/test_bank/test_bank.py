from bank import value
def main():
    test_bank()
def test_bank():

    assert value("hello") == 0
    assert value("Hello") == 0
    assert value(" hello ") == 0
    assert value("hi") == 20
    assert value("what's up") == 100

if __name__=="__main__":
    main()

