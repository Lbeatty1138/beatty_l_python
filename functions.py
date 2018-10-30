def greetings():
	print("hello from the greetings function")


# the greeting cution just says hello
# invoke or call the function
greetings()


def greetingsWithArgs(msg="a default message"):
	print("now we're saying", msg, "from another function")

greetingsWithArgs()
# this should come up with the defualt message because it was never given a value
greetingsWithArgs("somthing completely different")
greetingsWithArgs("this should never crash")

# variables and scope
myNumberVariable = 10


#  returning values from functions (very powerful)
def someMath(num1=2, num2=4):
	global myNumberVariable

	myNumberVariable = num1 + num2
	return num1 + num2


sum = someMath()
print("we are doing some math and getting", sum)

sum = someMath(10, 15)
print("another math operation with", sum, "as the result")


