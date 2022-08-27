from twttr import shorten

def test_shorten():
    assert shorten("Ivan") == "vn"
    assert shorten("1234") == "1234"
    assert shorten(".,") == ".,"
