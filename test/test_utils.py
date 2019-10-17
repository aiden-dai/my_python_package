from ad_python.utils import func_add

def test_func_add():

    x, y = 3, 5
    z = func_add(x, y)
    # z = 8
    assert z == 8



class TestUtils():

    def test_func_add(self):
        
        z = func_add(3, 4)
        assert z == 7