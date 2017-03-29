class swapping():
    def fswap(self):
        a= raw_input("first")
        b=raw_input("second")
        a,b = b, a
        print("the value for a is", a)
        print("the value for b is", b)

swapping().fswap()
