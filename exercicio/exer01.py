def mul(m):
    def mul_n(n):
        return m * n
    return mul_n
s1 = mul(2)
s2 = mul(3)
s3 = mul(4)


print(s3(1))