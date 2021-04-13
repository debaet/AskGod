import random

def main():
    with open("Happy.TXT") as f:
        gdWrds = f.read().splitlines()

    print(end="God says... ")

    for x in range(0, 30):
        wrds = random.choice(gdWrds)
        print(wrds, end=" ")

    wrds = random.choice(gdWrds)
    print(wrds + ".\n")


print('ask a question, god will send a decoded message')
var = input('Start with a greeting ')


if var in ("hey", "hello", "hi", "sup", "yo"):
	with open("Greet.TXT") as f:
		greetings = f.read().splitlines()

	print(end="God says... ")
	wrds1 = random.choice(greetings)
	print(wrds1 + ".\n")

else:
	print('...ha')

while True:
	var1 = input('Ask God: ')
	if var1 in ("who is god", "whos god", "what is god", "who is god"):
		print('Im_God_and_youre_not Im_God_who_the_hell_are_you')
	else:
		print(' ')
	main()
	
	    
