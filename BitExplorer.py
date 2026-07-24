a=10
b=6

def bits(n, width=4):
    return format (n&((1<<width)-1), f'0{width}b')
print("Bit Explorer")
print("A=", a, "->", bits(a))
print("B=", b, "->", bits(b))
print()
print("AND a&b=", a&b, "->", bits(a&b))
print("Or a|b", a|b, "->", bits(a|b))
print("NOT a", ~a, "->", bits(~a))
print("NOT b", ~b, "->", bits(~b))
print("XOR a^b", a^b, "->", bits(a^b))
print("Left a<<1", a<<1, "->", bits(a<<1))
print("Right a>>1", a>>1, "->", bits(a>>1))
print("Left b<<1", b<<1, "->", bits(b<<1))
print("Right b>>1", b>>1, "->", bits(b>>1))