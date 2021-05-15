import random
import time


# user topics
feeling1 = ["sad", "depressed", "sorrow", "heart broken","heartbroken"]
feeling2 = ["Happy","happy", "Cheerful", "cheerful","overjoyed","OverJoyed","Energetic","energetic"]
sayingok = ["OKAY", "OK", "SORRY","FINE","UGH"]
sayingyes = ["yes!", "absoultely", "yep", "i am","i sure am","yes","uh huh"]
sports = ["sport","sports","football", "swimming", "tennis", "Street Hockey","Dancing","Rugby","Softball","Handball","Soccer"]
censor = ["nigga", "spic", "fag","faggot","nigger"]
sayingthanks = ["thanks", "thank you", "thx","tysm","ty","thank","thanks!", "thank you!", "thx!","tysm!","ty!","thank!",]
sayingno = ["nope", "no", "i am not","im good","good","im alright","not"]
greeting = ["how are you","how are u", "are you good", "how are","are u good","whats up","what's up"]
topiclove = ["i love him","i am in love", "love", "i am in love"]
topicloving = ["love you!","love u", "i love you", "i love u","love you"]
topicpraying = ["praying","pray", "i prayed", "i prayed"]
topicmusic = ["i love music","song", "favoriate song", "music"]
topicschool = ["homework","school"]
topiccomedy = ["funny"]
topicmoney = ["wealth","money"]

# bot responses

# greeting
g1 = ["GREETING ONE ANOTHER", "Welcome one another as Christ has welcomed you", "greet God each day", "Greet one another with the kiss of love. Peace to all of you who are in Christ.", "Greet all the brothers with a holy kiss."]
# feeling1
g2 = ["Praying will wipe away every tear from their eyes, and death shall be no more, neither shall there be mourning, nor crying, nor pain anymore, for the former things have passed away","The Good News: In heaven, we will feel no pain, no sorrow, and there will be no death"]
# feeling2
g3 = ["Why are feeling like this!","Awesome, why are you feeling like this today?"]
# sayingok
g4 = ["Next topic","Next"]
# sayingyes
g5 = ["Next topic","Next"]
# sports
g6 = ["if anyone competes in athletics, he is not crowned unless he competes according to the rules."]
# censor
g7 = ["watch it","stop"]
# sayingthanks
g8 = ["your welcome.","very much welcome."]
# sayingno
g9 = ["okay","ok"]
# greeting
g10 = ["how are you!","how are you too?"]
# topiclove
g11 = ["1 Corinthians 13:4-5: Love is patient, love is kind. It does not envy, it does not boast, it is not proud. It does not dishonor others, it is not self-seeking, it is not easily angered, it keeps no record of wrongs"]
# topicloving
g12 = ["We love you too.","Love you too."]
# topicpraying
g13 = ["When you pray, say: Father, hallowed be your name, your kingdom come. Give us each day our daily bread. Forgive us our sins, for we also forgive everyone who sins against us.","Praying is Great."]
# topicmusic
g14 = ["songs of praise, songs of victory, songs of mourning, and above all the Psalms. Dances were also a common music expression along with the combination of singing with instrumental music"]
# topicschool
g15 = ["“Where God guides, he provides.” – Isaiah 58:11"," “They will soar on wings like eagles.” – Isaiah."]
# topiccomedy
g16 = ["God, who sits in Heaven, laughs; the Lord scoffs at them.” — Psalm 2:4", "There is nothing better for a person than that he should eat and drink and find enjoyment in his toil. This also, I saw, is from the hand of God"]
# topicmoney
g17 = ["Proverbs 13:11 Dishonest money dwindles away, but whoever gathers money little by little makes it grow.", "Proverbs 22:16 Whoever oppresses the poor for his own increase and whoever gives to the rich, both come to poverty."]


# this will be used to generate text if any topic or keyword above isnt detected.

def words():
    with open("Happy.TXT") as f:
        gdWrds = f.read().splitlines()

    print(end="God says... ")

    for x in range(0, 30):
        wrds = random.choice(gdWrds)
        print(wrds, end=" ")

    wrds = random.choice(gdWrds)
    print(wrds + ".\n")


def main():
    print('say hello!')
    while True:
        var = input('> ')
        if any(keyword in var for keyword in greeting):
            print(end='God Says... ')
            print(random.choice(g1))
        
        elif any(keyword in var for keyword in feeling1):
            print(end='God Says... ')
            print(random.choice(g2))
        
        elif any(keyword in var for keyword in feeling2):
            print(end='God Says... ')
            print(random.choice(g3))

        elif any(keyword in var for keyword in sports):
            print(end='God Says... ')
            print(random.choice(g4))

        elif any(keyword in var for keyword in censor):
            print(end='God Says... ')
            print(random.choice(g5))
        
        elif any(keyword in var for keyword in sayingthanks):
            print(end='God Says... ')
            print(random.choice(g6))
        
        elif any(keyword in var for keyword in sayingno):
            print(end='God Says... ')
            print(random.choice(g7))
        
        elif any(keyword in var for keyword in topiclove):
            print(end='God Says... ')
            print(random.choice(g8))

        elif any(keyword in var for keyword in topicpraying):
            print(end='God Says... ')
            print(random.choice(g9))

        elif any(keyword in var for keyword in topicmusic):
            print(end='God Says... ')
            print(random.choice(g10))

        elif any(keyword in var for keyword in greeting):
            print(end='God Says... ')
            print(random.choice(g11))

        elif any(keyword in var for keyword in greeting):
            print(end='God Says... ')
            print(random.choice(g12))

        elif any(keyword in var for keyword in greeting):
            print(end='God Says... ')
            print(random.choice(g13))

        elif any(keyword in var for keyword in greeting):
            print(end='God Says... ')
            print(random.choice(g14))

        elif any(keyword in var for keyword in greeting):
            print(end='God Says... ')
            print(random.choice(g15))

        elif any(keyword in var for keyword in greeting):
            print(end='God Says... ')
            print(random.choice(g16))

        elif any(keyword in var for keyword in greeting):
            print(end='God Says... ')
            print(random.choice(g17))
        else:
            words()

# Welcome
print('Welcome to AskGod.')
print('The More You Talk, The More The Bot Learns About You, SESSIONS ARE NOT SAVED')
print('Please wait.')
time.sleep(3)
main()
