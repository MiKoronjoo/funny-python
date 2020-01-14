def gen():
    i = 0
    while True:
        yield i
        i += 1

a = (x for x in range(20))
print('12 in a ->', 12 in a)
print('12 in a ->', 12 in a)
b = gen()
print('345 in b ->', 345 in b)
print('b.__next__() ->', b.__next__())
print('345 in b ->', 345 in b)  # infinite loop
