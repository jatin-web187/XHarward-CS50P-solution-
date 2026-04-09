import pytest
from um import count
def main():
    test_count_insenstivity()
    test_substring()
    test_valid_input()
def test_count_insenstivity():
    assert count("Um,thank for the album")==1
    assert count("Um,hello,um,world")==2
def test_substring():
    assert count("yummy")==0
    assert count("album")==0
def  test_valid_input():
    assert count("hello,um,world")==1
    assert count("um.......")==1
if __name__=="__main__":
    main()

