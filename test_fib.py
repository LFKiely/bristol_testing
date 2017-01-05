

def int_small():
    input(4)
    calc_ans = fib(input)
    exp_ans = 3
    assert calc_ans == exp_ans

def int_large():
    input(30)
    calc_ans = fib(input)
    exp_ans = 832040
    assert calc_ans == exp_ans


