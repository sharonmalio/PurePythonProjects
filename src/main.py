import math

class square():
    def squiring(self):
        a = [1,2,3,4]
        for a in [1,2,3,4]:
            newa = a ** a
            print ("the new list is: ", newa)

square().squiring()
class Calculate():
    def calculations(self):
        a = int(input(" please enter a value for a:"))
        b = int(input(" please enter a value for b:"))
        c = int(input(" please enter a value for c:"))
        if a > 0:
            total = a + b + c
            print("The total is:",total)
            # print "i am a woman "
        else:
            print('error')

Calculate().calculations()

class Largest():
    def large(self):
        a = int (input ("please enter a valuje for a:"))
        b = int (input("please enter a value for b:"))
        Max = a
        if a > b:
            print ("the max is a. ")

        else:
            print ("the max is b.")
Largest().large()

class swap():
    def swapping(self):
        a = int(input( "please enter a value for a:\n "))
        b = int(input("please enter a value for b:\n"))
        a,b = b,a
        print ("the value for b is: ", b )
        print("the value for a is:  ", a)
swap().swapping()