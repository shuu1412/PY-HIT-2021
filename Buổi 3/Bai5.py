from functools import reduce
def MyMathShower(*args):
    """
    :param:
    input:
         nhập 1 mảng tham số
    output:
        Tổng, Tích, Hiệu của mảng tham số
    """
    return reduce(lambda x, y: x + y,args), reduce(lambda x, y: x * y, args), reduce(lambda x, y: x - y, args)

a = list(map(float, input().split()))
print(MyMathShower(*a))