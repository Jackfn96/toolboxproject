from toolboxproject.lib import greet, who_am_i

def test_greet():
    assert type(greet('Jack')) == str

def test_who_am_i():
    assert type(who_am_i('Jack')) == str
