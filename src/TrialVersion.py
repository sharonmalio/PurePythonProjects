#using iteraton
count = 0
x_list = 0
sum = 0

for x in  [2,6,7,8,9]:
    x_list.append(x)
    for value in x_list:
        sum+= int(value)
    print("the sum is:", sum)
    count = count + 1

    print("the count is:", count)

#using random for random numbers
import random
for i in range(70):
    x = random.random()
    print (x)

x = 5
y = x + 1
print (x)
print (y)
quotient = x/y
reminder = x%y
#printing out a statement
print ("the quotient is:", quotient)
print ("the reminder is:", reminder)
#concatination
first = "i am sick"
sec = "please lets go home"

print (first + sec)

#asking fror  a users input
class work():
    def pay(self):
        try:
            hours = int(input("please enter your working hours:\n"))
            rate = float(input("kindly give your rate per hour:\n"))

            if hours > 45:
                newrate = rate * 1.5
                pay = hours * newrate

                print( pay)
            else:
                #print "your pay is"  + str(pay)  + "per hour"
                pay = hours * rate
                print (pay)

                print ("the rate  can not be a below zero value")
        except:
            print ("Lets deal with numbers only")

work().pay()

class score():
    def grade(self):
        try:
            x = float(input("enter a number between 0.0 1nd 1.0"))
            if x == 0:
                print ("fail")
            elif x > 0 and x < 0.95:
                print ("B")
            elif x > 0.95:
                print ("A")

        except:
            print("must not be greater than 1")


score().grade()


#asking fror  a users input
name = input("what is your name?:")

print("Hello "+ name+"!")

place = str(input("where do you come from?:"))

print (place + "that is a nice town")

age = int(input("how old are you?:"))

print ("what?,"+ str(age) +"that is so young!")

class temperature():
    def converter(self):
        temp = float(input("kindly enter the value you wanty to convert in degrees:\n"))
        fahrenheit = temp + 33
        print ("your value converted is:",fahrenheit)
temperature().converter()

