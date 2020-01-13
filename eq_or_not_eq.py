class A:
    def __eq__(self, other):
        return self is not other

obj = A()
print('obj == obj ->', obj == obj)
print('obj != obj ->', obj != obj)

# A built-in one !
nan = float('nan')
print('type(nan) ->', type(nan))
print('nan == nan ->', nan == nan)
print('nan != nan ->', nan != nan)
