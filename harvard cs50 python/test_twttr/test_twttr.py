from twttr import shorten
def main():
    test_twttr()

def test_twttr():
    assert shorten("jatin")=="jtn"
    assert shorten("JATIN")=="JTN"
    assert shorten("JaTIn")=="JTn"
    assert shorten("12345567")=="12345567"
    assert shorten("@#&*$!")=="@#&*$!"

if __name__=="__main__":
    main()

