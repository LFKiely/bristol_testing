import numpy as np

def test_yzero():
    x = 1.
    y = 0.
    calc_ans = sinc2d(x,y)
    exp_ans = np.sin(x)/x
    assert calc_ans == exp_ans 

def test_xzero():
    x = 0
    y = 2.3
    calc_ans = sinc2d(x,y)
    exp_ans = np.sin(y)/y
    assert calc_ans == exp_ans

def test_xyzero():
    calc_ans = sinc2d(0,0)
    exp_ans - 1
    assert calc_ans == exp_ans

def test_notzero():
    x = 5.6
    y = 0.4
    calc_ans = sinc2d(x,y)
    ex_ans = (np.sin(x)/x)*(np.sin(y)/y)
    assert calc_ans == ex_ans
    

