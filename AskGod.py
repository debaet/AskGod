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

ha

if var in (("What’s happening","How’s it going?","Good evening","Hey, boo","How are you?","Nice to meet you!","Long time no see","What’s the good word?","What’s new?","Look who it is!","How have you been?","Nice to see you again.","Greetings and salutations!","How are you doing today?","What have you been up to?","How are you feeling today?","Look what the cat dragged in!","Good afternoon, sir, how are you today?""Hello, sunshine!","Howdy, partner!","Hey, howdy, hi!","What’s kickin’, little chicken?","Peek-a-boo!","Howdy-doody!","Hey there, freshman!","My names Ralph and Im a bad guy.","Hi, mister!","I come in peace!","Put that cookie down!","Ahoy, matey!","Hiya!","‘Ello, govnor!","Top of the mornin’ to ya!","What’s crackin’?","GOOOOOD MORNING, VIETNAM!","‘Sup, homeslice?","This call may be recorded for training purposes.","Howdy, howdy ,howdy!","How does a lion greet the other animals in the field? A: Pleased to eat you.","Hello, my name is Inigo Montoya.","Im Batman.","At least, we meet for the first time for the last time!","Hello, whos there, Im talking.","Heres Johnny!","You know who this is.","Ghostbusters, whatya want?","Yo!","Whaddup.","Greetings and salutations!","Doctor.","‘Ello, mate.","Heeey, baaaaaby.","Hi, honeybunch!","Oh, yoooouhoooo!","How you doin,I like your face.","Whats cookin, good lookin?","Howdy, miss.","Why, hello there!","Hey, boo.","hi","hello","yo","sup","hey","heyy","heyyy","hello")):
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
	
	    
