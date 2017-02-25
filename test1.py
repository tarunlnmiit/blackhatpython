def sum(num1, num2):
    num1int = convert_integer(num1)
    num2int = convert_integer(num2)
    
    res = num1int + num2int
    
    return res


def convert_integer(num):
    return int(num)


ans = sum('1', '2')