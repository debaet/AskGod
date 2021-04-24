import random
import colorama
from colorama import Fore, Back, Style
import os
import time 
colorama.init()


# these are just keywords please ignore these. do NOT delete this


keywords1 = ["sad", "depressed", "sorrow", "heart broken","heartbroken"]
keywords = ["OKAY", "OK", "SORRY","FINE","UGH"]
keywords2 = ["yes!", "absoultely", "yep", "i am","i sure am","yes","uh huh"]
keywords3 = ["sport","sports","football", "swimming", "tennis", "Street Hockey","Dancing","Rugby","Softball","Handball","Soccer"]
notgoodwords = ["nigga", "spic", "fag","faggot","nigger"]
thanks = ["thanks", "thank you", "thx","tysm","ty","thank","thanks!", "thank you!", "thx!","tysm!","ty!","thank!",]
nope = ["nope", "no", "i am not","im good","good","im alright","not"]
greetings = ["how are you","how are u", "are you good", "how are","are u good","whats up","what's up"]

# these are just keywords please ignore these. any racist words are just used to filter any inputs.


def main():
    with open("Happy.TXT") as f:
        gdWrds = f.read().splitlines()

    print(end="God says... ")

    for x in range(0, 30):
        wrds = random.choice(gdWrds)
        print(wrds, end=" ")

    wrds = random.choice(gdWrds)
    print(wrds + ".\n")


def topicsport():
		if any(keyword in user3 for keyword in keywords3):
			print("God says... if anyone competes in athletics, he is not crowned unless he competes according to the rules. whats your favoriate sport?")
			user4 = input('> ')

			if any(keyword in user4 for keyword in notgoodwords):
				print("God Says... please pray.")

			else:
				print('God says...' + user3 + "is a good sport")
				main()



def qna():
		var = input('> ')
		main()
		if var in ("What’s happening","How’s it going?","Good evening","Hey, boo","How are you?","Nice to meet you!","Long time no see","What’s the good word?","What’s new?","Look who it is!","How have you been?","Nice to see you again.","Greetings and salutations!","How are you doing today?","What have you been up to?","How are you feeling today?","Look what the cat dragged in!","Good afternoon, sir, how are you today?""Hello, sunshine!","Howdy, partner!","Hey, howdy, hi!","What’s kickin’, little chicken?","Peek-a-boo!","Howdy-doody!","Hey there, freshman!","My names Ralph and Im a bad guy.","Hi, mister!","I come in peace!","Put that cookie down!","Ahoy, matey!","Hiya!","‘Ello, govnor!","Top of the mornin’ to ya!","What’s crackin’?","GOOOOOD MORNING, VIETNAM!","‘Sup, homeslice?","This call may be recorded for training purposes.","Howdy, howdy ,howdy!","How does a lion greet the other animals in the field? A: Pleased to eat you.","Hello, my name is Inigo Montoya.","Im Batman.","At least, we meet for the first time for the last time!","Hello, whos there, Im talking.","Heres Johnny!","You know who this is.","Ghostbusters, whatya want?","Yo!","Whaddup.","Greetings and salutations!","Doctor.","‘Ello, mate.","Heeey, baaaaaby.","Hi, honeybunch!","Oh, yoooouhoooo!","How you doin,I like your face.","Whats cookin, good lookin?","Howdy, miss.","Why, hello there!","Hey, boo.","hi","hello","yo","sup","hey","heyy","heyyy","hello"):
			with open("Greet.TXT") as f:
				greetings = f.read().splitlines()

			print(end="God Answered: ")
			wrds1 = random.choice(greetings)
			print(wrds1 + ".\n")

		else:
			print('...ha')


		while True:
			var = input('> ')
			if var in ("who is god", "whos god", "what is god", "who is god", "what is god", "who god", "What’s happening","How’s it going?","Good evening","Hey, boo","How are you?","Nice to meet you!","Long time no see","What’s the good word?","What’s new?","Look who it is!","How have you been?","Nice to see you again.","Greetings and salutations!","How are you doing today?","What have you been up to?","How are you feeling today?","Look what the cat dragged in!","Good afternoon, sir, how are you today?""Hello, sunshine!","Howdy, partner!","Hey, howdy, hi!","What’s kickin’, little chicken?","Peek-a-boo!","Howdy-doody!","Hey there, freshman!","My names Ralph and Im a bad guy.","Hi, mister!","I come in peace!","Put that cookie down!","Ahoy, matey!","Hiya!","‘Ello, govnor!","Top of the mornin’ to ya!","What’s crackin’?","GOOOOOD MORNING, VIETNAM!","‘Sup, homeslice?","This call may be recorded for training purposes.","Howdy, howdy ,howdy!","How does a lion greet the other animals in the field? A: Pleased to eat you.","Hello, my name is Inigo Montoya.","Im Batman.","At least, we meet for the first time for the last time!","Hello, whos there, Im talking.","Heres Johnny!","You know who this is.","Ghostbusters, whatya want?","Yo!","Whaddup.","Greetings and salutations!","Doctor.","‘Ello, mate.","Heeey, baaaaaby.","Hi, honeybunch!","Oh, yoooouhoooo!","How you doin,I like your face.","Whats cookin, good lookin?","Howdy, miss.","Why, hello there!","Hey, boo.","hi","hello","yo","sup","hey","heyy","heyyy","hello"):
				print('Im_God_and_youre_not Im_God_who_the_hell_are_you')

			elif any(keyword in var for keyword in greetings):
				print('')
			
			else:
				main()
				print('if question was not Answered please ask again.')




			if any(keyword in var for keyword in keywords1):
				print("God says... Are you upset?")




			elif any(keyword in var for keyword in keywords):
				print("God says... Are you upset?")

			elif any(keyword in var for keyword in keywords3):
				print("God says... if anyone competes in athletics, he is not crowned unless he competes according to the rules. whats your favoriate sport?")
				

	

			depressed = input('> ')

			if any(keyword in depressed for keyword in keywords):
				print("God says... Are you upset?")

			asking = input('> ')
			
			if any(keyword in asking for keyword in keywords2):
				print('God says... the best advice i shall give is to present your requests to me while praying. And the peace of us, which transcends all understanding, will guard your hearts and your minds in Christ Jesus')
			
			elif any(keyword in asking for keyword in nope):
				print('God Says... great')
				main()



			user = input('> ')

			if any(keyword in user for keyword in thanks):
				print('God says...  your very much welcome')
			else:
				main()


		# stating keywords for new lines after current one


			user2 = input('> ')

			if any(keyword in user2 for keyword in keywords):
				print("God says... Are you upset?")

			var79 = input('> ')
			

			if any(keyword in var79 for keyword in keywords2):
				print('God says.. Why?')

			elif any(keyword in var for keyword in keywords3):
				print("God says... if anyone competes in athletics, he is not crowned unless he competes according to the rules. whats your favoriate sport?")
				


			user6 = input('> ')

			if any(keyword in user6 for keyword in notgoodwords):
				print("God Says... pray.")


			elif any(keyword in var79 for keyword in notgoodwords):
				print("God Says... we cannot ignore when someone is being bullied. please pray.")

			elif any(keyword in var79 for keyword in keywords):
				print("God says... Are you upset?")


			else:
				main()


			user3 = input('> ')
			print('God says.. having wisdom and understanding people, and new things is better than having silver or gold. ')





