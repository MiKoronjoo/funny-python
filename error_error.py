class C:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        with C() as c:
            1 / 0


with C() as c:
    1 / 0

# During handling of the above exceptions, RecursionError occurred !!
