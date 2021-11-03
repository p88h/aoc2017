# a0 = 65
# b0 = 8921
a0 = 722
b0 = 354
def next_a(x):
    x *= 16807
    return x % 2147483647
def next_b(x):
    x *= 48271
    return x % 2147483647
t = 0
for r in range(40000000):
    a0 = next_a(a0)
    b0 = next_b(b0)
    if (a0 ^ b0) & 0xFFFF == 0:
        t += 1
print(t)
a0 = 722
b0 = 354
q = 0 
for r in range(5000000):
    a0 = next_a(a0)
    while a0 % 4 != 0:
        a0 = next_a(a0)
    b0 = next_b(b0)
    while b0 % 8 != 0:
        b0 = next_b(b0)
    if (a0 ^ b0) & 0xFFFF == 0:
        q += 1
print(q)
