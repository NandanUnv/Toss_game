# start your guessing

import random as ra

i = input("Guess the toss?(Heads/Tails):")
l = ['Heads','Tails']
ch = ra.choice(l)

if ch=='Heads':
    if i==ch:
        print("Toss:",ch)
        print("won the toss")
    else:
        print("Toss:",ch)
        print("loss the toss")
else:
    if i == ch:
        print("Toss:",ch)
        print("won the toss")
    else:
        print("Toss:",ch)
        print("loss the toss")
