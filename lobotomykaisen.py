import random
import array

j = 1
choose = ["nah",    "i'd win",     "because",   "the honored one",     "the one who left it all behind",    "and his overwhelming strength", "i'm you",   
"wallahi we are built different",   "stand proud",   "you are strong",  "as the king of curses",    "jogoat",  "throughout the heavens and the earth",  
"I alone am the",  "honored one",  "fucking monkeys",   "with this deving treasure I summon",   "always bet on hakari kinji",   "opened his domain"]


i = 0
temp = choose
final = []
for x in temp:
    k=i
    i = random.randint(0,len(choose)-1)
    if(i!=k):
        final.append(temp[i])
    else:
        i = k-1
        final.append(temp[i])
    if (j%3==0):
        temp.pop(i)
           j+=1

n1 = random.randint(0,len(choose)-1)
n2 = random.randint(0,len(choose)-1)

z1= final[n1]
z2 = final[n2]

geto = "are you " + z1 +" or are you " + z2
    
final.insert(i, geto)
s2= ""
for y in final:
    s1 = s2 + " " + y
    s2 = s1
print(s2)