def frontpage():
	print(Fore.MAGENTA + """ _______________
< Hello, world! Please wait.  >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                
                ||     ||""" + Style.RESET_ALL + Style.BRIGHT)
	time.sleep(5)
	os.system('cls' if os.name == 'nt' else 'clear')
	print(Fore.MAGENTA + """ ______________________________
< Welcome to AskGod. You will be Redirected to the Menu now.  >
 ----------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (l_l)\       )\/\
                
                ||     ||""" + Style.RESET_ALL + Style.BRIGHT)
	time.sleep(5)
	os.system('cls' if os.name == 'nt' else 'clear')
	print ('')
	print ('################################')
	print ('#  First God ChatBot  AskGod   #')
	print ('#             v3.0             #')
	print ('# ---------------------------- #')
	print ('#  Written by debaet/w3lcs     #')
	print ('#  github.com/debaet/AskGod    #')
	print ('#                              #')
	print ('################################\n')

	print ('')
	print ('################################')
	print ('#        Selection Menu        #')
	print ('#         Type a Number        #')
	print ('# ---------------------------- #')
	print ('#  1. Get New Words            #')
	print ('#  2. Chatbot(beta)            #')
	print ('#  3. Bible Verses             #')
	print ('################################\n')

	selection = input('Enter a Number: ')


	if selection=="1":
		#words()
		print('sorry not done yet')


	elif selection=="2":
		qna()

	elif selection=="3":
		#bible()
		print('sorry not done yet')


    
def questions():
	print('you made a great decision!')
	print('as stated before all this information is not stored anywhere.')
	print('these questions are NOT randomly generated.')
	print('this information will be used for the bot to learn more about you.')
	q1 = input('how old are you?')
	q2 = input('how happy do you feel?')
	q3 = input('what do you like to do?')
	q4 = input('do you like music?')
	q5 = input('do you read the bible?')
	q6 = input('do you feel safe?')
	print('thank you for providing information to enhance your exprience!')
	frontpage()






	# note to self , start code above. not below.




print('welcome to AskGod, ask a question and your question will be answered using Gods Terminology.')
print('============================================================================================')
print('in order to have the best exprience, you may need to answer some questions. you may chose whether or not you want to partake in the survey.')

variable = input('will you answer some questions to teach the bot about yourself? (y/n use lowercase only)')





if variable=="y":
	questions()
else:
	frontpage()
	


