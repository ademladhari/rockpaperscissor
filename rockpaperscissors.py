import random



tie=0 
wr=0
wp=0
ws=0
lr=0
lp=0
ls=0
total=100000
bot1=["Rock","Paper","Scissors"]
bot2=["Rock","Paper","Scissors"]

def winlose(rnd1,rnd2):
    global tie,wr,wp,ws,ls,lr,lp
    if (bot1[rnd1]==bot2[rnd2]):
        tie=tie+1
    elif (bot1[rnd1] == "Rock" and bot2[rnd2] == "Scissors")  :
        wr=wr+1
    elif (bot1[rnd1] == "Paper" and bot2[rnd2] == "Rock") :
        wp=wp+1
    elif (bot1[rnd1] == "Scissors" and bot2[rnd2] == "Paper") :
        ws=ws+1
    elif (bot1[rnd1] == "Rock" and bot2[rnd2] == "Paper")  :
        lr=lr+1
    elif (bot1[rnd1] == "Paper" and bot2[rnd2] == "Scissors") :
        lp=lp+1
    elif (bot1[rnd1] == "Scissors" and bot2[rnd2] == "Rock") :
        ls=ls+1

def winrate(r):
    for i in range(total):
        rnd2=random.randint(0,2)
        winlose(r,rnd2)
print("winrate if both random")

for i in range(total):
    rnd2=random.randint(0,2)
    rnd1=random.randint(0,2)
    winlose(rnd1,rnd2)
print(wr/total,ws/total,wp/total)
wr=0
ws=0
wp=0
print("winrate if you put only rock")
winrate(0)
print(wr/total)
print("winrate if you put only paper")
winrate(1)
print(wp/total)
print("winrate if you put only scissors")
winrate(2)
print(ws/total)

