# 4. Function returning multiple values
def calc(a, b):
    return a+b, a-b, a*b
s, d, m = calc(10, 5)
print("Sum =", s, "Diff =", d, "Mul =", m)